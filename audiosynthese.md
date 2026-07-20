<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VORTEX: Modulo 20 Akoestische Matrix</title>
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            color: #58a6ff;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .container {
            display: flex;
            gap: 40px;
            margin-top: 20px;
        }
        .panel {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 20px;
            width: 350px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        canvas {
            background-color: #000;
            border: 1px solid #58a6ff;
            border-radius: 4px;
        }
        .data-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            border-bottom: 1px solid #30363d;
            padding-bottom: 5px;
        }
        .highlight {
            color: #7ee787;
            font-weight: bold;
        }
        .prime-highlight {
            color: #ff7b72;
            font-weight: bold;
        }
        input[type=range] {
            width: 100%;
            margin: 20px 0;
        }
        button {
            background-color: #238636;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
            font-family: inherit;
            width: 100%;
            margin-bottom: 20px;
        }
        button:hover {
            background-color: #2ea043;
        }
        button:disabled {
            background-color: #30363d;
            cursor: not-allowed;
        }
    </style>
</head>
<body>

    <h1>Vigesimale Z-As Generator (Base-20)</h1>
    
    <div class="container">
        <!-- Visualisatie Paneel -->
        <div class="panel">
            <canvas id="matrixCanvas" width="350" height="400"></canvas>
            <input type="range" id="nodeSlider" min="0" max="100" value="0">
        </div>

        <!-- Data & Audio Paneel -->
        <div class="panel">
            <button id="audioBtn">Initialiseer Audio Engine</button>
            
            <div class="data-row">
                <span>Input Node:</span>
                <span id="outNode">0</span>
            </div>
            <div class="data-row">
                <span>Z-As (Mod 20):</span>
                <span id="outMod">0</span>
            </div>
            <div class="data-row">
                <span>Dimensionele Laag:</span>
                <span id="outLayer">0</span>
            </div>
            <div class="data-row">
                <span>Frequentie (Hz):</span>
                <span id="outFreq">0.00</span>
            </div>
            <div class="data-row">
                <span>Akoestisch Profiel:</span>
                <span id="outProfile">-</span>
            </div>
        </div>
    </div>

    <script>
        // Systeem Constanten
        const BASE_FREQ = 110.0; // Archeoakoestische basis
        const RATIO_11_LIMIT = 11 / 8; // Neutrale kwart (1.375)
        const TWIN_PRIME_MODULATOR = 1.0071; // Verrijking voor primes

        // DOM Elementen
        const canvas = document.getElementById('matrixCanvas');
        const ctx = canvas.getContext('2d');
        const slider = document.getElementById('nodeSlider');
        const btnAudio = document.getElementById('audioBtn');
        
        // Output velden
        const outNode = document.getElementById('outNode');
        const outMod = document.getElementById('outMod');
        const outLayer = document.getElementById('outLayer');
        const outFreq = document.getElementById('outFreq');
        const outProfile = document.getElementById('outProfile');

        // Audio Context variabelen
        let audioCtx;
        let oscillator;
        let gainNode;
        let isAudioActive = false;

        // Priemgetal checker
        function isPrime(num) {
            if (num <= 1) return false;
            if (num <= 3) return true;
            if (num % 2 === 0 || num % 3 === 0) return false;
            for (let i = 5; i * i <= num; i += 6) {
                if (num % i === 0 || num % (i + 2) === 0) return false;
            }
            return true;
        }

        // Start Web Audio API (vereist gebruikersinteractie)
        btnAudio.addEventListener('click', () => {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                oscillator = audioCtx.createOscillator();
                gainNode = audioCtx.createGain();
                
                oscillator.type = 'sine'; // Zuivere golf voor reine stemming
                oscillator.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                
                gainNode.gain.value = 0.1; // Voorkom clipping
                oscillator.start();
                isAudioActive = true;
                
                btnAudio.textContent = "Audio Engine Actief";
                btnAudio.disabled = true;
                
                updateSystem(parseInt(slider.value));
            }
        });

        // Visuele rendering van de modulaire matrix
        function drawMatrix(nodeValue, modValue, layer) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            const centerX = canvas.width / 2;
            const baseY = canvas.height - 30;
            const rowHeight = 60;
            
            // Teken de abstracte Z-As lijn
            ctx.beginPath();
            ctx.moveTo(centerX, baseY);
            ctx.lineTo(centerX, 20);
            ctx.strokeStyle = "#30363d";
            ctx.lineWidth = 2;
            ctx.stroke();

            // Teken de lagen (volumeblokken van 20)
            for (let l = 0; l <= 4; l++) {
                const y = baseY - (l * rowHeight);
                
                // Teken het referentievlak voor de laag
                ctx.beginPath();
                ctx.ellipse(centerX, y, 120, 20, 0, 0, 2 * Math.PI);
                ctx.strokeStyle = (l <= layer) ? "#1f6feb" : "#21262d";
                ctx.stroke();
                
                if (l === layer) {
                    // Markeer het actieve ankerpunt op de Z-as
                    ctx.beginPath();
                    // Verschuif de node horizontaal op basis van de modulo
                    const xOffset = (modValue - 10) * 8; 
                    ctx.arc(centerX + xOffset, y, 8, 0, 2 * Math.PI);
                    
                    if (modValue === 11) {
                        ctx.fillStyle = isPrime(nodeValue) ? "#ff7b72" : "#7ee787";
                        ctx.shadowBlur = 15;
                        ctx.shadowColor = ctx.fillStyle;
                    } else {
                        ctx.fillStyle = "#58a6ff";
                        ctx.shadowBlur = 0;
                    }
                    
                    ctx.fill();
                    ctx.shadowBlur = 0; // Reset
                }
            }
        }

        // Hoofd logica update
        function updateSystem(val) {
            const mod20 = val % 20;
            const layer = Math.floor(val / 20);
            const isPrimeNode = isPrime(val);
            
            let freq = BASE_FREQ;
            let profile = "Standaard Ruimtelijk";
            let cssClass = "";

            // Pas 11-limiet toe als we op de Z-as = 11 resoneren
            if (mod20 === 11) {
                freq = BASE_FREQ * RATIO_11_LIMIT;
                profile = "11-Limiet (Neutrale Kwart)";
                cssClass = "highlight";
            }

            // Schaaltransformatie: moduleer per laag
            const layerModulation = 1 + (layer * 0.05);
            freq *= layerModulation;

            // Priemgetal verrijking (specifiek voor 71 / twin primes)
            if (isPrimeNode && mod20 === 11) {
                freq *= TWIN_PRIME_MODULATOR;
                profile = "Prime Verrijkt (Twin Prime Phase)";
                cssClass = "prime-highlight";
            }

            // UI Updates
            outNode.textContent = val;
            outMod.textContent = mod20;
            outLayer.textContent = layer;
            outFreq.textContent = freq.toFixed(2);
            outProfile.textContent = profile;
            
            outMod.className = cssClass;
            outProfile.className = cssClass;

            // Audio update
            if (isAudioActive) {
                // Glijdende frequentie overgang voor akoestische continuïteit
                oscillator.frequency.setTargetAtTime(freq, audioCtx.currentTime, 0.1);
            }

            // Visuele update
            drawMatrix(val, mod20, layer);
        }

        // Event listener voor slider
        slider.addEventListener('input', (e) => {
            updateSystem(parseInt(e.target.value));
        });

        // Initiële render
        drawMatrix(0, 0, 0);
    </script>
</body>
</html>
