import random
print("Welcome to Mo's Chatbot. What's on your favorite video game, console, or genre type?")
doExit = False

while doExit == False:
    choice = input()
    if choice == "quit":
        doExit = True
        break

    #listen and respond to feelings
    if choice.find("Playstation") != -1 or choice.find("Xbox") != -1 or choice.find("PC") != -1 or choice.find("Nintendo") != -1 :
        print("Thats a good console to play on since it has a game variety")
        
    elif choice.find("Minecraft") != -1 or choice.find("TitanFall") != -1 or choice.find("Call of Duty") != -1 or choice.find("Fortnite") != -1 :
        print("Thats a good game to play when your bored")

    elif choice.find("FPS") != -1 or choice.find("Platformer") != -1 or choice.find("Puzzle") != -1 or choice.find("Horror") != -1 :
        print("Those genres are pretty good.")


    elif choice.find("I like ") != -1: #these next three lines let you repeat the word after "I'm" back in a sentence
        word_list = choice.split() #break the sentence into a list with one word per slot
        next_word = word_list[word_list.index("I like ")+1] #find the word after "I'm"
        print("Why do you like", next_word+ "?") #repeat it back 
        #NOTE: it would be good to add an if statement here checking if the next word was "a" 
        #so if someone says "I'm a frog", it doesn't say back, "Why are you a?"

    #listen and respond to specific topics
     
    else: #randomize last statement so it's not too repetetive 
        num = random.randrange(1, 100)
        if num <50:
            print("Can you tell me more?")
        else:
            print("What does that suggest to you?")
