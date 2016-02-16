import random
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
               
x = str(input(random.choice(oPQuestions)))

my_file = open("kappa.txt","w")
my_file.write((x))
my_file.close()
