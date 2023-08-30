import os
import random

teamScore1 = 0
teamScore2 = 0
turn = 0

massRelations = {100: ["Calculate the molar mass of calcium phosphate.", "A. 135.05 g/mol", "B. 270.10 g/mol", "C. 278.18 g/mol", "D. 310.17 g/mol", "D", False], 200: ["Acetaminophen, an analgesic and antipyretic drug, has a mass percent composition of 63.56% C, 6.00% H, 9.27% N, and 21.17% O. What is the molar mass of acetaminophen, given that its empirical formula is the same as its molecular formula?", "A. 137.16 g/mol", "B. 151.17 g/mol", "C. 153.16 g/mol", "D. 167.16 g/mol", "B", False], 300: ["In the Haber Process, hydrogen gas and nitrogen gas are reacted to form ammonia (NH3). When 100 grams of hydrogen gas are added to excess nitrogen gas, 30 grams of ammonia are formed. Calculate the percent yield of the reaction.", "A.  5.0%", "B. 5.2%", "C. 5.4%", "D. 5.6%", "C", False]}
electronConfiguration = {100: ["Which of the following states that every orbital in a sublevel is singly occupied before any orbital is doubly occupied?", "A. Pauli Exclusion Principle", "B. Hund’s Rule", "C. Schrödinger Equation", "D. Aufbau Principle", "B", False], 200: ["The highest energy sublevel in the ground state electron configuration of an atom is the 4p sublevel, occupied by 3 electrons total. What element is the identity of the atom?", "A. Arsenic", "B. Selenium", "C. Antimony", "D. Tellurium", "A", False], 300: ["Which of the following atoms contains the most unpaired electrons in its ground state?", "A. Beryllium", "B. Aluminum", "C. Titanium", "D. Copper", "C", False]}
chemistryStudyOfChange = {100: ["Determine the number of significant figures in 0.964", "A. One", "B. Two", "C. Three", "D. Four", "C", False], 200: ["If the mass is 22 and the volume is 11, what is the density?", "A. 242", "B. 222", "C. 2", "D. 4", "C", False], 300: ["A person ate a hamburger that was 1.24 pounds (lb). What is the mass in milligrams (mg)?", "A. 1.1E-3", "B. 2.3E-2", "C. 7.2E4", "D. 5.6E5", "D", False]}
aMI = {100: ["The number of protons plus neutrons is equal to?", "A. Mass number", "B. Atomic number", "C. Charge", "D. None of the above", "A", False], 200: ["Which of the following is an alkali metal?", "A. Fr", "B. Mt", "C. Ds", "D. N", "A", False], 300: ["How many number of protons, neutrons and electrons are in Carbon-14?", "A. 6,8,6", "B. 7,9,5", "C. 5,9,5", "D. 2,10,2", "A", False]}
molarity = {100: ["Calucate the concentration of 10g of Hydrochloric Acid in 250ml of water.", "A. 1.01M", "B. 0.90M", "C. 0.040M", "D. 0.40M", "A", False], 200: ["What volume of a 1.00-M Fe(NO3)3 solution can be diluted to prepare 1.00 L of a solution with a concentration of 0.250 M?", "A. 1L", "B. 2.5mL", "C. 0.250L", "D. 35cm^3", "C", False], 300: ["You prepare 525 mL of a 0.50 M solution of HI in an Erlenmeyer flask. You forget to seal the flask and don’t realize this until you find it three days later. Checking its molarity, you now find it to be a 0.82 M solution. How much water evaporated?", "A. 20mL", "B. 820mL", "C. 320mL", "D. 210mL", "D", False]}
electronegativity = {100: ["What type of bond is polar-covalent bond?", "A. Chemical bond where a pair of electrons is unequally shared between two atoms.", "B. Chemical bond between two metals", "C. Chemical bond where a pair of electrons is equally shared between two atoms.", "D. Chemical bond with a complete transfer of electrons between one atom to another.", "A", False], 200: ["Which of the following is a polar covalent molecule", "A. HF", "B. NaCl", "C. H+", "D. H2", "A", False], 300: ["Draw the all the resonance structures for SO4 2-. How many resonance structures does it have?", "A. 3", "B. 4", "C. 5", "D. 6", "D", False]} 
MolecularGeometry = {100: ["What is the molecular geometry of CO2?", "A. Linear", "B. Bent", "C. Trigonal Pyramidal", "D. Trigonal Planar", "A", False], 200: ["What is the molecular geometry of NH3?", "A. Linear", "B. Bent", "C. Trigonal Pyramidal", "D. Trigonal Planar", "C", False], 300: ["Which molecule is planar?", "A. CF4", "B. COF2", "C. SF4", "D. SOF2", "B", False]}


def displayQuestions():
    
    print("Mass Relations in Chemical Reactions [1]")
    for points in massRelations:
        if massRelations[points][6] == False:
            print("\t" + "<Question Worth: " + str(points) + ">")

        else:
            print("\t" + "<QuestionAnswered>")


    print("Electron Configuration [2]")
    for points in electronConfiguration:
        if electronConfiguration[points][6] == False:
            print("\t" + "<Question Worth: " + str(points) + ">")

        else:
            print("\t" + "<QuestionAnswered>")


    print("Chemistry - The Study of Change [3]")
    for points in chemistryStudyOfChange:
        if chemistryStudyOfChange[points][6] == False:
            print("\t" + "<Question Worth: " + str(points) + ">")

        else:
            print("\t" + "<QuestionAnswered>")


    print("Atoms, Molecules and Ions [4]")
    for points in aMI:
        if aMI[points][6] == False:
            print("\t" + "<Question Worth: " + str(points) + ">")

        else:
            print("\t" + "<QuestionAnswered>")

    print("Molarity [5]")
    for points in molarity:
        if molarity[points][6] == False:
            print("\t" + "<Question Worth: " + str(points) + ">")

        else:
            print("\t" + "<QuestionAnswered>")

    print("Electronegativity [6]")
    for points in electronegativity:
        if electronegativity[points][6] == False:
            print("\t" + "<Question Worth: " + str(points) + ">")

        else:
            print("\t" + "<QuestionAnswered>")
          
    print("MolecularGeometry [7]")
    for points in MolecularGeometry:
        if MolecularGeometry[points][6] == False:
            print("\t" + "<Question Worth: " + str(points) + ">")

        else:
            print("\t" + "<QuestionAnswered>")



def returnDict(x):
    if x == 1:
        return massRelations

    elif x == 2:
        return electronConfiguration

    elif x == 3:
        return chemistryStudyOfChange

    elif x == 4:
        return aMI

    elif x == 5:
        return molarity

    elif x == 6:
        return electronegativity

    elif x == 7:
        return MolecularGeometry

    else:
        return("NULL")

def returnAvailableQuestions():
    return (massRelations[100][6] and massRelations[200][6] and massRelations[300][6] and electronConfiguration[100][6] and electronConfiguration[200][6] and electronConfiguration[300][6] and chemistryStudyOfChange[100][6] and chemistryStudyOfChange[200][6] and chemistryStudyOfChange[300][6] and aMI[100][6] and aMI[200][6] and aMI[300][6] and molarity[100][6] and molarity[200][6] and molarity[300][6] and electronegativity[100][6] and electronegativity [200] [6] and electronegativity[300][6] and MolecularGeometry[100][6] and MolecularGeometry[200][6] and MolecularGeometry[300][6])

def askQuestion(turn):

    global teamScore1
    global teamScore2
    
    topic = int(input("Choose a topic (Enter the Number): "))
    a = returnDict(topic)

    while (a == "NULL") or (a[100][6] == True and a[200][6] == True and a[300][6] == True):
        print("Invalid. Please try again.")
        topic = int(input())
        a = returnDict(topic)

    
    numberOfPoints = int(input("How many points (Enter the number of points: 100, 200, 300): "))
    while (a[numberOfPoints][6] == True):
        print("That question was already answered. Please try again")
        numberOfPoints = int(input())

    print(os.system("clear"))
    print(a[numberOfPoints][0])
    print("\t" + a[numberOfPoints][1])
    print("\t" + a[numberOfPoints][2])
    print("\t" + a[numberOfPoints][3])
    print("\t" + a[numberOfPoints][4])

    answer = input("Enter the letter of the correct answer.")

    if answer.upper() == a[numberOfPoints][5]:
        print("Congratulations! you got it correct.")
        a[numberOfPoints][6] = True
        if turn == 0:
            teamScore1 += numberOfPoints

        else:
            teamScore2 += numberOfPoints
    else:
        print("Sorry! you got it wrong.")
        a[numberOfPoints][6] = True
        if turn == 0:
            teamScore1 -= numberOfPoints

        else:
            teamScore2 -= numberOfPoints

    input("Press any key to continue")
        
    
    

print("Welcome to Jeopardy. Two teams will play against each other to gain the most number points by selecting and answering quesitons. \n")

turn = random.randint(0,2)

if turn == 0:
    print("Team 1 will go first.")

else:
    print("Team 2 will go first")

print("Press Any Key to Begin:")
input()





while not (returnAvailableQuestions()):
    os.system("clear")
    displayQuestions()
    askQuestion(turn)

    if turn == 0:
        turn+=1
    else:
        turn-=1

print(teamScore1)
print(teamScore2)

if teamScore1 < teamScore2:
    print("Team 2 wins!")

elif teamScore2 < teamScore1:
    print("Team 1 Wins!")

else:
    print("Draw")