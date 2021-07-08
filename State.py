import EventHandler
import pygame
import Shapes
import Button
import Text
import ShapeRect
from PositionalVectors import Vector2
import ShapeRectBorder

mainMenu = 1
settingsMenu = 2
creditsMenu = 3
graphingMenu = 4





class State():

    # Checks the current state then changes the objects in Shape accordingly
    def renderCurrentState(self):
        if self.currentState == mainMenu:
            self.mainMenu()

        elif self.currentState == settingsMenu:
            self.settingsMenu()

        elif self.currentState == creditsMenu:
            self.rollCredits()

        elif self.currentState == graphingMenu:
            self.graphingMenu()

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

    # Creates the basic home screen, called at the start of the program
    def mainMenu(self):
        Shapes.clearAll()

        # Background
        Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (71, 121, 201)))

        # Close Program Button

        closeProgramButton = Button.Button(Vector2(40,40),Vector2(200,60),[175,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5), 30)
        closeProgramButton.addOnClickedCall(EventHandler.closeProgram)
 
        # Setting Button
        settingsButton = Button.Button(Vector2(1000,40),Vector2(150,60),[75,75,75],5,[0,0,0], "Settings",[0,0,0], Vector2(15,5), 30)
        settingsButton.addOnClickedCall( lambda : self.changeState(settingsMenu))

        # Start Button
        startButton = Button.Button(Vector2(390,330),Vector2(500,120),[28, 165, 179],5,[0,0,0], "Start Program",[0,0,0], Vector2(5,5), 70)
        startButton.addOnClickedCall( lambda : self.changeState(graphingMenu))

        # Credits Buttonin
        creditsButton = Button.Button(Vector2(580,530),Vector2(120,60),[125,125,125],5,[0,0,0], "Credits",[0,0,0], Vector2(5,5), 30)
        creditsButton.addOnClickedCall( lambda : self.changeState(creditsMenu))

    def settingsMenu(self):
        Shapes.runLoop = False

        Shapes.clearAll()

        # Background
        Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (75, 75, 75)))

        # Close Program Button
        closeButton = Button.Button(Vector2(40,40),Vector2(200,60),[150,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5), 30)
        closeButton.addOnClickedCall(EventHandler.closeProgram)

        # Back Button
        backButton = Button.Button(Vector2(40,600),Vector2(75,60),[150,150,150],5,[0,0,0], "Back",[0,0,0], Vector2(5,5), 30)
        backButton.addOnClickedCall(self.stepBackAState)


    def rollCredits(self):
        Shapes.clearAll()
        # Background
        Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (0, 0, 0)))

        # Close Program Button
        closeButton = Button.Button(Vector2(40,40),Vector2(200,60),[150,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5), 30)
        closeButton.addOnClickedCall(EventHandler.closeProgram)

        # Back Button
        backButton = Button.Button(Vector2(40,600),Vector2(75,60),[150,150,150],5,[0,0,0], "Back",[0,0,0], Vector2(5,5), 30)
        backButton.addOnClickedCall(self.stepBackAState)


        # Setting Button
        settingsButton = Button.Button(Vector2(1000,40),Vector2(150,60),[75,75,75],5,[0,0,0], "Settings",[0,0,0], Vector2(15,5), 30)
        settingsButton.addOnClickedCall( lambda : self.changeState(settingsMenu))

        # Adding the credits
        Shapes.text.append(Text.textInformation(Vector2(300,300),(175,175,175),"Credits : Kevin Sandberg, Main Programmer",30))
        Shapes.text.append(Text.textInformation(Vector2(300,340),(175,175,175),"Credits : RobertTeaches, Debugger",30))

    def graphingMenu(self):
        Shapes.runLoop = False

        Shapes.clearAll()
        # Background
        Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (180, 180, 180)))

        # Close Program Button
        closeProgram = Button.Button(Vector2(40,40),Vector2(200,60),[150,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5), 30)
        closeProgram.addOnClickedCall(EventHandler.closeProgram)

        # Back Button
        backButton = Button.Button(Vector2(40,600),Vector2(75,60),[150,150,150],5,[0,0,0], "Back",[0,0,0], Vector2(5,5), 30)
        backButton.addOnClickedCall(self.stepBackAState)


        # Setting Button
        settingsButton = Button.Button(Vector2(1000,40),Vector2(150,60),[75,75,75],5,[0,0,0], "Settings",[0,0,0], Vector2(15,5), 30)
        settingsButton.addOnClickedCall( lambda : self.changeState(settingsMenu))

        # Graphing Rectangle
        Shapes.borderRectangles.append(ShapeRectBorder.RectBorder(Vector2(290,240),Vector2(800,400),[190,190,190],10,[0,0,0]))

        # Inputs for graphing

state = State()



