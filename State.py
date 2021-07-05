import EventHandler


mainMenu = 1
settingsMenu = 2
creditsMenu = 3
graphingMenu = 4


class State():

    # Checks the current state then changes the objects in Shape accordingly
    def renderCurrentState():
        if currentState == mainMenu:
            EventHandler.startingEvent()

        elif currentState == settingsMenu:
            EventHandler.settingsMenu()

        elif currentState == creditsMenu:
            EventHandler.rollCredits()

        elif currentState == graphingMenu:
            EventHandler.graphingMenu()

    # Constructor
    def __init__(self):
        self.currentState = mainMenu
        self.previousStates = [mainMenu]
    
    # change state, 
    def changeState(self, newState):
        self.previousState.append(self.currentState)
        self.currentState = newState
        renderCurrentState(self.currentState)

    def stepBackAState(self):
        self.currentState = self.previousStates[-1]
        self.previousStates.pop(-1)

state = State()



