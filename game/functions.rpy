init python:
    #Event management functions
    Events = dict()
    def clearEvents():
        global Events
        Events = dict()
        return
    def registerEvent(id, label, weight):
        global Events
        Events[id] = [weight, label]
        return True
    def unregisterEvent(id):
        global Events
        if id in Events:
            del Events[id]
        return
    def chooseRandomEvent():
        global Events
        totalWeight = 0
        for id, event in Events.items():
            totalWeight += event[0]
        randomVal = renpy.random.randint(1, totalWeight)
        totalWeight = 0
        for id, event in Events.items():
            totalWeight += event[0]
            if randomVal <= totalWeight:
                return event[1]
        return False
    #Event content functions
    def addReputation(amount):
        global reputation
        reputation += amount
        global show_reputation
        show_reputation = True
        return
    def addCredits(amount):
        global credits
        credits += amount
        global show_credits
        show_credits = True
        return
    def addTech(amount):
        global tech
        tech += amount
        global show_tech
        show_tech = True
        return
    def addFleet(amount):
        global fleet
        fleet += amount
        global show_fleet
        show_fleet = True
        return
