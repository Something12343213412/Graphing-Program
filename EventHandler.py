import pygame
import Shapes
import Button
import Text
import ShapeRect
from PositionalVectors import Vector2
import ShapeRectBorder
import State

ProgramStarted = []
ProgramClose = []

GraphingMenuOpened = []
SettingMenuOpened = []
MainMenuOpened = []
GraphingMenyClosed = []
SettingsMenuClosed = []
MainMenuClosed = []

GraphStarted = []
GraphCompleted = []

def closeProgram():
    pygame.quit()



def testEvent():
    print("test")

    





    
#def returnToHome():
    #mainMenu()
    
def linkToEvent(event : int):
    if event == 0:
        testEvent()

    if event == 1:
        closeProgram()

    if event == 2:
        mainMenu()

    if event == 3:
        rollCredits()

    if event == 4:
        returnToHome()

    if event == 5:
        settingsMenu()

    if event == 6:
        graphingMenu()