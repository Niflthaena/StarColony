﻿# The script of the game goes in this file.

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

    
label miningwitheriumC:
    
    e "We've found a mine full of witherium on %(player_colony)s, a precious mineral traded throughout the galaxy. What luck!"
    
    menu:
        
        "I'm rich!":
            
            $ reputation-=20
            $ show_reputation=True
            $ credits+=60
            $ show_credits=True
            
            e "..."
        
        "Share it with the people of %(player_colony)s.":
        
            $ reputation+=10
            $ show_reputation=True
            $ credits+=10
            $ show_credits=True
            $ tech+=10
            $ show_tech=True
            $ fleet+=10
            $ show_fleet=True
            
            e "%(player_colony)s will benefit greatly from this."

    
    jump base_travel_events
    
    
label colonistaidF:
    
    c "Our citizens have been asking the Star Fleet for protection against the local wildlife."
    
    menu: 
        
        "Aid them.":
            
            $ reputation+=10
            $ show_reputation=True
            $ credits-=10
            $ show_credits=True
            $ fleet-=20
            $ show_fleet=True
            
            c "It will cost the fleet some resources, but the people will be happy."
            
        "Let them fend for themselves.":
        
            $ reputation-=20
            $ show_reputation=True
            
            c "Everyone should learn to fight eventually, anyway."

    
    jump base_travel_events
    
label alchemyT:
    
    m "%(title)s %(player_name)s, We've made a breakthrough in alchemical technology!"
    
    menu:
        
        "Cool.":
            $ credits+=20
            $ show_credits=True
            $ tech+=30
            $ show_tech=True
            $ fleet+=30
            $ show_fleet=True
            
            m "Alchemy will benefit everyone on %(player_colony)s."
            
        "Get rid of it!":
            $ reputation-=20
            $ show_reputation=True
            
            m "B-but... science helps people..."
            
    
    jump base_travel_events
    
label touristF:
    
    l "We found a strange fountain while exploring the planet. It could be a good tourist location, but opening our borders makes us more susceptible to attack."
    l "What do you think, %(title)s?"
    
    menu: 
        
        "Open up to tourists.":
            $ reputation+=10
            $ show_reputation=True
            $ credits+=20
            $ show_credits=True
            $ fleet-=10
            $ show_fleet=True
            
            l "We'll charge everyone who wants to see the fountain."
            
        "Keep our colony isolated." :
            $ reputation-=10
            $ show_reputation=True
            $ fleet+=10
            $ show_fleet=True
            
            l "Yeah, we don't want any terrorists slipping through our defenses."
    
    jump base_travel_events
    
label expeditionF:
    
    # Set up for multi-part event
    
    if expedition == 0:
    
        e "There are many untold secrets on %(player_colony)s, just waiting to be explored. Will you fund my expedition? It is very expensive."
        
        menu:
            "Yes.":
                $ credits-=50
                $ show_credits=True
                $ expedition+=1
                
                e "I'll send a group of my men to explore, %(title)s. You'll be the first to hear about whatever they find!"
                
            "No.":
                e "Oh... is this a bad time? I'll ask again later."
                
        jump base_travel_events
    
    elif expedition == 1:
        
        e "The expedition was a success! I'll return your investment and share the profits."
        
        menu:
            
            "Great.":
                
                $ credits+=60
                $ show_credits=True
                $ reputation+=10
                $ show_reputation=True
                $ tech+=10
                $ show_tech=True
                $ fleet+=10
                $ show_fleet=True
                $ title = "Entrepreneur"
                
                e "It was a pleasure doing business with you."
                l "People have started calling you an %(title)s after this last success."
                
            "Distribute the profits equally.":
                
                $ credits+=20
                $ show_credits=True
                $ reputation+=20
                $ show_reputation=True
                $ tech+=20
                $ show_tech=True
                $ fleet+=20
                $ show_fleet=True
                $ title = "Entrepreneur"
                
                e "That's most generous of you, %(title)s %(player_name)s."
                l "People have started calling you an %(title)s after this last success."
                
        # set expedition to 0
        $ expedition=0
            
        jump base_travel_events
                
label taxesC:
    
    l "We really don't make enough money. The people won't like it, but let's increase the taxes on %(player_colony)s."
    
    menu:
        
        "Sure.":
            
            $ credits+=30
            $ show_credits=True
            $ reputation-=20
            $ show_reputation=True
            
            l "It's for the people's benefit, even if they don't realize it."
            
        "No.":
            
            $ credits-=10
            $ show_credits=True
            $ reputation+=10
            $ show_reputation=True
            
            l "Okay, but we'll need to get money from somewhere else then."
            
    jump base_travel_events
            
label tvC:
    
    l "A famous broadcaster has taken note of %(player_colony)s's unique landscape, and wants to record a show here. It's a life-or-death quiz show game. Should we let him?"
    
    menu:
        
        "Yes.":
            
            $ credits+=20
            $ show_credits=True
            $ reputation-=10
            $ show_reputation=True
            
            l "He'll give us part of his profits in return. And it sounds kind of entertaining, right?"
            
        "No.":
            
            $ credits-=10
            $ show_credits=True
            $ reputation+=10
            $ show_reputation=True
            
            l "Oh. Is it weird that I was kind of looking forward to seeing it?"
            
    jump base_travel_events
            
label weaponsT:
    
    m "%(title)s, We've found new technology that will increase our weapon power!"
    
    menu:
        
        "Good.":
            
            $ reputation-=10
            $ show_reputation=True
            $ fleet+=20
            $ show_fleet=True
            
            m "Our enemies will learn to fear us."
            
        "I don't want it.":
            
            $ reputation+=10
            $ show_reputation=True
            $ tech-=10
            $ show_tech=True
            $ fleet-=10
            $ show_fleet=True
            
            m "Don't you want our enemies to fear us, %(title)s?"
            
    jump base_travel_events
    
label aiT:
    
    if robot == 0:
        
        m "Some of our AI has become self-aware and is demanding that we give them human rights. Should we?"
            
        menu:
                
            "Sure?":
            
                $ reputation+=20
                $ show_reputation=True
                $ credits-=10
                $ show_credits=True
                $ tech-=20
                $ show_tech=True
                $ fleet-=10
                $ show_fleet=True
                $ robot = 1
                    
                m "This is going to get complicated ... and expensive ..."
                    
            "No way.":
                    
                $ reputation-=20
                $ show_reputation=True
                $ tech+=20
                $ show_tech=True
                $ fleet-=10
                $ show_fleet=True
                $ robot = 2
                    
                m "We'll teach those robots to know their place."
                
        jump base_travel_events
        
    elif robot == 1:
        
        l "A robot that was part of the emancipation movement wants to see you. Should we let her-"
        r "Beep, bop. I have traveled across the planet. All to proclaim my love to you, %(title)s %(player_name)s."
        r "Please, allow me to stay by your side."
    
        menu:
        
            "Sure?":
            
                $ reputation+=10
                $ show_reputation=True
                $ title = "Robot Lover"
                $ robot = 3
            
                r "Thank you, %(player_name)s! I will prove my worth in time."
                l "A robot girlfriend? People are going to be talking about this."
                l "And now people have started calling you %(title)s as a result..."
                
            "No way.":
            
                $ reputation-=10
                $ show_reputation=True
                $ robot = 4
            
                r "I understand... people still doubt that we robots can properly exhibit emotion. It would be risky for someone in your position."
                r "Still, I am very grateful that you have been so encouraging of pro-robot rights. I will do my best to aid you from afar."
            
        jump base_travel_events
            
    elif robot == 2:
        
        l "The AI advocating for human rights has had an episode of violence. Some colonists and soldiers were killed, but we caught one of the robot rebels. What should we do with it?"
        
        menu:
            
            "Dismantle and set an example.":
                
                $ reputation-=20
                $ show_reputation=True
                $ credits-=10
                $ show_credits=True
                $ tech-=10
                $ show_tech=True
                $ fleet-=10
                $ show_fleet=True
                $ title = "Tyrant"
                
                l "We'll add it to the scrap heap, then. Let's hope the robots cease this free will nonsense."
                l "People don't seem to like how we've been dealing with the robots. They've started calling you a %(title)s."
                
            "Reprogram its obedience.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits-=20
                $ show_credits=True
                $ tech+=10
                $ show_tech=True
                $ fleet-=10
                $ show_fleet=True
                
                l "I'll personally go and tell the scientists to get it right this time. Let's hope this is the last case of a robot uprising."
                l "People don't seem to like how we've been dealing with the robots. They've started calling you a %(title)s."
                
        jump base_travel_events
    
    elif robot == 3:
        
        l "Your robot girlfriend wants to send you a gift. She asked if you prefer money or technology."
        
        menu:
            
            "Credits.":
                
                $ reputation+=10
                $ show_reputation=True
                $ credits+=20
                $ show_credits=True
                
                l "A message came with the gift. It says 'robot emoji robot emoji heart heart robot emoji xxo'."
            
            "Tech.":
                
                $ reputation+=10
                $ show_reputation=True
                $ tech+=20
                $ show_tech=True
                
                l "A message came with the gift. It says 'robot emoji robot emoji heart heart robot emoji xxo'."
                
        jump base_travel_events
        
    elif robot == 4:
        
        l "Your definitely not robot girlfriend wants to send you a gift. She asked if you prefer money or technology."
        
        menu:
            
            "Credits.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits+=20
                $ show_credits=True
                
                l "A message came with the gift. It says 'I hope you find my continued support beneficial'."
            
            "Tech.":
                
                $ reputation-=10
                $ show_reputation=True
                $ tech+=20
                $ show_tech=True
                
                l "A message came with the gift. It says 'I hope you find my continued support beneficial'."
                
        jump base_travel_events
        
label doctorT:
    
    m "A famous doctor has traveled all the way from megapolis planet Lumines to our little colony %(player_colony)s. He's offering his services here."
    
    menu:
            
        "Welcome him.":
                
            $ reputation+=10
            $ show_reputation=True
            $ credits-=20
            $ show_credits=True
            $ tech+=20
            $ show_tech=True
                
            m "We're lucky to procure his talents for %(player_colony)s."
                
        "Turn him away.":
                
            $ reputation-=10
            $ show_reputation=True
            
            m "It's unfortunate that we can't hire him, but I'll tell him to look elsewhere for work."
                
    jump base_travel_events
        
label experimentT:
    
    m "We were working on a science experiment, but it died... then came back to life. What should we do with it?"
    
    menu:
            
        "Continue your research.":
                
            $ reputation-=10
            $ show_reputation=True
            $ credits-=10
            $ show_credits=True
            $ tech+=20
            $ show_tech=True
                
            m "Does it hold the secret of immortality...?"
                
        "Put it out of its misery.":
                
            $ reputation+=10
            $ show_reputation=True
            $ credits-=10
            $ show_credits=True
            $ tech-=20
            $ show_tech=True
                
            m "You've got a soft heart, %(title)s %(player_name)s. We'll be throwing out everything we've worked towards."
                
    jump base_travel_events
    
label mutationsT:
    
    m "Some of the people on %(player_colony)s are mutating and getting special powers. They could be dangerous if left alone, but capturing them will be expensive. What should we do?"
    
    menu:
            
        "Keep them quiet.":
                
            $ reputation-=10
            $ show_reputation=True
            $ credits-=10
            $ show_credits=True
            $ tech+=10
            $ show_tech=True
            $ fleet+=10
            $ show_fleet=True
                
            m "We'll capture them and study them intently. They'll do great work for %(player_colony)s."
                
        "Do nothing.":
                
            $ reputation+=10
            $ show_reputation=True
            $ credits+=10
            $ show_credits=True
            $ tech-=10
            $ show_tech=True
            $ fleet-=10
            $ show_fleet=True
                
            m "I hope they don't become a liability. People will figure out what's happening eventually."
                
    jump base_travel_events
    
label parasiteT:
    
    m "We've captured a parasitic alien creature, native to %(player_colony)s. It's killed a lot of people. What should we do with it?"
    
    menu:
        
        "Kill it.":
            
            $ reputation+=20
            $ show_reputation=True
            $ tech-=20
            $ show_tech=True
            
            m "I'm sure the people will be grateful that this creature is gone."
            
        "Research it.":
            
            $ reputation-=20
            $ show_reputation=True
            $ tech+=20
            $ show_tech=True
            
            m "We'll learn the secrets of this planet eventually!"
            
    jump base_travel_events
    
label piratesF:
    
    c "Pirates have started preying on trade ships within our space sector."
    
    menu:
        
        "Send the fleet!":
            
            $ reputation+=10
            $ show_reputation=True
            $ fleet-=20
            $ show_fleet=True    
            
            c "Yes %(title)s %(player_name)s, I don't care how many men we lose, we'll teach those pirates a lesson!"
            
        "Why should I care?":
            
            $ reputation-=20
            $ show_reputation=True
            
            c "Think of your people, %(title)s ..."
            
    jump base_travel_events
    
label roguesF: 
    
    c "Local thugs have begun extorting businesses for 'protection' money."
    
    menu:
        
        "Send the fleet!":
            
            $ reputation+=20
            $ show_reputation=True
            $ fleet-=20
            $ show_fleet=True  
            
            c "Yes %(title)s %(player_name)s, we'll stop their 'business' practices right away."
            
        "Leave them alone if they send in a cut of their payments.":
            
            $ reputation-=30
            $ show_reputation=True
            $ credits+=30
            $ show_credits=True 
            
            c "If word of this gets out, the people will hate you, %(title)s."
            
    jump base_travel_events
    
label warF:
    
    if war == 0:
        
        c "Warships are advancing from planet Geddon. They're heading straight our way. What should we do?"
    
        menu:
        
            "Prepare to fight.":
        
                $ reputation+=10
                $ show_reputation=True
                $ credits-=30
                $ show_credits=True 
                $ tech-=30
                $ show_tech=True
                $ fleet-=30
                $ show_fleet=True
                
                $ war = 1
            
                c "The war will be expensive, but we'll try our best to protect %(player_colony)s, %(title)s %(player_name)s."
                
            "Welcome them.":
            
                $ reputation-=10
                $ show_reputation=True
                
                $ war = 2
            
                c "We'll try to avoid all-out war."
            
        jump base_travel_events
        
    elif war == 1:
        
        c "We managed to win a skirmish against the Geddon, and capture one of their captains. My men desire their revenge for their fallen comrades. What shall we do with our enemies?"
        
        menu:
            
            "Release them.":
                
                $ reputation+=10
                $ show_reputation=True
                $ credits+=20
                $ show_credits=True 
                $ tech+=10
                $ show_tech=True
                $ fleet-=10
                $ show_fleet=True
                $ title = "Warlord"
                
                c "My men hate them, but if you insist, %(title)s %(player_name)s."
                l "People have started calling you %(title)s since you ended the war."
                
            "Kill them.":
                
                $ reputation+=20
                $ show_reputation=True
                $ credits+=20
                $ show_credits=True 
                $ tech+=10
                $ show_tech=True
                $ fleet+=10
                $ show_fleet=True
                $ title = "Warlord"
                
                c "My men will appreciate the chance for revenge."
                l "People have started calling you %(title)s since you ended the war."
                
        jump base_travel_events
        
    elif war == 2:
        
        c "The Geddon sent us terms for our surrender, and it's pretty brutal. They've already boxed in our fleet, so fighting is no longer an option. Should we accept their terms?"
        
        menu:
            
            "Accept the terms.":
                
                $ reputation-=20
                $ show_reputation=True
                $ credits-=30
                $ show_credits=True 
                $ tech-=20
                $ show_tech=True
                $ fleet-=20
                $ show_fleet=True
                
                $ war = 3
                
                c "It will limit our influence, but will save a few more lives for %(player_colony)s."
                
            "Reject the terms.":
                
                $ reputation+=10
                $ show_reputation=True
                $ credits-=20
                $ show_credits=True 
                $ tech-=20
                $ show_tech=True
                $ fleet-=30
                $ show_fleet=True
                
                $ war = 2
                
                c "A bold decision, but the Geddon will make the people suffer. It will buy us a little time... "
                
    elif war == 3:
            
        l "The Geddon are demanding that we send them tribute."
            
        menu:
                
            "Credits.":
                    
                $ reputation-=10
                $ show_reputation=True
                $ credits-=20
                $ show_credits=True 
                
                l "The people are calling you a coward for not fighting them..."
                
            "War ships":
                    
                $ reputation-=10
                $ show_reputation=True
                $ fleet-=20
                $ show_fleet=True 
                
                l "The people are calling you a coward for not fighting them..."
                    
                
        jump base_travel_events
        
                
label weaponF:
    
    c "Our fleet is ill-equipped. We should spend to improve our weapons."
    
    menu:
        
        "Yes.":            
        
            $ credits-=10
            $ show_credits=True 
            $ tech+=10
            $ show_tech=True
            $ fleet+=30
            $ show_fleet=True
            
            c "I will inform the science division immediately!"
            
        "No.":
            
            $ fleet-=10
            $ show_fleet=True
            
            c "I hope we're prepared enough to defend %(player_colony)s..."
            
    jump base_travel_events
    
label wagesF:
    
    c "You should pay the soldiers of our fleet more. It will attract more recruits."
    
    menu:
        
        "Yes.":
            
            $ credits-=10
            $ show_credits=True 
            $ fleet+=30
            $ show_fleet=True
            
            c "Good, that makes my job easier."
            
        "No.":

            $ fleet-=10
            $ show_fleet=True
            
            c "I hope we'll have enough resources to defend %(player_colony)s..."
            
    jump base_travel_events
    
            
label taxesCE:
    
    e "%(title)s %(player_name)s, the taxes are too high for the people of %(player_colony)s. Please lower them slightly."
    
    menu:
        
        "Yes.":
            
            $ credits-=20
            $ show_credits=True 
            $ reputation+=30
            $ show_fleet=True
            
            e "The people are most grateful. Thank you, %(title)s."
            
        "No.":
            
            $ credits+=10
            $ show_credits=True 
            $ reputation-=10
            $ show_fleet=True
            
            e "Well, I tried."
            
    jump base_travel_events
    
    
label investmentC:
    
    if investment == 0:
    
        e "Entrepreneurs from Lumines have taken an interest in our colony %(player_colony)s for its natural salt content. They want a loan of credits and promise to pay you back when their salt business profits."
    
        menu:
        
            "Give them 50 credits.":
            
                $ credits-=50
                $ show_credits=True 
                $ reputation+=10
                $ show_reputation=True
                $ investment = 1
            
                e "They will make good use of the money."
                
            "Not right now.":
                
                $ reputation-=10
                $ show_reputation=True
                
                e "They'll be unhappy to have traveled far without cause."
                
        jump base_travel_events
            
    elif investment == 1:
        
        e "The entrepreneurs have sent in part of their profits."
       
        menu:
            
            "Good.":
                
                $ credits+=20
                $ show_credits=True 
                
                e "Their business seems to be doing well."
                
            "Keep it.":
                
                $ reputation+=20
                $ show_reputation=True 
                
                e "They were astounded by your generosity, %(title)s %(player_name)s."
                
        jump base_travel_events
        
label festivalR:
    
    e "The people of %(player_colony)s work extremely hard. Let's throw a huge party so they can relax."
    
    menu:
        
        "Yes.":
            
            $ credits-=20
            $ show_credits=True 
            $ reputation+=30
            $ show_reputation=True
            
            e "Let's get down and funky!"
            e "Sorry, I got excited."
            
        "Get back to work!":
            
            $ reputation-=20
            $ show_reputation=True
            
            e "All work and no play..."
            
    jump base_travel_events
            
label clonesT:
    
    if clone == 0:
        
        m "We could create clones to minimize daily workload, improve our medical technology, and fight our wars."
    
        menu:
        
            "Let's build a clone army!":
            
                $ reputation-=10
                $ show_reputation=True
                $ credits-=20
                $ show_credits=True 
                $ tech+=30
                $ show_tech=True
                $ fleet+=20
                $ show_fleet=True
                $ clone = 1
                
                m "The best part is there's absolutely no risk involved."
                
            "Let's not.":
                
                $ reputation-=10
                $ show_reputation=True
                
                m "There's no risk involved and it's incredibly convenient. Think about it some more, okay?"
                
        jump base_travel_events
        
    elif clone == 1:
        
        m "The clones we created have extremely short life spans. We should research how to make more."
        
        menu:
            
            "Sure.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits-=10
                $ show_credits=True 
                $ tech+=20
                $ show_tech=True
                $ fleet+=20
                $ show_fleet=True
                $ clone = 2
                
                m "We'll have so many clones that no one will dare to attack us!"
                
            "Don't we have enough?":
                
                $ reputation+=10
                $ show_reputation=True
                
                m "There's no such thing as too many clones."
                
        jump base_travel_events
                
    elif clone == 2:
        
        m "I'm here to drop off your yearly batch of clones."
        
        menu:
            
            "Okay.":
                
                $ tech+=20
                $ show_tech=True
                $ fleet+=20
                $ show_fleet=True
                $ title = "Clone Master"
                
                m "I'll be back after we make some more."
                l "People are really impressed with your clone army. They've started calling you %(title)s."
                
                
            "Okay?":
                
                $ tech+=20
                $ show_tech=True
                $ fleet+=20
                $ show_fleet=True
                $ title = "Clone Master"
                
                m "I'll be back after we make some more."
                l "People are really impressed with your clone army. They've started calling you %(title)s."
                
        jump base_travel_events

label diseaseO:
    
    if disease == 0:
        
        e "Some of the colonists contracted a virus previously thought extinct in the universe. What should we do?"
        
        menu:
            
            "Send our best doctors.":
                
                $ credits-=20
                $ show_credits=True
                $ tech-=20
                $ show_tech=True
                $ fleet-=10
                $ show_fleet=True
                $ disease = 1
                
                e "I hope they can stop the virus..."
            
            "Quarantine the area.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits-=10
                $ show_credits=True
                $ fleet-=10
                $ show_fleet=True
                $ disease = 1
                
                e "We'll try to minimize its effect..."
                
        jump base_travel_events
        
    elif disease == 1:
        
        e "Despite our best efforts, the virus is evolving and hitting more people."
        
        menu:
            
            "Devote a significant resources to research how to stop it.":
                
                $ reputation+=10
                $ show_reputation=True
                $ credits-=30
                $ show_credits=True
                $ tech-=30
                $ show_tech=True
                $ fleet-=30
                $ show_fleet=True
                $ disease = 0
                
                e "We were able to stamp out the virus. The people should be okay now."
                
            "Quarantine the area.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits-=10
                $ show_credits=True
                $ fleet-=10
                $ show_fleet=True
                
                e "We slowed its progress, but people will keep dying at this rate."
                
        jump base_travel_events
            
label vigilanteO:
    
    if vigilante == 0:
    
        c "A vigilante has started taking the law into their own hands. People love them, but we should put up a bounty and stop them."
        
        menu:
            
            "Put up a bounty.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits-=20
                $ show_credits=True
                $ fleet+=10
                $ show_fleet=True
                $ vigilante = 1
                
                c "People should know that our law is the only law."
                
            "It's whatever.":
                
                $ reputation+=10
                $ show_reputation=True
                $ fleet-=10
                $ show_fleet=True
                
                c "Do you realize how hard it is to keep discipline in the fleet when there's heroes running around loose?"
                
        jump base_travel_events
        
    elif vigilante == 1:
        
        c "We managed to capture that vigilante. I'd like to make an example of her."
            
        menu:
                
            "Just lock her up.":
                    
                $ reputation-=10
                $ show_reputation=True
                $ fleet-=20
                $ show_fleet=True
                $ vigilante = 0
                
                c "I'll try to contain myself, then."
                
            "Do whatever you want.":
                
                $ reputation-=30
                $ show_reputation=True
                $ fleet+=20
                $ show_fleet=True
                $ vigilante = 0
                
                c "Breaking rules has consequences."
                
        jump base_travel_events
                  
    
        
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