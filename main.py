import re
def normalize_value(value, replacements):
    for pattern, replacement in replacements.items():
        if re.match(pattern, value, re.IGNORECASE):
            return replacement
    return value
type1, type2, type3, type4, type5, type6, type7, type8, type9, type10, type11, type12, type13, type14, type15, type16, type17 = ('',) * 17
# Define regex patterns and replacements
regex_replacements = {

    r"\bclés disponibles en agence\b": "Clés agence",
    r"\brdv sur place\b": "RDV sur place",
    r"\bavec le propriétaire\b": "Avec le propriétaire",
    r"\bavec un locataire\b": "Avec un locataire",
    r"\bavec une personne de l'agence\b": "Avec une personne de l'agence",
    r"\bavec une tierce personne\b": "Avec une tierce personne",
    r"\bindividuel électrique\b": "Individuel élec",
    r"\bindividuel gaz\b": "Individuel gaz",
    r"\bcollectif\b": "Collectif",
    r"\bpas de chauffage\b": "Pas de chauffage",
    r"\bautre\b": "Autre",
    r"\bvente\b": "Vente",
    r"\blocation\b": "Location",
    r"\brénovation énergétique\b": "Rénovation énergétique",
    r"\bavant-travaux / avant-démolition\b": "Avant travaux",
    r"\brur place\b": "Sur place",
    r"\ba réception de facture\b": "A réception de facture",
    r"\bmaison\b": "Maison",
    r"\bappartment\b": "Appartment",
    r"\bgarage\b": "Garage",
    r"\bimmeuble\b": "Immeuble",
    r"\blocal commercial ou professionnel\b": "Local commercial ou professionnel",
    r"\bparties communes\b": "Parties communes",
    r"\bpas de mode de production d'eau chaude\b": "Pas de mode de production d'eau chaude",
    r"\bdiagnostics de performance énergétique (dpe)\b": "Diagnostics de Performance énergétique (DPE)",
    r"\boui\b": "Oui",
    r"\bnon\b": "Non",
    r"\bpropriétaire\b": "Propriétaires",
    r"\bagence\b": "Agence",
    
}
type17 = input_data.get('Superficie Carrez/Boutin')
type16 = input_data.get('Diagnostics de Performance énergétique (DPE)')
type14 = input_data.get('Investigations complémentaires (IC)')
type15 = input_data.get('Audit énergétique réglementaire')
type1 = input_data.get('Diagnostic Amiante')
type2 = input_data.get('Diagnostic Plomb')
type3 = input_data.get('Diagnostic Électrique')
type4 = input_data.get('Diagnostic Gaz')
type5 = input_data.get('Diagnostic Termites')
type6 = input_data.get('Etat Parasitaire')
type7 = input_data.get('Etat des Risques et Pollution (ERP)')
type8 = input_data.get('Assainissement')
type9 = input_data.get('Pré-audit')
type10 = input_data.get('DPE projeté')
type11 = input_data.get("Besoin d'accompagnement pour être sûr(e) des diagnostics nécessaires")
# type12 = input_data.get('DPE sur Plan')
type13 = input_data.get('DPE Collectif')

if type16 == "checked":
    type16 = "Diagnostics de Performance énergétique (DPE)"
if type1 == "checked":
    type1 = "Diagnostic Amiante"
if type2 == "checked":
    type2 = "Diagnostic Plomb (constructions datant d'avant 1949)"
if type3 == "checked":
    type3 = "Diagnostic Électrique"
if type4 == "checked":
    type4 = "Diagnostic Gaz"
if type5 == "checked":
    type5 = "Diagnostic Termites"
if type6 == "checked":
    type6 = "Etat Parasitaire"
if type7 == "checked":
    type7 = "Etat des Risques et Pollution (ERP)"
if type8 == "checked":
    type8 = "Assainissement"
if type9 == "checked":
    type9 = "Pré-audit"
if type10 == "checked":
    type10 = "DPE projeté"
if type11 == "checked":
    type11 = "Besoin d'accompagnement pour être sûr(e) des diagnostics nécessaires"
# if type12 == "checked":
#     type12 = "DPE sur Plan"
if type13 == "checked":
    type13 = "DPE Collectif"
if type14 == "checked":
    type14 = "Investigations complémentaires (IC)"
if type15 == "checked":
    type15 = "Audit énergétique réglementaire"
if type17 == "checked":
    type17 = "Superficie Carrez/Boutin"

output = {key: normalize_value(value, regex_replacements) for key, value in input_data.items()}
output["type1"] = type1
output["type2"] = type2
output["type3"] = type3
output["type4"] = type4
output["type5"] = type5
output["type6"] = type6
output["type7"] = type7
output["type8"] = type8
output["type9"] = type9
output["type10"] = type10
output["type11"] = type11
# "type12" = type12,
output["type13"] = type13
output["type14"] = type14
output["type15"] = type15
output["type16"] = type16
output["type17"] = type17