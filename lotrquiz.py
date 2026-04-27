'''
Mitchell Johnston 20/4/2026
This is my code about the lord of the rings and new zealand, the questions are
 multichoice so the user has a more fair chance of getting the question correct
'''
#this is the list of all the questions
questions = ["What town in New Zealand were the hobbits homes created?", 
            "What did Gollum call the one ring?",
            "What race are the main characters in the movies?",
            "What is the name of the big battle in the third film?", 
            "Where is Mt doom/Mordor in NZ?", 
            "How many films are in the LOTR series?", 
            "What is the name of the Dark Lord?", 
            "What Mountain is the filming location for the Edoras (The Capital city of Rohan) in Lord Of The Rings",]
#this is the list of all the answers 
options = ["1. Matamata\n2. Tauranga\n3. Auckland\n4. Dunedin", 
        "1. His Ring\n2. His Wife\n3. His Precious\n4. His Favourite\n",
        "1. Elf\n2. Hobbit\n3. Dwarf\n4. Orc\n",
        "1. Battle of Helm's Deep\n2. Battle of Moscow\n3. Battle of Gate Pa\n4. Battle of the Pelennor Fields\n",
        "1. Mt cook\n2. Mt Ngauruhoe\n3. Taranaki\n4. Mt Maunganui\n",
        "1. 3\n2. 4\n3. 8\n4. 1\n",
        "1. Sam Wise\n2. Sauron\n3. Hitler\n4. Gandalf\n",
        "1. Mount Sunday\n2. Aoraki \n3. Mount tasman\n4. Mount ruapehu\n",]
Correctanswer = [1,3,2,4,2,1,2,1]
wrongscore = 0
score = 0
questionno = 0

for x in questions:
    print(questions[questionno])
    print(options[questionno])
    answer = int(input("Select the number that you think is the answer: "))
    if answer == Correctanswer[questionno]:
        score = score + 1
    else:
        wrongscore = wrongscore + 1

    questionno = questionno + 1
    print("")

print(f"You got {score}")