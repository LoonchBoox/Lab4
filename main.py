import requests

from spells import SmallSpell, FullSpell, AllSpells

from pydantic import ValidationError

 
spellListPath = "spells.txt"
base_api_url = "https://www.dnd5eapi.co/api/2014/spells/"

def addSpelltoList(spellIndex):
    spellList = open(spellListPath,"a")
    spellList.write(f"\n{spellIndex}")
    spellList.close()

def removeSpellfromList(spellIndex):
    spellList = open(spellListPath,"r")
    listSpellsList = spellList.readlines()
    spellList.close()
    listSpellsList.remove(spellIndex)
    spellList = open(spellListPath, "w")
    for spell in listSpellsList:
        spellList.write(spell)
    spellList.close()
    print(f"{spellIndex} has been removed")

def getValidateResultAllSpells():
    result = requests.get(f"{base_api_url}")

    if result.status_code == 200: # everything is ok :)
        data = result.json()
        try:
            return AllSpells(**data)

        except ValidationError:
            print("error")
            exit()
    else:
        print("error")
        exit()

def getValidateResultFullSpell(append):
    result = requests.get(f"{base_api_url}{append}")

    if result.status_code == 200: # everything is ok :)
        data = result.json()
        return FullSpell(**data)
    else:
        print(" status bad error")
        print(result.status_code)

allspells = getValidateResultAllSpells()
option = ""
while (option != "4"):
    print("D&D spells list!\n [1] View/Edit List\n [2] Search Spells\n [3] View Spell\n [4] Exit")
    option = input()
    if (option == "1"):
        while (option != "exit"):
            spellListfile = open(spellListPath,"r")
            listSpellsList = spellListfile.readlines()
            spellListfile.close()
            print("Type the number of the spell you would like to view\nor type exit to go back...")
            spellnumbering = 0
            for spell in listSpellsList:
                spellnumbering += 1
                print(f" [{spellnumbering}] {getValidateResultFullSpell(spell.strip()).printBasic()}")
            option = input()
            try:
                print(getValidateResultFullSpell(listSpellsList[int(option)-1].strip()).__repr__())
                remove = input("\nto remove this spell from the list, type remove\n otherwise, press enter\n")
                if (remove == "remove"):
                    removeSpellfromList(listSpellsList[int(option)-1])
            except:
              print()
    if (option == "2"):
        desiredLevel = input("Please select a spell level(0 to 9):")
        for spell in allspells.results:
            if (spell.level == int(desiredLevel)):
                print(spell.__repr__())
    if (option == "3"):
        desiredSpell = input("Please enter the name of the spell you would like to view:")
        desiredSpellIndex = ""
        for spell in allspells.results:
            if (spell.name == desiredSpell):
                desiredSpellIndex = spell.index
        try:
            retrievedSpell = getValidateResultFullSpell(desiredSpellIndex)
        except:
            print("Invalid Spell Name")
        else:
            print(retrievedSpell.__repr__())
            wantaddspell = input("\nWould you like to add this spell to your list?(yes or no)")
            if (wantaddspell == "yes" or wantaddspell == "y"):
                addSpelltoList(desiredSpellIndex)