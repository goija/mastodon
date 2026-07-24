import re
import spacy
from typing import Dict, List, Set
import sys

# 1. SETUP & MODEL LADEN
# Zorg ervoor dat het Nederlandse model is geïnstalleerd:
# !python -m spacy download nl_core_news_sm
try:
    nlp = spacy.load("nl_core_news_sm")
except OSError:
    print("⚠️ Model 'nl_core_news_sm' niet gevonden. Probeer te installeren...")
    # Use sys.executable to ensure the correct Python interpreter is used
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "nl_core_news_sm"])
        nlp = spacy.load("nl_core_news_sm")
        print("✅ Model 'nl_core_news_sm' succesvol geïnstalleerd en geladen.")
    except Exception as e:
        print(f"❌ Kon model 'nl_core_news_sm' niet installeren of laden: {e}")
        print("Installeer handmatig met: !python -m spacy download nl_core_news_sm")
        sys.exit(1) # Exit if installation also fails

class DelpherEntityExtractor:
    def __init__(self, nlp_model):
        self.nlp = nlp_model

        # 2. REGEX PATRONEN VOOR HISTORISCHE TEKSTEN
        # Vangt namen met initialen en titels, bijv: "prof. M. W. F. Treub", "mr. dr. H. Colijn", "H.W.A. Deterding"
        self.person_regex = re.compile(
            r'\b(?:(?:prof|dr|mr|jhr|juffr|mevr|ds|gen|kol|admr|mr\.? dr)\.\s*)*(?:[A-Z]\.\s*){1,4}[A-Z][a-zëïéèt\-]+(?:\s+[a-z]{1,4})?\s+[A-Z][a-zëïéè]+',
            re.UNICODE
        )

        # Vangt typische Delpher maatschappijen en instituties
        self.org_regex = re.compile(
            r'\b(?:[A-Z][a-zëïéèt\-]+\s+){0,4}(?:Maatschappij|Syndicaat|Ondernemersraad|Bond|Vereeniging|Fonds|Faculteit|Bank|Handelsblad|Nieuwsblad|Courant|Club)(?:\s+voor\s+[A-Z][a-zëïéèt\-]+|\s+van\s+[A-Z][a-zëïéèt\-]+)?\b',
            re.UNICODE
        )

        # Vangt historische afkortingen met punten (bijv. B.P.M., K.N.I.L., Bat. Nbl., N.V., N.I.)
        self.abbr_regex = re.compile(
            r'\b(?:[A-Z][a-zA-Z]{0,3}\.\s*){2,5}',
            re.UNICODE
        )

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        results = {
            "personen": set(),
            "maatschappijen_instituties": set(),
            "afkortingen": set(),
            "locaties": set()
        }

        # --- STAP A: REGEX EXTRACTIE ---
        # 1. Extract personen met initialen/titels
        for match in self.person_regex.finditer(text):
            clean_name = re.sub(r'\s+', ' ', match.group(0)).strip()
            results["personen"].add(clean_name)

        # 2. Extract maatschappijen en bonden
        for match in self.org_regex.finditer(text):
            clean_org = re.sub(r'\s+', ' ', match.group(0)).strip()
            # Filter te korte of foute hits
            if len(clean_org) > 5:
                results["maatschappijen_instituties"].add(clean_org)

        # 3. Extract afkortingen (en maak ze schoon)
        for match in self.abbr_regex.finditer(text):
            clean_abbr = match.group(0).strip()
            if len(clean_abbr) >= 3 and not clean_abbr.lower().startswith(('bijv.', 'uzw.', 'enz.')):
                results["afkortingen"].add(clean_abbr)

        # --- STAP B: SPACY NLP EXTRACTIE ---
        # We voeren spaCy uit op de tekst voor contextuele herkenning
        doc = self.nlp(text)

        for ent in doc.ents:
            clean_text = re.sub(r'\s+', ' ', ent.text).strip()

            # Voeg alleen locaties (GPE/LOC) en extra organisaties toe (die RegEx gemist heeft)
            if ent.label_ in ["GPE", "LOC"] and len(clean_text) > 2:
                results["locaties"].add(clean_text)
            elif ent.label_ == "ORG" and len(clean_text) > 3:
                # Voorkom duplicaten met al gevonden afkortingen
                if not any(clean_text in abbr for abbr in results["afkortingen"]):
                    results["maatschappijen_instituties"].add(clean_text)
            elif ent.label_ == "PER" and len(clean_text) > 3:
                # Als spaCy een persoon vindt zonder initialen (bijv. "Treub" of "Colijn")
                # voeg toe als er niet al een volledige naam in staat
                if not any(clean_text in p for p in results["personen"]):
                    results["personen"].add(clean_text)

        # Gesorteerde lijsten teruggeven
        return {k: sorted(list(v)) for k, v in results.items()}

# ==========================================
# TEST MET DE ARCHIEFTEKST OVER TREUB
# ==========================================
if __name__ == "__main__":
    test_tekst = """
    Batavia. Het Bat. Nbl. meldt, dat de regeering heeft beslist, dat het Suikersyndicaat
    voortaan wederom zal worden geraadpleegd over alle aangelegenheden, waarin de suikerindustrie
    is betrokken of waarbij zij betrokken kan worden. (Aneta)

    Deze beslissing van de regeering is het logisch gevolg van het uittreden van den Bond van
    Eigenaren van Nederlandsch-Indische Suikerondernemingen uit den Indischen Ondernemersraad en het
    daarmede samenhangende uittreden, in Indië, van het Suikersyndicaat uit den Ondernemersraad.

    Zooals men weet, was het sinds jaren de gewoonte, dat de regeering over alle zaken waarbij het
    belang van de suikerindustrie was betrokken, advies vroeg van het Suikersyndicaat. Bij zijn
    laatste verblijf in Indië had prof. M. W. F. Treub, de voorzitter van den Ondernemersraad, echter bewerkt
    dat deze adviseerende bevoegdheid zou worden beperkt tot die aangelegenheden, die speciaal de
    suikerindustrie betroffen; in zaken van algemeenen aard zou de Ondernemersbond advies uitbrengen.
    Tegenover de B.P.M. en het K.N.I.L. in Balikpapan en Tarakan stelde ook mr. dr. H. Colijn zich kritisch op.
    """

    extractor = DelpherEntityExtractor(nlp)
    geextraheerde_data = extractor.extract_entities(test_tekst)

    # Resultaten netjes printen voor het noteboek
    import json
    print("--- 🔍 GEËXTRAHEERDE HISTORISCHE ENTITEITEN ---")
    print(json.dumps(geextraheerde_data, indent=2, ensure_ascii=False))
