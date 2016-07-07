#WRITE RANDOM NAMES AND SPECIALTIES ONTO LMCOdata.txt

import names
import math
import random

specialties = ['Data Analytics', 'Structural Engineering', 'Management', 'Chemical Processes', 'Materials Engineering', "Mechanical Engineering", "IT", 'Software Engineering', 'Systems Engineering']

theFile = open('LMCOdata.txt', 'w')

def randomSpecialty():
    return specialties[int(str(math.floor(float(len(specialties)*random.random())))[0])]

def writeNames(x):
    """WRITES x NAMES ONTO DATA ATTACHED WITH THEIR SPECIALTIES"""
    for i in range(x):
        newName = names.get_full_name()
        newSpecialties = []
        for i in range(int(str(math.floor(float(3*random.random())))[0]) + 1):
            newSpec = randomSpecialty()
            if newSpec in newSpecialties:
                newSpecialties += []
            newSpecialties += [randomSpecialty()]
        newLine = newName + ":" + ",".join(newSpecialties) + '\n'
        theFile.write(newLine)
