init python:
    # Event management functions
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
    # Event content functions
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

    # Quest functions
    TemporaryQuests = dict()
    PersistentQuests = dict()
    def clearQuests():
        global TemporaryQuests
        TemporaryQuests = dict()
        return
    # string id: arbitrary, not shown to the player. Use to override or unregister.
    # string text: quest text to show in the quest log.
    # string[] conditions: a set of conditions to evaluate, such as ["FleetRatio() > 0.75", "TechRatio() > 0.75"].
    # string callback: Label to call once the quest is complete. Note: This should end with a RETURN, not a JUMP.
    # bool isPersistent: Whether the quest lasts between playthroughs.
    def registerQuest(id, text, conditions, callback, isPersistent):
        quest = [text, conditions, callback]
        if isPersistent:
            global PersistentQuests
            PersistentQuests[id] = quest
        else:
            global TemporaryQuests
            TemporaryQuests[id] = quest
        return
    def unregisterQuest(id):
        global TemporaryQuests
        if id in TemporaryQuests:
            del TemporaryQuests[id]
        global PersistentQuests
        if id in PersistentQuests:
            del PersistentQuests[id]
        return
    def checkQuests():
        for id, quest in TemporaryQuests.items():
            checkQuest(id, quest)
        for id, quest in PersistentQuests.items():
            checkQuest(id, quest)
        return
    def checkQuest(id, quest):
        for condition in quest[1]:
            if not eval(condition):
                return
        # If all conditions pass, quest is complete.
        unregisterQuest(id)
        renpy.call(quest[2])
        return

    # Resource ratio helper functions
    # Because these are all ints, and division floors by default, these helper functions will get around that.
    def ReputationRatio():
        return (reputation * 1.0) / max_reputation
    def CreditRatio():
        return (credits * 1.0) / max_credits
    def TechRatio():
        return (tech * 1.0) / max_tech
    def FleetRatio():
        return (fleet * 1.0) / max_fleet