import asyncio
import websockets
import json
import numpy as np

# Constanten uit de VORTEX architectuur
COLUMNS = 18
ROWS = 13
TOTAL_NODES = 234
NULPUNT = (9, 9)
BASE_FREQ = 110.0

def calculate_telemetry(node_value):
    """Berekent de parameters voor een specifieke node."""
    # Helix Hoek (Sprong 19)
    next_pos = ((node_value - 1) + 19) % TOTAL_NODES
    dx = (next_pos % COLUMNS - (node_value - 1) % COLUMNS) % COLUMNS
    dy = next_pos // COLUMNS - (node_value - 1) // COLUMNS
    angle_rad = np.arctan2(dx, dy if dy != 0 else 1e-9)
    angle = np.degrees(angle_rad)

    # Modulaire zwaartekracht
    digitsum = sum(int(d) for d in str(node_value))
    grid_x = (node_value % 17) + 1
    grid_y = ((node_value // 17) % 17) + 1
    distance = abs(grid_x - NULPUNT[0]) + abs(grid_y - NULPUNT[1])

    # 13-Limiet Freq
    reine_ratio = (((node_value % 2) + 1) * (((node_value % 3) ** 2) + 1) * ((node_value % 13) + 1)) / 8
    freq = BASE_FREQ * reine_ratio
    
    return next_pos + 1, angle, distance, digitsum, freq

async def vortex_stream(websocket):
    print(">>> VORTEX OMNI-BRIDGE: Frontend verbonden.")
    node = 1
    
    try:
        while True:
            # Bereken telemetrie voor de huidige node
            next_node, angle, distance, d_sum, freq = calculate_telemetry(node)
            
            # Bouw de JSON payload
            payload = {
                "timestamp": asyncio.get_event_loop().time(),
                "currentNode": node,
                "nextNodeELS": next_node,
                "helixAngle": round(angle, 2),
                "gravityDistance": distance,
                "harshadDivisor": d_sum,
                "audioFreq": round(freq, 4)
            }
            
            # Stuur data naar de Vue frontend
            await websocket.send(json.dumps(payload))
            
            # De slaapcyclus bepaalt de pulssnelheid. 
            # We gebruiken de 13.75 Hz hartslag als basis voor de data-interval (1 / 13.75 sec)
            await asyncio.sleep(1 / 13.75)
            
            # Schuif door de matrix
            node = node + 1 if node < TOTAL_NODES else 1
            
    except websockets.exceptions.ConnectionClosed:
        print("<<< VORTEX OMNI-BRIDGE: Verbinding verbroken.")

async def main():
    print("VORTEX Backend Initialized. Wachten op connectie via ws://localhost:8765...")
    async with websockets.serve(vortex_stream, "localhost", 8765):
        await asyncio.Future()  # Houdt de server oneindig draaiend

if __name__ == "__main__":
    asyncio.run(main())
