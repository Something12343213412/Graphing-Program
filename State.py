import EventHandler


mainMenu = 1
settingsMenu = 2
creditsMenu = 3
graphingMenu = 4


class State():

    # Checks the current state then changes the objects in Shape accordingly
    def renderCurrentState(self):
        if self.currentState == mainMenu:
            EventHandler.mainMenu()

        elif self.currentState == settingsMenu:
            EventHandler.settingsMenu()

        elif self.currentState == creditsMenu:
            EventHandler.rollCredits()

        elif self.currentState == graphingMenu:
            EventHandler.graphingMenu()

    # Constructor
    def __init__(self):
        self.currentState = mainMenu
        self.previousStates = [mainMenu]
    
    # change state, 
    def changeState(self, newState):
        self.previousStates.append(self.currentState)
        self.currentState = newState
        self.renderCurrentState()

    # step backs a state
    def stepBackAState(self):
        print(self.previousStates)
        self.currentState = self.previousStates[-1]
        self.previousStates.pop(-1)
        self.renderCurrentState()

state = State()



