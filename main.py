import requests

from spells import SmallSpell, FullSpell, AllSpells

from pydantic import ValidationError

 

base_api_url = "https://www.dnd5eapi.co/api/2014/spells"

result = requests.get(f"{base_api_url}")

if result.status_code == 200: # everything is ok :)

    data = result.json()

 

    try:

        allspells = AllSpells(**data)

 

    except ValidationError:

        print("error")

        exit()

else:

    print("error")

    exit()

for spell in allspells.results:
    print(spell.__repr__())