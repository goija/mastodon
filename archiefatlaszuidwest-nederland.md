<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historisch & Genealogisch Zoekportaal Zuidwest-Nederland</title>
    <style>
        :root {
            --bg-dark: #0f172a;
            --panel-bg: #1e293b;
            --card-bg: #334155;
            --accent-blue: #38bdf8;
            --accent-hover: #0284c7;
            --accent-gold: #f59e0b;
            --accent-green: #10b981;
            --accent-red: #ef4444;
            --accent-purple: #a855f7;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #475569;
            --player-bg: #0b1120;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-main);
            line-height: 1.6;
            padding-bottom: 5.5rem; /* Ruimte voor vaste webplayer */
        }

        /* Header */
        header {
            background: linear-gradient(135deg, #0b1120 0%, #1e293b 100%);
            border-bottom: 2px solid var(--border-color);
            padding: 2.5rem 1rem;
            text-align: center;
            position: relative;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }

        header h1 {
            font-size: 2.4rem;
            font-weight: 800;
            color: #fff;
            letter-spacing: -0.5px;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }

        header h1 span {
            color: var(--accent-blue);
        }

        header p {
            color: var(--text-muted);
            font-size: 1.05rem;
            max-width: 850px;
            margin: 0 auto;
        }

        /* Hoofdlayout */
        .container {
            max-width: 1300px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: grid;
            grid-template-columns: 340px 1fr;
            gap: 2rem;
        }

        @media (max-width: 900px) {
            .container {
                grid-template-columns: 1fr;
            }
        }

        /* Zijbalk met Zoekmachine en Filters */
        .search-sidebar {
            background: var(--panel-bg);
            padding: 1.8rem;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            align-self: start;
            position: sticky;
            top: 1.5rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        .search-sidebar h2 {
            font-size: 1.25rem;
            color: #fff;
            margin-bottom: 1.2rem;
            padding-bottom: 0.8rem;
            border-bottom: 2px solid var(--border-color);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .filter-group {
            margin-bottom: 1.3rem;
        }

        .filter-group label {
            display: block;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-muted);
            margin-bottom: 0.4rem;
        }

        .filter-group input[type="text"], 
        .filter-group select {
            width: 100%;
            padding: 0.75rem 1rem;
            background: var(--bg-dark);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-main);
            font-size: 0.95rem;
            transition: border-color 0.2s, box-shadow 0.2s;
        }

        .filter-group input[type="text"]:focus, 
        .filter-group select:focus {
            outline: none;
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
        }

        .reset-btn {
            width: 100%;
            padding: 0.7rem;
            background: var(--card-bg);
            color: var(--text-main);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
            margin-top: 0.5rem;
        }

        .reset-btn:hover {
            background: var(--border-color);
        }

        .stats-box {
            margin-top: 1.5rem;
            padding-top: 1.2rem;
            border-top: 1px dashed var(--border-color);
            font-size: 0.85rem;
            color: var(--text-muted);
            line-height: 1.5;
        }

        .stats-box strong {
            color: var(--accent-gold);
            font-size: 1.1rem;
        }

        /* Resultaten Paneel */
        .results-panel {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        /* Tabbladen in Resultatenpaneel */
        .view-tabs {
            display: flex;
            gap: 0.5rem;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 0.5rem;
            flex-wrap: wrap;
        }

        .view-tab-btn {
            background: var(--panel-bg);
            color: var(--text-muted);
            border: 1px solid var(--border-color);
            padding: 0.6rem 1.2rem;
            border-radius: 6px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.2s;
        }

        .view-tab-btn:hover {
            color: #fff;
            border-color: var(--accent-blue);
        }

        .view-tab-btn.active {
            background: var(--accent-blue);
            color: #000;
            border-color: var(--accent-blue);
        }

        /* Cards Raster */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 1.5rem;
        }

        .record-card {
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
            position: relative;
            overflow: hidden;
        }

        .record-card:hover {
            transform: translateY(-4px);
            border-color: var(--accent-blue);
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 0.8rem;
            gap: 0.5rem;
        }

        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #fff;
            line-height: 1.3;
        }

        .badge {
            font-size: 0.68rem;
            font-weight: 800;
            text-transform: uppercase;
            padding: 0.25rem 0.6rem;
            border-radius: 999px;
            white-space: nowrap;
            color: #fff;
        }

        .badge-archief { background: var(--accent-blue); color: #000; }
        .badge-persoon { background: var(--accent-gold); color: #000; }
        .badge-polder { background: var(--accent-green); color: #000; }
        .badge-thema { background: var(--accent-purple); color: #fff; }

        .card-meta {
            font-size: 0.85rem;
            color: var(--accent-blue);
            font-weight: 600;
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        .card-desc {
            font-size: 0.92rem;
            color: var(--text-muted);
            margin-bottom: 1.2rem;
            flex-grow: 1;
        }

        .entity-box {
            background: var(--bg-dark);
            padding: 0.8rem;
            border-radius: 8px;
            font-size: 0.82rem;
            color: #cbd5e1;
            margin-bottom: 1.2rem;
            border-left: 3px solid var(--accent-gold);
        }

        .entity-box strong {
            color: var(--accent-gold);
            display: block;
            margin-bottom: 0.2rem;
        }

        .card-actions {
            display: flex;
            gap: 0.6rem;
            flex-wrap: wrap;
        }

        .btn {
            flex: 1;
            min-width: 130px;
            padding: 0.65rem 1rem;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.4rem;
            border: none;
        }

        .btn-primary {
            background: var(--accent-blue);
            color: #000;
        }

        .btn-primary:hover {
            background: var(--accent-hover);
            color: #fff;
        }

        .btn-secondary {
            background: var(--card-bg);
            color: #fff;
            border: 1px solid var(--border-color);
        }

        .btn-secondary:hover {
            border-color: var(--text-muted);
            background: var(--border-color);
        }

        /* Highlight van zoektermen */
        .highlight {
            background-color: rgba(245, 158, 11, 0.35);
            color: #fff;
            font-weight: bold;
            padding: 0 2px;
            border-radius: 2px;
        }

        /* Archief API & Leges Simulator Sectie */
        .api-section {
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 2rem;
            display: none;
        }

        .api-section.active {
            display: block;
            animation: fadeIn 0.3s ease;
        }

        .api-form {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        @media (max-width: 768px) {
            .api-form { grid-template-columns: 1fr; }
        }

        .leges-warning {
            grid-column: 1 / -1;
            padding: 1.2rem;
            border-radius: 8px;
            font-size: 0.9rem;
            line-height: 1.5;
            display: none;
        }

        .leges-warning.success {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid var(--accent-green);
            color: #34d399;
            display: block;
        }

        .leges-warning.blocked {
            background: rgba(239, 68, 68, 0.15);
            border: 1px solid var(--accent-red);
            color: #f87171;
            display: block;
        }

        /* Vaste Webplayer onderin */
        .webplayer-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--player-bg);
            border-top: 2px solid var(--accent-blue);
            padding: 0.8rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            box-shadow: 0 -5px 25px rgba(0,0,0,0.8);
            z-index: 1000;
        }

        @media (max-width: 768px) {
            .webplayer-bar {
                flex-direction: column;
                padding: 1rem;
                gap: 0.8rem;
                text-align: center;
            }
        }

        .player-info {
            display: flex;
            align-items: center;
            gap: 1rem;
            min-width: 280px;
        }

        .visualizer {
            display: flex;
            align-items: flex-end;
            gap: 3px;
            height: 24px;
            width: 32px;
        }

        .vis-bar {
            width: 4px;
            background: var(--accent-blue);
            border-radius: 2px 2px 0 0;
            height: 4px;
            transition: height 0.1s ease;
        }

        .playing .vis-bar:nth-child(1) { animation: bounce 0.6s infinite alternate; }
        .playing .vis-bar:nth-child(2) { animation: bounce 0.4s infinite alternate 0.1s; }
        .playing .vis-bar:nth-child(3) { animation: bounce 0.7s infinite alternate 0.2s; }
        .playing .vis-bar:nth-child(4) { animation: bounce 0.5s infinite alternate 0.15s; }
        .playing .vis-bar:nth-child(5) { animation: bounce 0.65s infinite alternate 0.05s; }

        @keyframes bounce {
            0% { height: 4px; }
            100% { height: 24px; background: var(--accent-gold); }
        }

        .player-text h4 {
            font-size: 0.95rem;
            color: #fff;
            margin-bottom: 0.1rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 320px;
        }

        .player-text p {
            font-size: 0.75rem;
            color: var(--text-muted);
        }

        .player-controls {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .ctrl-btn {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            color: #fff;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1.1rem;
            transition: transform 0.1s, background 0.2s;
        }

        .ctrl-btn:hover {
            background: var(--accent-blue);
            color: #000;
            transform: scale(1.08);
        }

        .ctrl-btn-primary {
            background: var(--accent-blue);
            color: #000;
            width: 46px;
            height: 46px;
            font-size: 1.3rem;
        }

        .player-volume {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .player-volume input[type="range"] {
            width: 100px;
            accent-color: var(--accent-blue);
            cursor: pointer;
        }
    </style>
</head>
<body>

<header>
    <h1>ArchiefAtlas <span>Zuidwest-Nederland</span></h1>
    <p>Geïntegreerd Zoekportaal voor Genealogie, Streekgeschiedenis, Kadaster (OAT 1832) en Oude Zakelijke Rechten in Zeeland, Tholen, West-Brabant en Bergen op Zoom.</p>
</header>

<div class="container">
    <aside class="search-sidebar">
        <h2>🔍 Zoeken & Filteren</h2>
        
        <div class="filter-group">
            <label for="search-input">Vrij Zoeken (Trefwoord, Naam, Perceel)</label>
            <input type="text" id="search-input" placeholder="Bijv. Bout, Loncke, RAZE 5183, Weervisserij..." oninput="executeSearch()">
        </div>

        <div class="filter-group">
            <label for="category-select">Categorie / Bron</label>
            <select id="category-select" onchange="executeSearch()">
                <option value="alle">Alle Categorieën (Dossiers)</option>
                <option value="archief">Archiefstukken & Inventarissen</option>
                <option value="persoon">Genealogische Knooppunten & Adel</option>
                <option value="polder">Polders, Kadaster & Eigendom</option>
                <option value="thema">Historische Thema's & Ambachten</option>
            </select>
        </div>

        <div class="filter-group">
            <label for="region-select">Geografische Regio</label>
            <select id="region-select" onchange="executeSearch()">
                <option value="alle">Heel Zuidwest-Nederland</option>
                <option value="Tholen">Eiland Tholen & St. Philipsland</option>
                <option value="Zeeland">Overig Zeeland (Bevelanden, Walcheren)</option>
                <option value="West-Brabant">West-Brabant & Bergen op Zoom</option>
            </select>
        </div>

        <div class="filter-group">
            <label for="period-select">Tijdvak / Eeuw</label>
            <select id="period-select" onchange="executeSearch()">
                <option value="alle">Alle Eeuwen</option>
                <option value="15e-16e">15e & 16e Eeuw (Middeleeuwen / Opstand)</option>
                <option value="17e-18e">17e & 18e Eeuw (Republiek / Gouden Eeuw)</option>
                <option value="19e-20e">19e & 20e Eeuw (Kadaster / Wederopbouw)</option>
            </select>
        </div>

        <button class="reset-btn" onclick="resetFilters()">↺ Wis Alle Filters</button>

        <div class="stats-box">
            Aantal resultaten:<br>
            <strong id="stat-count">0</strong> dossiers en knooppunten geladen.
        </div>
    </aside>

    <main class="results-panel">
        <div class="view-tabs">
            <button class="view-tab-btn active" onclick="switchView('grid')">📋 Dossier Raster</button>
            <button class="view-tab-btn" onclick="switchView('api')">⚙️ Archief API & Leges Simulator</button>
            <button class="view-tab-btn" onclick="switchView('kringen')">🏛️ Contactcenter Historische Kringen</button>
        </div>

        <div id="view-grid" class="cards-grid">
            </div>

        <div id="view-api" class="api-section">
            <h2 style="color: #fff; margin-bottom: 0.5rem;">Archief API & Leges-clausule Toetsing</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem;">
                Simuleer hier een live bevraging bij de depots van het Zeeuws Archief, West-Brabants Archief, Nationaal Archief of Gemeentearchief Tholen. Het systeem verifieert automatisch of de aanvraag valt onder kosteloze Open Data / CC0-scans of dat de wettelijke gemeentelijke legesclausule van kracht is.
            </p>

            <div class="api-form">
                <div class="filter-group">
                    <label>Archiefinstelling & Depot</label>
                    <select id="api-archive">
                        <option value="ZA">Zeeuws Archief (Middelburg) — RAZE & Rekenkamer B</option>
                        <option value="WBA">West-Brabants Archief (Bergen op Zoom) — Schepenbanken</option>
                        <option value="GAT">Gemeentearchief Tholen — DTB, BS & Weeskamer</option>
                        <option value="NA">Nationaal Archief (Den Haag) — Nassause Domeinraad (1.08.11)</option>
                    </select>
                </div>

                <div class="filter-group">
                    <label>Inventaris- of Kadasternummer</label>
                    <input type="text" id="api-inv" placeholder="Bijv. RAZE 5183, fol. 253 of OAT 1832 Scherpenisse B nr. 281">
                </div>

                <div class="filter-group" style="grid-column: 1 / -1;">
                    <label>Type Aanvraag & Autorisatiemodus</label>
                    <select id="api-mode">
                        <option value="opendata">Digitale CC0 Scan / Open Data Harvesting (OAI-PMH) — Volledig Gratis</option>
                        <option value="afschrift">Gecertificeerd Afschrift (Burgerlijke Stand / Notarieel) — Legesplichtig</option>
                        <option value="fysiek">Fysiek Archiefonderzoek door Studiezaalmedewerker — Leges & Uurtarief</option>
                    </select>
                </div>

                <button class="btn btn-primary" style="grid-column: 1 / -1; padding: 0.9rem; font-size: 1rem;" onclick="simulateApiCall()">
                    ⚡ VERSTUUR AANVRAAG NAAR ARCHIEFSYSTEEM
                </button>

                <div id="api-output" class="leges-warning"></div>
            </div>
        </div>

        <div id="view-kringen" class="api-section">
            <h2 style="color: #fff; margin-bottom: 0.5rem;">Regionaal Contactcenter Historische Kringen</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
                Directe doorverwijzing naar streekontsluiters en expertisecentra voor lokale ondersteuning bij stamboomonderzoek, paleografie en poldergeschiedenis.
            </p>

            <div class="cards-grid">
                <div class="record-card">
                    <div>
                        <div class="card-header">
                            <h3 class="card-title">Heemkundekring Stad en Lande van Tholen</h3>
                            <span class="badge badge-archief">Tholen</span>
                        </div>
                        <p class="card-desc">Gevestigd in het Oude Stadhuis te Tholen. Gespecialiseerd in de agrarische en bestuurlijke historie van het eiland Tholen, weeskamerakten en genealogie (o.a. families Bout, Schot, Quaak).</p>
                        <div class="entity-box"><strong>Bezoekadres:</strong> Hoogstraat 12, Tholen<br><strong>Collectie:</strong> Bibliotheek, fotobeeldbank, Cronicke van Tholen.</div>
                    </div>
                    <a href="https://www.archieftholen.nl" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">Bezoek Website ↗</a>
                </div>

                <div class="record-card">
                    <div>
                        <div class="card-header">
                            <h3 class="card-title">Geschiedkundige Kring De Ghulden Roos</h3>
                            <span class="badge badge-persoon">West-Brabant</span>
                        </div>
                        <p class="card-desc">Gevestigd in het Markiezenhof te Bergen op Zoom. Experts in de Markiezen van Bergen op Zoom, scheepvaart langs de Roosendaalse Vliet, turfwinning en maritieme zeehelden (familie Loncke).</p>
                        <div class="entity-box"><strong>Bezoekadres:</strong> Steenbergsestraat 6, Bergen op Zoom<br><strong>Collectie:</strong> Jaarboeken De Ghulden Roos, scheepvaartdossiers.</div>
                    </div>
                    <a href="https://www.westbrabantsarchief.nl" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">Bezoek Archiefportaal ↗</a>
                </div>

                <div class="record-card">
                    <div>
                        <div class="card-header">
                            <h3 class="card-title">Stichting Behoud Weervisserij</h3>
                            <span class="badge badge-thema">Oosterschelde</span>
                        </div>
                        <p class="card-desc">Behartigt het immaterieel cultureel erfgoed van de traditionele ansjovisvangst op de zandplaten van de Oosterschelde (Kraaijer-platen). Beheert historische pachtcontracten vanaf 1882.</p>
                        <div class="entity-box"><strong>Expertise:</strong> Visrechten, getijdenwerking, spieringen en weren.<br><strong>Erfgoedstatus:</strong> Nationale Inventaris Immaterieel Erfgoed.</div>
                    </div>
                    <a href="https://www.immaterieelerfgoed.nl/nl/weervisserij" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">Bekijk Erfgoedportaal ↗</a>
                </div>

                <div class="record-card">
                    <div>
                        <div class="card-header">
                            <h3 class="card-title">Heemkundekring Philippuslandt</h3>
                            <span class="badge badge-polder">St. Philipsland</span>
                        </div>
                        <p class="card-desc">Richt zich op de bedijking en poldergeschiedenis van Sint Philipsland, de Watersnoodramp van 1953 en agrarische stamboomreconstructies van Noord-Zeeuwse geslachten.</p>
                        <div class="entity-box"><strong>Bezoekadres:</strong> Dorpshuis De Wimpel, Sint Philipsland<br><strong>Publicatie:</strong> Cronicke van den lande van Philippuslandt.</div>
                    </div>
                    <a href="https://www.philippuslandt.nl" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">Bezoek Heemkring ↗</a>
                </div>
            </div>
        </div>
    </main>
</div>

<div class="webplayer-bar">
    <div class="player-info">
        <div class="visualizer" id="visualizer">
            <div class="vis-bar"></div>
            <div class="vis-bar"></div>
            <div class="vis-bar"></div>
            <div class="vis-bar"></div>
            <div class="vis-bar"></div>
        </div>
        <div class="player-text">
            <h4 id="player-title">Geen archiefcast geselecteerd</h4>
            <p id="player-sub">Selecteer een dossier of lezing om de audioreconstructie af te spelen</p>
        </div>
    </div>

    <div class="player-controls">
        <button class="ctrl-btn ctrl-btn-primary" id="play-pause-btn" onclick="togglePlay()" title="Afspelen/Pauzeren">▶</button>
        <button class="ctrl-btn" onclick="stopPlayer()" title="Stop">■</button>
    </div>

    <div class="player-volume">
        <span style="font-size: 1.1rem;">🔊</span>
        <input type="range" id="volume-slider" min="0" max="1" step="0.05" value="0.8" onchange="updateVolume(this.value)">
    </div>
</div>

<audio id="html5-audio" crossorigin="anonymous"></audio>

<script>
    // 1. DATABASE MET HISTORISCHE, GENEALOGISCHE & KADASTRALE DOSSIERS
    const database = [
        {
            id: "RAZE-5183",
            title: "Transportakte Herberg 'Het Wapen van Dort'",
            category: "archief",
            region: "Tholen",
            period: "17e-18e",
            meta: "RAZE inv.nr. 5183, fol. 253 (Tholen, 1699–1717)",
            desc: "Verkoopakte van een huis en erf aan de Kaaij te Tholen door de erfgenamen van Willem Jacobsen Moeijelijcker aan schipper Bastiaen Dirckse Bout. Betreft herberg 'Het Wapen van Dort', het logistieke knooppunt voor Zeeuwse beurtschippers en graanhandelaren.",
            entities: "Bastiaen Dirckse Bout, Willem Jacobsen Moeijelijcker, familie Moeliker, De Kaaij.",
            url: "https://archieftholen.nl",
            audioTitle: "Archiefcast: Herbergen & Schippersgilden aan de Thoolse Kaaij",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "OAT-1832-SPN",
            title: "Kadastrale Legger Scherpenisse Sectie B",
            category: "polder",
            region: "Tholen",
            period: "19e-20e",
            meta: "OAT 1832, Scherpenisse, Sectie B, nr. 281-282",
            desc: "Oorspronkelijk Aanwijzende Tafel (OAT) van de gemeente Scherpenisse. Registratie van weiland en bouwland in eigendom van J.C. Dorst & Mede Landbouwers, direct aangrenzend aan de landerijen van Christiaan Kleppe en Krijn van der Werf.",
            entities: "J.C. Dorst, Christiaan Kleppe, Krijn van der Werf, familie Bolier, Sectie B.",
            url: "https://kadastralekaart.com",
            audioTitle: "Lezing: De invoering van het Kadaster in Zeeland (1832)",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "GEN-ROOSEVELT",
            title: "Regentengeslacht Van 't Rosevelt",
            category: "persoon",
            region: "Tholen",
            period: "17e-18e",
            meta: "Oud-Vossemeer & Tholen (16e – 18e eeuw)",
            desc: "Invloedrijke familie van Thoolse regenten, schepenen, leenmannen en schoolmeesters in Oud-Vossemeer. Josina van 't Rosevelt huwde met schipper Krijn Marinisse Kamhooft. Vormt de Zeeuwse wieg (cradle) van de Amerikaanse presidentiële dynastie Roosevelt.",
            entities: "Josina van 't Rosevelt, Johannes Jorissen van 't Rosevelt, Pieter Jorisz, Krijn Kamhooft.",
            url: "https://www.oudvossemeer.com",
            audioTitle: "Podcast: De Zeeuwse wortels van de presidenten Roosevelt",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "THEMA-WEERVISSERIJ",
            title: "Oude Zakelijke Visrechten & Weervisserij",
            category: "thema",
            region: "West-Brabant",
            period: "19e-20e",
            meta: "BVZS inv.nr. 779/780 & Kraaijer-platen (1825–1914)",
            desc: "Eeuwenoude visserijtechniek op ansjovis in de Oosterschelde ter hoogte van Bergen op Zoom via houten weren. Bij de Visserijwetten trachtte de Staat deze gilde-rechten om te zetten in pachtcontracten. De leggers van 1882 vormen het harde juridische bewijs van watervaste visrechten.",
            entities: "Familie Schot, familie Bout, Bestuur der Visserijen Zeeuwse Stromen (BVZS), Kraaijer.",
            url: "https://www.immaterieelerfgoed.nl/nl/weervisserij",
            audioTitle: "Reportage: Weervissers op de Oosterschelde bij laagwater",
            audioUrl: "https://stream.omroepbrabant.nl/radio"
        },
        {
            id: "RAZE-5588",
            title: "Weeskamerprotocol Oud-Vossemeer",
            category: "archief",
            region: "Tholen",
            period: "17e-18e",
            meta: "RAZE inv.nr. 5588 (Oud-Vossemeer, 1689–1707)",
            desc: "Gedigitaliseerd register van weesakten, voogdijstellingen en boedelscheidingen van de Ambachtsheerlijkheid Oud-Vossemeer. Cruciale bron voor erfrechtelijke reconstructies na het overlijden van lokale landbouwers en polderpachters.",
            entities: "Notaris Pieter van Levendale, Jan Jansen van Couwerve, weesmeesters Oud-Vossemeer.",
            url: "https://www.openarch.nl",
            audioTitle: "Archiefcast: Weeskamers en erfrecht in de Thoolse polders",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "GEN-LONCKE",
            title: "Maritieme Dynastie Loncke & Zeehelden",
            category: "persoon",
            region: "West-Brabant",
            period: "15e-16e",
            meta: "Roosendaal, Tholen & Zierikzee (1421–1634)",
            desc: "Geslacht met een opmerkelijke dualiteit: enerzijds lokaal verankerde schepenen en grondbezitters rond de Roosendaalse Vliet (Lambrecht Pieters Loncke), anderzijds de maritieme tak die VOC-zeeheld admiraal Hendrik Corneliszoon Lonck voortbracht.",
            entities: "Lambrecht Pieters Loncke, Pieter Lambrechtse Lonke, Admiraal Hendrik Lonck, Roosendaal.",
            url: "https://www.westbrabantsarchief.nl",
            audioTitle: "Audiotour: Admiraal Lonck en de verovering van de Zilvervloot",
            audioUrl: "https://stream.omroepbrabant.nl/radio"
        },
        {
            id: "THEMA-OPROER1702",
            title: "De Thoolse Oproer van 1702",
            category: "thema",
            region: "Tholen",
            period: "17e-18e",
            meta: "Stadsregering Tholen / Tweede Stadhouderloze Tijdperk",
            desc: "Felle burgeropstand na het overlijden van stadhouder Willem III. De lokale ambachtsgilden (schippers en timmerlieden) kwamen in verzet tegen de regentenkliek en eisten democratische controle op de stadsfinanciën en vrije verkiezing van schepenen.",
            entities: "Jacob Wouters, Jan Snoeck, gildebroeders Tholen, Gecommitteerde Raden.",
            url: "https://kzgw.nl",
            audioTitle: "Historisch Debat: Democratisch verzet in Tholen anno 1702",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "POLDER-1500GEMETEN",
            title: "De 1500 Gemetenpolder & Meekrapstoven",
            category: "polder",
            region: "Tholen",
            period: "17e-18e",
            meta: "Scherpenisse & Stavenisse (1624–1810)",
            desc: "Cruciaal agrarisch poelgebied tussen Scherpenisse en Stavenisse. De kohieren van de 100e penning documenteren de pachters van landbouwgronden en de opkomst van de meekrapindustrie (meestoven 'De Eendracht' en 'Molenberg').",
            entities: "Familie Bout broers, Simon Cornelisse Camhoot, Meestoof De Eendracht, Molenvliet.",
            url: "https://www.zeeuwseankers.nl",
            audioTitle: "Reportage: Het bruine goud – Meekrapstoven in Zeeland",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "NDR-13854",
            title: "Nassause Domeinrekening Sint-Maartensdijk",
            category: "archief",
            region: "Tholen",
            period: "15e-16e",
            meta: "NDR 1.08.11, inv.nr. 13854 (Den Haag, 1575)",
            desc: "Financiële verantwoording van het beheer van de Nassause domeinen door de rentmeester van de Oranjes te Sint-Maartensdijk en Scherpenisse. Bevat lijsten van pachtsommen, tiendheffingen en agrarische opbrengsten.",
            entities: "Prins van Oranje, rentmeester Sint-Maartensdijk, Marcus Faasse, Nassause Domeinraad.",
            url: "https://www.nationaalarchief.nl",
            audioTitle: "College: Het rentmeesterschap van de Oranjes in Zeeland",
            audioUrl: "https://stream.rijksoverheid.nl/audio/persconferentie_schoof.mp3"
        },
        {
            id: "GEN-STEENGRACHT",
            title: "Regentengeslacht Steengracht & Pous",
            category: "persoon",
            region: "Zeeland",
            period: "17e-18e",
            meta: "Middelburg, Zierikzee & Veere (15e – 19e eeuw)",
            desc: "Prominente Zeeuwse regentenfamilie met zware bestuursfuncties in de Admiraliteit en Staten-Generaal. Allianties met de geslachten Pous, Loncque, Verheije en Cau. Mr. Bonifacius Pous stelde belangrijke vroege genealogische manuscripten samen.",
            entities: "Bonifacius Pieterszoon Pous, Johan Steengracht, Nicolaas Steengracht van Oostcapelle.",
            url: "https://www.zeeuwsarchief.nl",
            audioTitle: "Podcast: Zeeuwse regenten en hun buitenplaatsen",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "POLDER-REIMERSWAAL",
            title: "Verdronken Stad & Land van Reimerswaal",
            category: "polder",
            region: "Zeeland",
            period: "15e-16e",
            meta: "Oosterschelde & Zuid-Beveland (1374–1632)",
            desc: "Ooit een bloeiende handelsstad aan de Oosterschelde met eigen stadsrechten en schepenbank. Na zware stormvloeden (Sint-Felixvloed 1530) verdronk het omliggende land. De archieven werden in 1635 gered en overgebracht naar de Rekenkamer van Zeeland.",
            entities: "Adriaen Jans Camhoot (schepen/burgemeester), Nicolaas Kervin van Reimerswaal, Bergse Diepsluis.",
            url: "https://www.zeeuwseankers.nl",
            audioTitle: "Reportage: Archeologie van de verdronken stad Reimerswaal",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        },
        {
            id: "GEN-DEGRAAF",
            title: "Agrarische Elite De Graaf & Rijstenbil",
            category: "persoon",
            region: "Tholen",
            period: "19e-20e",
            meta: "Scherpenisse, Stavenisse & Oud-Vossemeer",
            desc: "Sterk verweven geslachten binnen de Thoolse boerenstand en polderbesturen. Meervoudige huwelijksbanden in de 19e eeuw (o.a. 1837 en 1845) consolideerden grootgrondbezit in de Oudelandpolder en rond Scherpenisse.",
            entities: "Jan Bartelsz de Graeff, Berbera de Graaf, Jan Rijssebil, familie Bolier, Hendrik Quaak.",
            url: "https://www.wiewaswie.nl",
            audioTitle: "Lezing: Grondbezit en boerenelite op Tholen in de 19e eeuw",
            audioUrl: "https://icecast.omroepzeeland.nl/radio"
        }
    ];

    // 2. STATE & ZOEKFUNCTIES
    let currentView = 'grid';
    const searchInput = document.getElementById('search-input');
    const categorySelect = document.getElementById('category-select');
    const regionSelect = document.getElementById('region-select');
    const periodSelect = document.getElementById('period-select');
    const gridContainer = document.getElementById('view-grid');
    const statCount = document.getElementById('stat-count');

    function highlightText(text, query) {
        if (!query) return text;
        const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
        return text.replace(regex, '<span class="highlight">$1</span>');
    }

    function executeSearch() {
        const query = searchInput.value.toLowerCase().trim();
        const cat = categorySelect.value;
        const reg = regionSelect.value;
        const per = periodSelect.value;

        const filtered = database.filter(item => {
            const matchCat = cat === 'alle' || item.category === cat;
            const matchReg = reg === 'alle' || item.region === reg;
            const matchPer = per === 'alle' || item.period === per;
            
            const searchString = `${item.title} ${item.meta} ${item.desc} ${item.entities} ${item.region}`.toLowerCase();
            const matchQuery = !query || searchString.includes(query);

            return matchCat && matchReg && matchPer && matchQuery;
        });

        statCount.textContent = filtered.length;
        renderGrid(filtered, query);
    }

    function renderGrid(data, query = "") {
        gridContainer.innerHTML = '';

        if (data.length === 0) {
            gridContainer.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; background: var(--panel-bg); border-radius: 12px; border: 1px dashed var(--border-color);">
                    <h3 style="color: #fff; margin-bottom: 0.5rem;">Geen dossiers of knooppunten gevonden</h3>
                    <p style="color: var(--text-muted);">Probeer uw zoekterm te verruimen of wis de actieve filtermatrijzen in de zijbalk.</p>
                    <button class="reset-btn" style="max-width: 200px; margin: 1.5rem auto 0 auto;" onclick="resetFilters()">Wis Filters</button>
                </div>
            `;
            return;
        }

        data.forEach(rec => {
            const card = document.createElement('article');
            card.className = 'record-card';
            
            let badgeClass = 'badge-archief';
            if (rec.category === 'persoon') badgeClass = 'badge-persoon';
            if (rec.category === 'polder') badgeClass = 'badge-polder';
            if (rec.category === 'thema') badgeClass = 'badge-thema';

            card.innerHTML = `
                <div>
                    <div class="card-header">
                        <h3 class="card-title">${highlightText(rec.title, query)}</h3>
                        <span class="badge ${badgeClass}">${rec.category}</span>
                    </div>
                    <div class="card-meta">📍 ${highlightText(rec.region, query)} — <span>${highlightText(rec.meta, query)}</span></div>
                    <p class="card-desc">${highlightText(rec.desc, query)}</p>
                    <div class="entity-box">
                        <strong>Gekoppelde Entiteiten / Sleutelpersonen:</strong>
                        ${highlightText(rec.entities, query)}
                    </div>
                </div>
                <div class="card-actions">
                    <button class="btn btn-primary" onclick="playMedia('${rec.title}', '${rec.audioTitle}', '${rec.audioUrl}')">▶ Luister Archiefcast</button>
                    <button class="btn btn-secondary" onclick="prefillApi('${rec.meta}', '${rec.region}')">⚡ Vraag op via API</button>
                </div>
            `;
            gridContainer.appendChild(card);
        });
    }

    function resetFilters() {
        searchInput.value = '';
        categorySelect.value = 'alle';
        regionSelect.value = 'alle';
        periodSelect.value = 'alle';
        executeSearch();
    }

    function switchView(viewId) {
        currentView = viewId;
        document.querySelectorAll('.view-tab-btn').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');

        document.getElementById('view-grid').style.display = viewId === 'grid' ? 'grid' : 'none';
        document.getElementById('view-api').classList.toggle('active', viewId === 'api');
        document.getElementById('view-kringen').classList.toggle('active', viewId === 'kringen');
    }

    // 3. ARCHIEF API & LEGES SIMULATOR
    function prefillApi(metaText, region) {
        switchView('api');
        document.querySelectorAll('.view-tab-btn')[1].classList.add('active');
        document.querySelectorAll('.view-tab-btn')[0].classList.remove('active');

        document.getElementById('api-inv').value = metaText;
        
        if (metaText.includes('1.08.11') || metaText.includes('NDR')) {
            document.getElementById('api-archive').value = 'NA';
        } else if (region === 'West-Brabant') {
            document.getElementById('api-archive').value = 'WBA';
        } else if (metaText.includes('DTB') || metaText.includes('Weeskamer')) {
            document.getElementById('api-archive').value = 'GAT';
        } else {
            document.getElementById('api-archive').value = 'ZA';
        }

        window.scrollTo({ top: 300, behavior: 'smooth' });
    }

    function simulateApiCall() {
        const inv = document.getElementById('api-inv').value.trim();
        const arch = document.getElementById('api-archive').options[document.getElementById('api-archive').selectedIndex].text;
        const mode = document.getElementById('api-mode').value;
        const output = document.getElementById('api-output');

        if (!inv) {
            alert('Vul alstublieft een geldig inventaris- of kadasternummer in.');
            return;
        }

        output.className = 'leges-warning';

        if (mode === 'opendata') {
            output.classList.add('success');
            output.innerHTML = `
                <strong style="font-size: 1.05rem;">✔ [AANVRAAG GOEDGEKEURD — OPEN DATA HARVESTING]</strong><br>
                Het aangevraagde archiefobject (<em>${inv}</em> bij <em>${arch}</em>) is geclassificeerd als publiek domein (CC0-licentie).<br>
                <hr style="border-color: var(--accent-green); margin: 0.6rem 0;">
                <span style="color: #fff;">De digitale METS-referentie en hoge-resolutie JPEG/JP2-scans zijn kosteloos vrijgegeven en direct gekoppeld aan uw studiezaal-sessie. Geen gemeentelijke leges of onderzoeksrechten verschuldigd.</span>
            `;
        } else {
            output.classList.add('blocked');
            output.innerHTML = `
                <strong style="font-size: 1.05rem;">⚠️ [AANVRAAG GEBLOKKEERD — WETTELIJKE LEGES- & KOSTENCLAUSULE ACTIEF]</strong><br>
                De aanvraag voor <em>${inv}</em> betreft een administratieve handeling (gecertificeerd afschrift of fysiek archiefonderzoek door studiezaalmedewerker) waarvoor door <em>${arch}</em> leges of uurtarieven in rekening worden gebracht conform de lokale legesverordening.<br>
                <hr style="border-color: var(--accent-red); margin: 0.6rem 0;">
                <span style="color: #fff;"><strong>Beschermingsregeling Gevolmachtigde:</strong> Conform de strikte volmachtvoorwaarden is automatische verwerking gestopt. U dient vooraf een gespecificeerde prijsopgave/offerte van de archiefdienst te accorderen alvorens deze kosten mogen worden gemaakt.</span>
            `;
        }
    }

    // 4. WEBPLAYER MET EQUALIZER
    const audioEl = document.getElementById('html5-audio');
    const visualizer = document.getElementById('visualizer');
    const playBtn = document.getElementById('play-pause-btn');
    const titleEl = document.getElementById('player-title');
    const subEl = document.getElementById('player-sub');
    let isPlaying = false;

    function playMedia(sourceTitle, audioTitle, url) {
        titleEl.textContent = audioTitle;
        subEl.textContent = `Dossier: ${sourceTitle}`;
        
        audioEl.src = url;
        audioEl.volume = document.getElementById('volume-slider').value;
        
        audioEl.play().then(() => {
            setPlayingState(true);
        }).catch(() => {
            // Fallback simulatiemodus bij browser CORS/autoplay restricties
            console.warn("Directe audioweergave geblokkeerd. Audiosimulatie-modus geactiveerd.");
            setPlayingState(true);
            subEl.textContent += " [Archief-simulatie Actief]";
        });
    }

    function togglePlay() {
        if (titleEl.textContent === "Geen archiefcast geselecteerd") {
            const first = database[0];
            playMedia(first.title, first.audioTitle, first.audioUrl);
            return;
        }

        if (isPlaying) {
            audioEl.pause();
            setPlayingState(false);
        } else {
            audioEl.play().catch(() => {});
            setPlayingState(true);
        }
    }

    function stopPlayer() {
        audioEl.pause();
        audioEl.currentTime = 0;
        audioEl.removeAttribute('src');
        setPlayingState(false);
        titleEl.textContent = "Geen archiefcast geselecteerd";
        subEl.textContent = "Selecteer een dossier of lezing om de audioreconstructie af te spelen";
    }

    function updateVolume(val) {
        audioEl.volume = val;
    }

    function setPlayingState(state) {
        isPlaying = state;
        if (state) {
            visualizer.classList.add('playing');
            playBtn.textContent = "❚❚";
        } else {
            visualizer.classList.remove('playing');
            playBtn.textContent = "▶";
        }
    }

    // Initialisatie bij start
    window.onload = () => {
        executeSearch();
    };
</script>

</body>
</html>
