---
title: "VORTEX v3.0: De Priem-Architectuur & Topologische Dimensies"
date: 2026-07-21
author: "goija"
tags: [VORTEX, Modulo20, DiscreteMathematics, Primes, AudioSynthesis, Topology, JavaScript]
---

# Release: VORTEX v3.0 – De Priem-Architectuur

De nieuwste iteratie van de **Vigesimale Harmonische Matrix** is zojuist gepusht naar de repository. In VORTEX v3.0 stappen we voorbij louter lineaire iteraties. We maken de onderliggende priemgetal-architectuur direct visueel, conceptueel én akoestisch tastbaar op de digitale abacus. 

Binnen dit systeem fungeren priemgetallen niet als abstracte kwantiteiten, maar als de ondeelbare "atomen" van de werkelijkheid. In v3.0 zijn deze ruimtelijke dimensies en cryptografische ankers hardcoded in de engine.

---

## 1. De Wiskundige Abstractie: "Smooth Numbers" & De Tesseract

In topologische modellen coderen priemgetallen kwalitatieve dimensies. Binnen het "Smooth numbers" systeem representeert elke nieuwe priemfactor een nieuwe ruimtelijke of cognitieve dimensie in het proces van *selfing-and-othering*. We hebben dit abstracte gegeven vertaald naar drie hoofdassen:

* **Factor 2 (Rode as):** Binaire splitsing en analyse (Yang).
* **Factor 3 (Groene as):** Triadische synthese en bemiddeling (Yin).
* **Factor 5 (Blauwe as):** De kwintessens; wat het Zelf in essentie tot dit specifieke Zelf maakt.

Door deze machten wiskundig te combineren in de vormule $2^N \times 3^M \times 5^P$, worden complexe transities geprojecteerd op de hoekpunten van een afgeknotte tesseract. Waar samengestelde getallen de voorspelbare, positieve ruimte ("Figure") vormen, zijn de zuivere priemgetallen de fundamentele, negatieve ruimte ("Ground")—de onwrikbare eigenwaarden die dicteren waar het systeem in balans komt.

---

## 2. De Code Implementatie: Real-time Factorisatie

Om deze wiskunde zonder zware overhead in de browser te draaien, fungeert de JavaScript-kern van de VORTEX als een iteratieve microprocessor. In plaats van vooraf berekende databases te laden, parseert het algoritme elke node real-time zodra u de slider beweegt.

Hier is de kernlogica die de ruimtelijke assen extraheert:

```javascript
function berekenPriemDimensies(getal) {
    let n = getal;
    let factor2 = 0, factor3 = 0, factor5 = 0;

    if (n < 1) return { factor2, factor3, factor5, isSmooth: false };

    // Iteratieve extractie van de fundamentele bouwstenen
    while (n % 2 === 0 && n > 0) { factor2++; n /= 2; }
    while (n % 3 === 0 && n > 0) { factor3++; n /= 3; }
    while (n % 5 === 0 && n > 0) { factor5++; n /= 5; }

    return { 
        f2: factor2, 
        f3: factor3, 
        f5: factor5,
        // Een zuiver 'Smooth Number' heeft geen restwaarde groter dan 1
        isSmooth: (n === 1 && getal > 1) 
    };
}
