init python:
    Events = dict()
    def clearEvents():
        global Events
        Events = dict()
        return
    def registerEvent(id, label, weight):
        global Events
        Events[id] = [weight, label]
        return True
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


