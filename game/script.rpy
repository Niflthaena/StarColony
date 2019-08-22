# The script of the game goes in this file.

image bg defaultBG = "defaultBG.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cayden, Fleet Captain", color="#00FFFF")
define e = Character("Edith, Colonist Rep", color ="#FF0000")
define l = Character("Lamea, Advisor", color ="#FFFFFF")
define m = Character("Max, Scientist", color ="#00FF00")
define n = Character(None, kind=nvl)
define r = Character("Cute Robot", color="#D3D3D3")


# Resource meters
# Reputation Meter

init -2 python:
    ## Resource Reputation --------------
   
    reputation = 50 #The number of points she Starts with. 
    max_reputation = 100  #The maximum points she can get. 

init python: 
    ## ------------ Reputation Points Activation Code-------------------
    #This controls when the love-points floater appears. 
    show_reputation=False

    ## ------------ Reputation Points Floating Meter --------------------
    def stats_overlay():               
        
        # --- Reputation Bar -------
        if show_reputation:
            ui.frame(
                xpos = 10, #centered 0.5
                ypos = 100,) #400 px Down from the Top
            
            ui.vbox(xalign = 0.5)
            ui.text ("Reputation: %d" %reputation, 
                xalign = 0.5)
            ui.bar(max_reputation, reputation, 
                style="my_bar")
            
            ui.close()
    config.overlay_functions.append(stats_overlay)
    
# Credits meter

init -2 python:
    ## Resource Credits --------------
   
    credits = 50 #The number of points she Starts with. 
    max_credits = 100  #max points

init python: 
    ## ------------ Credits Points Activation Code-------------------
    #This controls when the love-points floater appears. 
    show_credits=False

    ## ------------ Credits Points Floating Meter --------------------
    def stats_overlay():               
        
        # --- Credits Bar -------
        if show_credits:
            ui.frame(
                xpos = 330, #centered 0.5
                ypos = 100,) #400 px Down from the Top
            
            ui.vbox(xalign = 0.5)
            ui.text ("Credits: %d" %credits, 
                xalign = 0.5)
            ui.bar(max_credits, credits, 
                style="my_bar")
            
            ui.close()
    config.overlay_functions.append(stats_overlay)

# Tech meter

init -2 python:
    ## Resource Tech --------------
   
    tech = 50 #starting points 
    max_tech = 100  #max points

init python: 
    ## ------------ Tech Points Activation Code-------------------
    #This controls when the love-points floater appears. 
    show_tech=False

    ## ------------ Tech Points Floating Meter --------------------
    def stats_overlay():               
        
        # --- Tech Bar -------
        if show_tech:
            ui.frame(
                xpos = 650, #centered 0.5
                ypos = 100,) #400 px Down from the Top
            
            ui.vbox(xalign = 0.5)
            ui.text ("Tech: %d" %tech, 
                xalign = 0.5)
            ui.bar(max_tech, tech, 
                style="my_bar")
            
            ui.close()
    config.overlay_functions.append(stats_overlay)

# Star Fleet meter

init -2 python:
    ## Resource Fleet --------------
   
    fleet = 50 #starting points 
    max_fleet = 100  #max points

init python: 
    ## ------------ Fleet Points Activation Code-------------------
    #This controls when the love-points floater appears. 
    show_fleet=False

    ## ------------ Fleet Points Floating Meter --------------------
    def stats_overlay():               
        
        # --- Fleet Bar -------
        if show_fleet:
            ui.frame(
                xpos = 950, #centered 0.5
                ypos = 100,) #400 px Down from the Top
            
            ui.vbox(xalign = 0.5)
            ui.text ("Fleet: %d" %fleet, 
                xalign = 0.5)
            ui.bar(max_fleet, fleet, 
                style="my_bar")
            
            ui.close()
    config.overlay_functions.append(stats_overlay)


# The game starts here.

label start:
    "Choose which chapter to skip to:"
    menu:
        "Tutorial":
            jump tutorial
            
        "Beginning":
            
            "This will jump past the tutorial. Select configurations:"
    
            $ player_name = renpy.input("What's your name?", default="Magicalgirl123")
            $ player_name = player_name.strip()
    
            # The .strip() instruction removes any extra spaces the player 
            # may have typed by accident.

            #  If the player can't be bothered to choose a name, then we
            #  choose a suitable one for them:
            if player_name == "":
                $ player_name="Magicalgirl123"
            
            $ player_colony = renpy.input("Name your colony", default="Eve")
            $ player_colony = player_colony.strip()
    
            # The .strip() instruction removes any extra spaces the player 
            # may have typed by accident.

            #  If the player can't be bothered to choose a name, then we
            #  choose a suitable one for them:
            if player_colony == "":
                $ player_colony="Eve"
                
            # Global Variables
            $ years = 0
                
            jump beginning
            
label tutorial: 
    
    # Global Variables
    $ years = 0
    $ title = "Commander"
    
    scene bg defaultBG
    
    "Morning, %(title)s!"
    "Uh-oh. You got that look on your face again. You've forgotten everything, haven't you?"
    l "That's a-okay! Your righteous second-in-command, Lamea, is here to help!"
    l "So let's start off with a simple question."
    
    $ player_name = renpy.input("What's your name?", default="Magicalgirl123")
    $ player_name = player_name.strip()
    
    # The .strip() instruction removes any extra spaces the player 
    # may have typed by accident.

    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="Magicalgirl123"
                
    l "Yeah! %(title)s %(player_name)s, we just settled on this new planet and have started a colony."
    
    $ player_colony = renpy.input("What will be the name of our star colony?", default="Eve")
    $ player_colony = player_colony.strip()
    if player_colony == "":
        $ player_colony="Eve"
                
    l "%(player_colony)s, huh? I like the sound of that."
    l "As %(title)s of %(player_colony)s, you'll be making decisions for our planet."
    l "Don't worry, it's easy! Just say yes or no, okay?"
    
    menu: 
        
        "Yes":
        
            l "Yeah! You're starting to get the hang of it already."
        
        "No":
            
            l "Ha ha. You're hilarious, %(title)s."
            
    l "Keep a careful eye on our resources."
    $ show_reputation=True 
    l "There's our political influence,"
    $ show_credits=True
    l "money,"
    $ show_tech=True
    l "technology,"
    $ show_fleet=True
    l "and military strength."
    # This makes the Meter appear.

    # pause 0.5
    # This makes the meter sit there for half a second, so that when the points 
    # are added, the player can actually 'see' the meter extend.

    # $ reputation+=50
    #This adds points to the meter. 
    
    #  show expression Text("{color=ffffff}+50 Reputation Points{/color}", 
    #    size=50, 
    #    yalign=0.1, # Centers the text -- Toward Bottom.
    #    xalign=0.1, # Centers the text -- Toward Right. 
    #    drop_shadow=(2, 2)) as text
    # with dissolve
    
    $ show_reputation=True
    # This is a Refresh that shows the increase in points ON the meter.

    # $ renpy.pause()
    #This keeps the bar visible until the player hits a key. 

    
label beginning:

    $ clearEvents()
    $ registerEvent("miningwitheriumC", "miningwitheriumC", 1)
    $ registerEvent("colonistaidF", "colonistaidF", 1)
    $ registerEvent("alchemyT", "alchemyT", 1)
    $ registerEvent("touristF", "touristF", 1)
    $ registerEvent("expeditionF", "expeditionF", 1)
    $ registerEvent("taxesC", "taxesC", 1)
    $ registerEvent("tvC", "tvC", 1)
    $ registerEvent("weaponsT", "weaponsT", 1)
    $ registerEvent("aiT", "aiT", 1)
    $ registerEvent("doctorT", "doctorT", 1)
    $ registerEvent("experimentT", "experimentT", 1)
    $ registerEvent("mutationsT", "mutationsT", 1)
    $ registerEvent("parasiteT", "parasiteT", 1)
    $ registerEvent("piratesF", "piratesF", 1)
    $ registerEvent("roguesF", "roguesF", 1)
    $ registerEvent("warF", "warF", 1)
    $ registerEvent("weaponF", "weaponF", 1)
    $ registerEvent("wagesF", "wagesF", 1)
    $ registerEvent("taxesCE", "taxesCE", 1)
    $ registerEvent("investmentC", "investmentC", 1)
    $ registerEvent("festivalR", "festivalR", 1)
    $ registerEvent("clonesT", "clonesT", 1)
    $ registerEvent("diseaseO", "diseaseO", 1)
    $ registerEvent("vigilanteO", "vigilanteO", 1)
    
    scene bg defaultBG
    
    l "Let's make %(player_colony)s a great place to live."
    
    $ reputation = 50
    $ credits = 50
    $ tech = 50
    $ fleet = 50
    $ years = 0
    $ title = "Commander"
    
    # scenario variables
    $ expedition = 0
    $ war = 0
    $ robot = 0
    $ investment = 0
    $ clone = 0
    $ disease = 0
    $ vigilante = 0
    
    $ show_reputation=True
    $ show_credits=True
    $ show_tech=True
    $ show_fleet=True
    
    # Randomization Event code
    
label base_travel_events:
    
    # Check loss conditions first, before moving to random choice
    
    if reputation <= 0:
        jump reputationZ
    elif reputation >= 100:
        jump reputationM
    elif credits <= 0:
        jump creditsZ
    elif credits >= 100:
        jump creditsM
    elif tech <= 0:
        jump techZ
    elif tech >= 100:
        jump techM
    elif fleet <= 0:
        jump fleetZ
    elif fleet >= 100:
        jump fleetM
        
    # increase years counter if no losses are met
    $ years+=1
    
    if years <= 1:
        l "%(player_colony)s has been colonized for %(years)s year."
    elif years >= 2:
        l "%(player_colony)s has been colonized for %(years)s years."
    

    # event hub
    $ choice = chooseRandomEvent()
    jump expression choice

            
## Death Scenes

label reputationM:
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "You hear the sound of stampeding feet. At the sound of a polite knock, you open your door.
       Colonists rush in and lay claim to the title of %(title)s. You are thrown into the prison, where you are well-taken care of, but not allowed to leave."
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
label reputationZ:
    
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "You hear the sound of stampeding feet. There are shouts and gunfire, as the people of your colony stampede past your security.
       Colonists rush in and kill you."
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
label creditsM:
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "News of your wealth reaches even the most distant planets. 
       A powerful planet, under the disguise of pirates, infiltrates your Command Center and kills you."
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
label creditsZ:
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "The colonists of your own planet fund everything. They purchase the Command Center and throw you out!"
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
label techM:
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "Your scientist create the perfect specimen to utterly destroy everything that it fights.
       Except then it gets loose. It wipes out the Command Center, killing you and all your men."
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
label techZ:
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "Your scientists claim to have created the perfect vaccine against deadly diseases.
       It's only after they've administered it to you and all the people that they realize it wasn't strained properly, and everyone gets sick and dies."
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
label fleetM:
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "The doors to your Command Center open without your clearance, revealing armed soldiers from your fleet.
       'This is a coup!' the captain screams, and you are killed along with your few remaining soldiers."
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
label fleetZ:
    
    # hide variable bars
    $ show_reputation=False
    $ show_credits=False
    $ show_tech=False
    $ show_fleet=False
    
    nvl clear
    
    "A large force from an enemy planet invades your colony. Your fleet is too weak to do anything to stop them,
       and you are killed when they invade the Command center."
    n "{b}{color=#f00}{size=+10}Game over! You survived %(years)s years.{/b}{/color}{/size}"
    
    nvl clear
    jump beginning
    
    


    # This ends the game.

    return
