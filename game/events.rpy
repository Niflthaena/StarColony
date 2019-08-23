label miningwitheriumC:
    
    e "We've found a mine full of witherium on %(player_colony)s, a precious mineral traded throughout the galaxy. What luck!"
    
    menu:
        
        "I'm rich!":
            $ reputation-=20
            $ credits+=60
            
            e "..."
        
        "Share it with the people of %(player_colony)s.":
            $ reputation+=10
            $ credits+=10
            $ tech+=10
            $ fleet+=10
            
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
                $ registerEvent("expeditionF", "expeditionF", 200)
                
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
        $ registerEvent("expeditionF", "expeditionF", 100)
            
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
                
        $ registerEvent("aiT", "aiT", 300)
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
        
        l "The AI advocating for human rights has had an episode of violence. Some colonists and soldiers were killed, but we caught one of the robot rebels. What should we do with it?" (interact=False)
        
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
                $ robot = 5
                
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
                $ robot = 5
                
                l "I'll personally go and tell the scientists to get it right this time. Let's hope this is the last case of a robot uprising."
                l "People don't seem to like how we've been dealing with the robots. They've started calling you a %(title)s."
        
        $ registerEvent("aiT", "aiT", 400)
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
        
            
    elif robot == 5:
        
        l "There's still unrest about the robot uprising."
        
        menu:
            
            "Tell the people to chill out.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits-=10
                $ show_credits=True
                
                l "When will we find peace?"
            
            "Can't you do something about that.":
                
                $ reputation-=10
                $ show_reputation=True
                $ credits-=10
                $ show_credits=True
                
                l "I'm doing my best, but no one is happy with the outcome."
                
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
        
        $ registerEvent("warF", "warF", 200)
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
                $ registerEvent("warF", "warF", 300) 
                
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
    
        e "Entrepreneurs from Lumines have taken an interest in our colony %(player_colony)s for its natural salt content."
        e "They want a loan of credits and promise to pay you back when their salt business profits."
    
        menu:
        
            "Give them 50 credits.":
            
                $ credits-=50
                $ show_credits=True 
                $ reputation+=10
                $ show_reputation=True
                $ investment = 1
                $ registerEvent("investmentC", "investmentC", 300)
            
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
                
        $ registerEvent("investmentC", "investmentC", 300)
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
        
        m "We could create clones to minimize daily workload, improve our medical technology, and fight our wars. There's no downside!"
    
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
                $ registerEvent("clonesT", "clonesT", 300)
                
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
                $ registerEvent("clonesT", "clonesT", 400)
                
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
                
        $ registerEvent("clonesT", "clonesT", 600)
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
        
label pollution:
    
    e "There was an accident while extracting witherium and some of the waste polluted a nearby stream."
    e "If we don't act soon, the wildlife could become endangered." 
    
    menu:
        
        "Clean it.":
            
            $ reputation+=20
            $ show_reputation=True
            $ credits-=20
            $ show_credits=True
            
            e "Thank you. We should be able to continue our extractions without further incident."
            
        "I can't afford that...":
            
            $ reputation+=20
            $ show_reputation=True
            
            e "Many species of animals may die out as a result. We'll see where this leaves us in a few years..."
            
    jump base_travel_events
    
label embezzle:

    l "There was corruption in the Star Armada fleet, and one of the higher-ups was sending colony resources to fund his own ventures." 
    
    menu:
        
        "Send him jail.":
        
            $ reputation+=20
            $ show_reputation=True
            $ credits-=10
            $ show_credits=True
        
            l "Too bad he can't pay us back in prison."
            
        "Blackmail him.":
            
            $ reputation-=10
            $ show_reputation=True
            $ credits+=20
            $ show_credits=True
            
            l "He can stay in the fleet for now, at least until he pays back what he owes with interest."
            
    jump base_travel_events
    
label inflation:
    
    l "We're importing too many goods and our own merchants can't compete with their lower prices. If this continues, our market will collapse."
    
    menu:
        
        "Impose heavier tariffs.":
    
            $ reputation-=10
            $ show_reputation=True
            $ credits+=20
            $ show_credits=True
        
            l "We can use this as an opportunity to make more money until the market stabalizes."
        
        "Leave it.":
            
            $ reputation+=10
            $ show_reputation=True
            $ credits-=20
            $ show_credits=True
            
            l "The merchants will be happy, but it will hurt our economy in the long term."
            
    jump base_travel_events
    
label immigrants:
    
    e "We have too many people interested in coming to %(player_colony)s! We should build more to accomodate them." 
    
    menu:
        
        "Build it up!":
            
            $ reputation+=10
            $ show_reputation=True
            $ credits-=20
            $ show_credits=True
            $ fleet+=10
            $ show_fleet=True
            $ tech+=10
            $ show_tech=True
            
            e "They have settled in quite well. Some have taken jobs in the Star Armada and Science Division."
        
        "Turn them away.":
            
            $ reputation-=20
            $ show_reputation=True
            
            e "They came from across the galaxy, but we'll have to send them back."
            
    jump base_travel_events
    
label storm:
    
    e "A terrible storm wrecked many of the colonists' homes. We just need some extra hands to help with construction." 
    
    menu:
        
        "Send soldiers to help with construction.":
            
            $ reputation+=20
            $ show_reputation=True
            $ fleet-=10
            $ show_fleet=True
            
            e "Thank you. We will be able to get this work done much faster."
            
        "Tough it up, buttercup!":
        
            $ reputation-=20
            $ show_reputation=True
            
            e "It is going to be a long road to recovery."
            
    jump base_travel_events
    
label fauna:
    
    m "We've discovered a new kind of carnivorous plant, unique to %(player_colony)s. I bet we could cultivate it to destroy our enemies!" 
    
    menu:
        
        "Unleash the plants!":
            
            $ reputation-=20
            $ show_reputation=True
            $ fleet+=10
            $ show_fleet=True
            $ tech+=10
            $ show_tech=True
            
            m "Yes, yes! We will create an army of plants!"
            
        "Sounds dangerous.":
            
            $ reputation+=10
            $ show_reputation=True
            $ tech-=10
            $ show_tech=True
            
            m "Bah, don't be confined by what your people say. This could have been a great opportunity."
            
    jump base_travel_events