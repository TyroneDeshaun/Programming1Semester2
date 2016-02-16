import random

isRunning = str(input("Type if Yes if you want this program to work.(Caps matters) "))
oPQuestions = ("What is the meaning of life? ",
               "Where did we come from? ",
               "Who is the most important person on earth? ",
               "Where are we going? ",
               "Why are we here? ",
               "What is the best twitch emoticon? ",
               "Kappa or Nah? ",
               "What do you think you symbolize? ",
               "Would you sacrifice 100 close people to you for the world? ",
               "Would you sacrifice the world for 100 people close to you? ")

while((isRunning) == "Yes"):
    x = str(input(random.choice(oPQuestions)))
    my_file = open("kappa.txt","a")
    my_file.write((x) + "\n")
    my_file.close()
    isRunning = str(input("Type Stop if you want this program to stop.(Caps matters. "))
else:
    print("K cya")
