mainMenu = 1
settingsMenu = 2
creditsMenu = 3
graphingMenu = 4


class State():
    
    def __init__(self):
        self.currentState = mainMenu
        self.previousStates = [mainMenu]

    def changeState(self, newState):
        self.previousState.append(self.currentState)
        self.currentState = newState

    def stepBackAState(self):
        self.currentState = self.previousStates[-1]
        self.previousStates.pop(-1)


