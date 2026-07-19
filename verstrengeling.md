<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VORTEX - Quantum Spin Matrix</title>
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <style>
        :root {
            --bg-color: #050505;
            --text-color: #e0e0e0;
            --accent-color: #00ffcc;
            --dimmed-color: #222222;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }

        .dashboard {
            background: #111;
            padding: 30px;
            border-radius: 8px;
            border: 1px solid #333;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.1);
            max-width: 800px;
            width: 100%;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 1px solid #333;
            padding-bottom: 10px;
        }

        /* De Matrix Grid */
        .matrix {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-bottom: 30px;
        }

        /* Node Styling */
        .node {
            background: #1a1a1a;
            border: 1px solid var(--accent-color);
            padding: 20px;
            border-radius: 4px;
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            position: relative;
        }

        .node-title {
            font-size: 0.9em;
            color: #888;
            margin-bottom: 10px;
        }

        .node-value {
            font-size: 1.5em;
            font-weight: bold;
        }

        /* Visuele Dimming: Hamming-Minimalisme (Spinwaarde 0) */
        .dimmed {
            opacity: 0.15;
            border-color: #333;
            transform: scale(0.98);
        }

        .controls {
            display: flex;
            justify-content: space-between;
        }

        button {
            background: transparent;
            color: var(--accent-color);
            border: 1px solid var(--accent-color);
            padding: 10px 20px;
            font-family: inherit;
            cursor: pointer;
            transition: background 0.2s, color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        button:hover {
            background: var(--accent-color);
            color: var(--bg-color);
        }
    </style>
</head>
<body>

    <div id="vortex-app">
        <div class="dashboard">
            <div class="header">
                <h2>VORTEX_CORE :: Q-SPIN MATRIX</h2>
                <p>Status: {{ isEntangled ? 'SUPERPOSITIE ACTIEF' : 'DISCRETE STATUS' }}</p>
            </div>

            <div class="matrix">
                <div 
                    v-for="rule in spinRules" 
                    :key="rule.id" 
                    class="node" 
                    :class="{ dimmed: rule.x === 0 }"
                >
                    <div class="node-title">Node {{ rule.id }} [Paar {{ rule.pair }}]</div>
                    <div class="node-value">
                        Spin: {{ rule.x }}<br>
                        Amp: $ {{ rule.amplitude.toFixed(3) }}
                    </div>
                </div>
            </div>

            <div class="controls">
                <button @click="resetState">Reset (Hamming Collapse)</button>
                <button @click="triggerEntanglement">Simuleer Verstrengeling ($\frac{1}{\sqrt{2}}$)</button>
            </div>
        </div>
    </div>

    <script>
        const { createApp, ref } = Vue;

        createApp({
            setup() {
                // Fundamentele kwantumconstante
                const ENTANGLEMENT_CONSTANT = 0.70710678; // 1/sqrt(2)

                // De reactieve "Sparse" Systeemstatus
                const isEntangled = ref(false);
                
                // Initiële staat: asymmetrisch geladen (Hamming-gewicht 2)
                const initialState = [
                    { id: 0, pair: 'A', x: 1, amplitude: 1.0 },
                    { id: 1, pair: 'A', x: 0, amplitude: 0.0 },
                    { id: 2, pair: 'B', x: 1, amplitude: 1.0 },
                    { id: 3, pair: 'B', x: 0, amplitude: 0.0 }
                ];

                const spinRules = ref(JSON.parse(JSON.stringify(initialState)));

                // Functie voor de 0.707 amplitude splitsing
                const triggerEntanglement = () => {
                    isEntangled.value = true;
                    
                    // Koppel de regels paarsgewijs (0-1 en 2-3)
                    // We simuleren de Bell-staat verdeling
                    spinRules.value.forEach(rule => {
                        // Alle nodes in een verstrengeld paar lichten op (spin > 0 ongedaan maken van de dim)
                        rule.x = 1; 
                        // De energie (amplitude) wordt hoekgetrouw gesplitst
                        rule.amplitude = ENTANGLEMENT_CONSTANT;
                    });
                };

                // Functie om de golf te laten instorten naar discrete bits
                const resetState = () => {
                    isEntangled.value = false;
                    spinRules.value = JSON.parse(JSON.stringify(initialState));
                };

                return {
                    spinRules,
                    isEntangled,
                    triggerEntanglement,
                    resetState
                };
            }
        }).mount('#vortex-app');
    </script>

</body>
</html>
