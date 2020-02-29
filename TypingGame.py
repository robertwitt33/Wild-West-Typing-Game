import pygame
import random
import string

pygame.init()

# Creating the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Image imports
house = pygame.image.load("Graphics\WesternHouse.jpg")
target = pygame.image.load("Graphics\Circle.png")
shotty = pygame.image.load("Graphics\Shotgun.png")
muzzle = pygame.image.load("Graphics\MuzzleFlash.png")
shot = pygame.image.load("Graphics\Shot.png")
cowboy = pygame.image.load("Graphics\Cowboy.png")
bubble = pygame.image.load("Graphics\Bubble.png")

# Title and icon
pygame.display.set_caption("Wild West Typing!")
icon = pygame.image.load("Graphics\TypingIcon.png")
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

# Text font
font = pygame.font.Font("freesansbold.ttf", 32)

# Target coordinates, these two values should change when the new word appears
textX = 170
textY = 450

# Current word that we are typing. It has an indexed version as well so we can update as we type
currentWord = " "
OGword = " "
indexedWord = list(currentWord)
currentLength = len(indexedWord)
lengthTracker = 0
starttrack = 0  # used to have the intro screen only appear at the begininning

# Random words (This can be changed to any list of words)
words = [
    "supreme",
    "throne",
    "thrill",
    "long",
    "size",
    "hair",
    "plan",
    "nauseating",
    "pull",
    "cagey",
    "berserk",
    "balance",
    "previous",
    "ship",
    "phone",
    "icky",
    "balance",
    "private",
    "hysterical",
    "ashamed",
    "bike",
    "sun",
    "better",
    "early",
    "glow",
    "chase",
    "verse",
    "stale",
    "point",
    "milky",
    "futuristic",
    "cushion",
    "clam",
    "wait",
    "flesh",
    "peaceful",
    "limit",
    "bat",
    "wound",
    "beg",
    "odd",
    "cave",
    "authority",
    "wink",
    "apparel",
    "settle",
    "debonair",
    "turn",
    "slip",
    "seal",
]

# Scoreboard
score = 0
scoreboard = "Words typed: " + str(score)

# All of the functions used in the program


def printer(x, y):
    """ Presents the text onto the screen."""
    show = font.render(currentWord, True, (255, 0, 100))
    screen.blit(show, (x, y))


def updatescore(scoreboard):
    """ Updates the score"""
    show = font.render((scoreboard), True, (0, 0, 0))  # pygame surface string
    screen.blit(show, (525, 10))


def intro():
    """ Lays out everything for the starting screen"""
    CX = 350
    show1 = font.render(("YEEEE HAWWW!"), True, (0, 0, 0))  # pygame surface string
    show2 = font.render(("Press SPACEBAR"), True, (0, 0, 0))  # pygame surface string
    show3 = font.render(("to start typin!"), True, (0, 0, 0))  # pygame surface string
    screen.blit(show1, (75, 90))
    screen.blit(show2, (70, 125))
    screen.blit(show3, (80, 160))
    screen.blit(cowboy, (CX, 80))
    screen.blit(bubble, (17, 0))


def randomString():
    """Generate a random string of fixed length """
    num = random.randrange(50)
    return words[num]


def randomCoordinates():
    """Generates random coordinates to use when spawning a new word in"""
    textX = random.randrange(550)
    textY = random.randrange(125, 350)
    return textX, textY


def correctLetter():
    """Eliminates the first letter of the word when the user is correct"""
    global textX
    global lengthTracker
    global indexedWord
    global currentWord
    del indexedWord[0]
    temp = ""  # stores the joined string
    currentWord = temp.join(indexedWord)
    lengthTracker += 1  # used to keep track of which letter the user is on


def wrongLetter():
    """When a letter is wrong, we want to restart and print out the original word."""
    global OGword
    global currentWord
    global OGindex
    global indexedWord
    global lengthTracker
    # reseting the word length
    currentWord = OGword
    indexedWord = OGindex.copy()
    lengthTracker = 0  # resets the letter tracker


# Loops through the game
tracker = True
while tracker:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tracker = (
                False  # This causes the While loop to evaluate False and exit the game
            )

        # This is tracking if a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "a":
                    correctLetter()
                else:
                    wrongLetter()

            # Each elif statement is for a certain letter on the keyboard
            elif event.key == pygame.K_b:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "b":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_c:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "c":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_d:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "d":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_e:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "e":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_f:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "f":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_g:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "g":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_h:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "h":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_i:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "i":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_j:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "j":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_k:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "k":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_l:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "l":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_m:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "m":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_n:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "n":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_o:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "o":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_p:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "p":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_q:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "q":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_r:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "r":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_s:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "s":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_t:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "t":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_u:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "u":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_v:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "v":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_w:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "w":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_x:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "x":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_y:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "y":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_z:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == "z":
                    correctLetter()
                else:
                    wrongLetter()

            elif event.key == pygame.K_SPACE:
                # if this key is pressed, we need to check if the  letter is the zero index
                if indexedWord[0] == " ":
                    correctLetter()

    screen.fill((65, 105, 225))
    screen.blit(house, (0, 0))
    printer(textX, textY)
    updatescore(scoreboard)
    if starttrack == 0:
        # This loop only occurs at the start of the game
        intro()
    if lengthTracker == currentLength:
        # this activates if the user types a whole word correctly
        IMAGE_TIME = 30
        if IMAGE_TIME > 0 and (starttrack != 0):
            screen.blit(muzzle, (220, 75))
            screen.blit(shot, (textX - 10, textY - 100))
            IMAGE_TIME -= 1
            score += 1
        starttrack += 1  # used to exit loading screen in the begining
        scoreboard = "Words typed: " + str(score)  # updates the scoreboard
        currentWord = randomString()  # choses a new word randomly
        OGword = currentWord  # this keeps the original random string
        indexedWord = list(currentWord)
        OGindex = indexedWord.copy()
        currentLength = len(indexedWord)
        lengthTracker = 0  # resets the tracker for the next word
        textX, textY = randomCoordinates()  # new target location
    if starttrack != 0:
        # this spawns shotgun and a new target
        screen.blit(target, (textX - 10, textY - 100))
        screen.blit(shotty, (250, 350))
    clock.tick(60)  # this is to control the length of the bullet muzzle flash
    pygame.display.update()

# Things to do in future possibly:
# word changes with cool sound effect, like a bullet firing
# word moves around screen
# randomly generates a word with a generator instead of a predisposed list
# add a starting menu with advanced options
# calculate words per minute
# Speed Letter Recognition game mode
# paragraph calculator that calculates words per minute
