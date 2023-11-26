import json
import os
from random import choice

# Set the working directory to the location of your project
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)

class NPC:
    def __init__(self, **kwargs):

        self.name = self.generate_name()
        self.appearance = self.generate_appearance()
        self.backstory = self.generate_backstory()
        self.personality = self.generate_personality()
        self.virtue = self.generate_virtue()
        self.vice = self.generate_vice()
        self.powers = self.generate_powers()

        pass

    def generate_name(self):
        with open(os.path.join('data', 'npc_names.json'), 'r') as json_file:
            table = json.load(json_file)

        skaa_name = choice(table["Skaa"])
        first_name = choice(table["Male"] + table["Female"])
        family_name = choice(table["Family"])

        return 'Skaa: ' + skaa_name + ' OR Noble: ' + first_name + ' ' + family_name

    def generate_appearance(self):
        with open(os.path.join('data', 'npc_appearance.json'), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea
    
    def generate_backstory(self):
        with open(os.path.join('data', 'npc_backstory.json'), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea
    
    def generate_personality(self):
        with open(os.path.join('data', 'npc_personality.json'), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea
    
    def generate_virtue(self):
        with open(os.path.join('data', 'npc_virtue.json'), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea
    
    def generate_vice(self):
        with open(os.path.join('data', 'npc_vice.json'), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea
    
    def generate_powers(self):
        with open(os.path.join('data', 'npc_powers.json'), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea





