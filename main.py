import requests

from spells import SmallSpell, FullSpell, AllSpells

from pydantic import ValidationError

 
spellListPath = "spells.txt"
base_api_url = "https://www.dnd5eapi.co/api/2014/spells/"

def addSpelltoList(spellIndex):
    spellList = open(spellListPath,"a")
    spellList.writelines(spellIndex)
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
        try:
            return FullSpell(**data)

        except ValidationError:
            print("validation error")
            exit()
    else:
        print(" status bad error")
        print(result.status_code)
        exit()

allspells = getValidateResultAllSpells()
option = ""
while (option != "4"):
    print("D&D spells list!\n [1] View/Edit List\n [2] Search Spells\n [3] View Spell\n [4] Exit")
    option = input()
    if (option == "1"):
        spellListfile = open(spellListPath,"r")
        listSpellsList = spellListfile.readlines()
        spellListfile.close()
        spellnumbering = 0
        for spell in listSpellsList:
            spellnumbering += 1
            print(f" [{spellnumbering}] {getValidateResultFullSpell(spell.strip()).printBasic()}")

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
        retrievedSpell:FullSpell = getValidateResultFullSpell(desiredSpellIndex)
        print(retrievedSpell.__repr__())
        wantaddspell = input("Would you like to add this spell to your list?(yes or no)")
        if (wantaddspell == "yes" or wantaddspell == "y"):
            addSpelltoList(desiredSpellIndex)
        