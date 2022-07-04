def game_over():
    print("Oh no! It's game over. Would you like to play again?")
    playagain = input(">").lower()
    if "y" in playagain:
        start()
    else:
        exit()
wizard = 0
fighter = 1

def wizfig():
    print ("Why don't we try this. Do you feel any magic coursing through your veins? You know, sparks shooting out of your fingertips, the pull of the universe, the whole shebang? ")
    classtype = input(">").lower()
    if "y" in classtype:
        def playertype():
            global wizard
            wizard = True
        print ("Sounds cool. You shoot some sparks out of your fingertips, but it doesn't really help to keep you dry.")
        bartime()
    elif "n" in classtype:
        def playertype():
            global fighter
            fighter = True
        print("That seems fine. You don't remember having to rely on magic before, and there's no need to start now.")
        bartime()
    else:
        print ("That means nothing to me. Try again, and use a YES or a NO this time.")
        wizfig()

def battlewin():
    print("After your rather distasteful work has finished, you emerge from the basement, bathed in only the sickly colors of rat guts splattered over your clothes. The bartender hurriedly motions you to move away from the customers and over to their small office. 'Thanks so much. I really appreciate it,' they say, furtively pressing a wrinkled and folded bill into your hand.")
    print("Mission accomplished! I, the narrator, definitely knew you could do it. Would you like to play again?")
    playagain = input(">").upper()
    if "Y" in playagain:
        start()
    elif "N" in playagain:
        exit()
    else: print("Let's try that again. Yes or no?")
def battlelose():
    print("You flee the alleyway and hunker down near the street, until you build up the strength to go to wherever your home is.")
    print("Would you like to play again?")
    playgain = input(">").upper()
    if "Y" in playgain:
        start()
    elif "N" in playgain:
        exit()
    else: print("Let's try that again. Yes or no?") 

class Weapon:
    weapon = "weapon"
    def __init__(self, wep):
        self.wep = wep
wand = Weapon("wand")
hammer = Weapon("hammer")
pot = Weapon("pot lid")
        
def quest():
    print("\n'I'm not a monster, of course. I'll give you whatever you need to start. And by whatever you need, I mean whatever's left in the bar Lost and Found.' You walk over the Lost and Found, where you see a wand, a hammer, and a pot lid.  'Hey,' the bartender calls. 'I didn't say it would be useful.'")
    print("\nWhich one do you take?")
    stuff = input(">").upper()
    if "WAND" in stuff and wizard:
        wand = True
        print("You take the wand. It feels almost too light in your hand. You flick the wand experimentally, and some sparks shoot out. You think that you might've had a wand before your drunken stupor.")
        begin()
    if "WAND" in stuff and fighter: 
        wand = True
        print("You take the wand. It feels almost too light in your hand. You flick the wand, and accidentally shoot out a stream of sparks at a patron's mug of beer. He glares at you as you hurriedly turn away.")
        begin()
    elif "HAMMER" in stuff and wizard:
        hammer = True
        print("You take the hammer. It seems weighty in your hand. A little too weighty, if anything. It even seems a little hard to hold with one hand, but you tough it out in order to look cool in front of the customers.")
        begin()
    elif "HAMMER" in stuff and fighter:
        hammer = True
        print("You take the hammer. It seems weighty in your hand. It feels perfect. Your hands curl around the grip, and you give a careful experimental swing.")
        begin()
    elif "POT" in stuff:
        print(" You curiously pick up the pot lid, giving it a few experimental spins around your finger. A patron looks at you, impressed.")
        pot = True
        begin()
    else:
            print("I didn't understand that, so let's try it again. Do you want the WAND, the POT, or the HAMMER?")
def begin():
    print("You head down to the basement with your weapon of choice, amongst the sounds of a few patrons wolf-whistling and cheering for you. You ignore them, of course, feeling secure with the presence of your weapon.")
    print("The rats are almost invisible at first, but they start to creep out from the walls. Their eyes are huge and glowing, and there seem to be too many of them for the amount of rat-like bodies taking up the cramped room. The room stinks of mildew and mold, and other smells you don't even want to identify. As the rats close in on you, you take out your weapon and swing it. ")
    print("\nHere goes nothing...")
    import random
    if wand and wizard:
        fight = random.randint(1,10)
        if fight > 3:
            print("Your wand sends out a streak of flame that paints the walls black with ash and burnt rat fur. ")
            battlewin()
        if fight <= 3:
            print("Your wand sends out a streak of flame that manages to only singe the back of the rats' fur, who them lunge at you. You run out of the basement, out of the bar, and back to the safe alley. ") 
            battlelose()
    if wand and fighter:
        fight = random.randint(1,10)
        if fight > 6:
            print("Your wand sends out a streak of flame that paints the walls black with ash and burnt rat fur. ")
            battlewin()
        if fight <= 6: 
            print("Your wand sends out a streak of flame that manages to only singe the back of the rats' fur, who them lunge at you. You run out of the basement, out of the bar, and back to the safe alley. ") 
            battlelose()
    if hammer and fighter:
        fight = random.randint(1,10)
        if fight > 3:
            print("Your hammer whistles through the air, colliding with the fur, skulls, brains, and other assorted viscera of the rats at your feet.")       
            battlewin()
        if fight <= 3:
            print("Your hammer slices through the air and directly into the wall. It's so lodged in there, that the rats close in on you before you can pull it out. You run out of the basement, out of the bar, and back to the safe alley. ") 
            battlelose()
    if hammer and wizard:
        fight = random.randint(1,10)
        if fight > 6:
            print("Your hammer whistles through the air, colliding with the fur, skulls, brains, and other assorted viscera of the rats at your feet.")       
            battlewin()
        if fight <= 6:
            print("Your hammer slices through the air and directly into the wall. It's so lodged in there, that the rats close in on you before you can pull it out. You run out of the basement, out of the bar, and back to the safe alley. ") 
            battlelose()
    if pot:
        fight = random.randint(1,10)
        if fight > 6:
            print("You brandish the pot lid in front of you like a shield. The rats stare at it, entranced by the mottled, warped reflections in the lid, and shrink back into the darkness.")
            battlewin()
        if fight <= 6:
            print("You swing the pot lid, and the rats stare unimpressed as it sails over their heads. They jump at you, clawing at your clothes. You run out of the basement, out of the bar, and back to the safe alley.")
            battlelose()
def barquestion():
    print("\nThe bartender frowns, thinking. 'You know, I might have a job for an adventurer like you,'' they say thoughtfully, sizing you up. ")
    print("\n 'What do you say about clearing out some rats I have in my basement? Just a few fantasy rats, nothing a seasoned adventurer like you can't handle.' They say. 'Are you in?' ")
    answer4 = input(">").lower()
    if "y" in answer4: 
        print ("You nod vigorously. Beating up some rats is nothing you can't handle.")
        quest()
    elif "n" in answer4:
        print ("You shake your head. Rats have the same right to live as us. ") 
        persuading()
    else:
        print ("That means nothing to me. Try again, and use a YES or a NO this time.")
        barquestion()   
def bartime(): 
    print ("\nYou manage to wipe the last of the gunk off of your hands and stagger towards the only door in the alley you can see.")
    print ("\nYou put your hands on the door, hesitating. Do you want to go in? ")
    answer = input(">").lower()
    if "y" in answer:
        print ("You push on the door hesitantly, but the hinges are so slick that it slams open. It opens up to a crowded room- no, bar. The music literally screeches to a halt as a musician slams on her accordion,  air wheezing out of it. Everyone stares at you.")
        insidebar()
    elif "n" in answer:
        print("You sit back down and decide to stay out here in the alley instead. The alley is comfortable. The alley is warm. The alley is home. Feel free to stay here as long as you want.")
        game_over()
    else:
        print ("That means nothing to me. Try again, and use a YES or a NO this time.")
        bartime()
def insidebar():
    print("The bar is waiting with bated breath for your next move. Do you decide to act like you belong or ask the bartender who you are?")
    answer2 = input(">").lower()
    if "act" in answer2:
        print("You slide into the bar, nodding politely to the nearest customer, an old lady with a distinct smell of fish. You sit at an empty seat at the bar and signal to the bartender, who pours you a glass of water.")
        bartender()
    elif "ask" in answer2:
        print("You ask the bartender who you are. Amongst the laughter of the patrons, the bartender looks at you with a resigned glance that says that they've done this dance many times before. They shrug, and pointedly pour you a glass of water.")
        bartender()
    else:
        print ("That means nothing to me. Try again, and use ACT or ASK this time.")
        insidebar()
def bartender():
    print ("\nYou sit, sipping your water, when the bartender sidles up to you, eyes looking at you suspiciously. 'You seem to be doing better today,' they say, drumming their fingers on the table. 'You were quite a mess yesterday.'")    
    print("\nDo you deny it?")
    answer3 = input(">").lower()
    if "y" in answer3: 
        print ("You violently shake your head side to side. You have never been drunk in your life, you're sure of it. The bartender gives you a weird look, and continues. ")
        barquestion()
    elif "n" in answer3:
        print("You reluctantly nod. The thumping in your head is proof of their statement. The bartender pats you on the shoulder sympathetically. ")
        barquestion()
    else:
        print ("That means nothing to me. Try again, and use a YES or a NO this time.")
        bartender()


def persuading():
    print ("'C'mon, it'll take five minutes, tops. IN and out.' What do you think?")
    answer5 = input(">").lower()
    if "y" in answer5:
        print ("You nod reluctantly. It'll be a good way to get you back into the saddle again. Metaphorically, of course. If you had a horse yesterday, it's probably long gone.")
        quest()
    elif "n" in answer5: 
        print ("You shake your head, and the bartender leaves you alone. You enjoy your drink in silence.")
        game_over()
    else:
        print ("That means nothing to me. Try again, and use a YES or a NO this time.")
        persuading()
def guess():
    action = input(">").upper()
    print ("Will", action, "work though? I'm not so sure about that. ")
    wizfig()



def start():
    print ("\nYou wake up and the first thing you feel is a steady dripping of some sort of liquid onto your head. You back aches, and your hand instinctually goes to clutch your head. When you push yourself to stand up, you realize that the ground is more than just damp- it's straight up wet. You quickly wipe your hands on your pants, and that's when you realize. You don't know your name. Time to make one up for yourself.")
    print ("\nWhat is your name?")
    name = input(">").upper()
    print ("\nSounds like a nice name. So" , name ,", what are you going to do to get out of this mess?")
    guess()

start()