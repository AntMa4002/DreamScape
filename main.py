import pygame, sys, random, time

pygame.init()
clock = pygame.time.Clock()

#Game Window
w = 800
h = 550
windowSize = (w, h)
screen = pygame.display.set_mode(windowSize)

#Colours
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
OUTLINE = (0)

#introduction screen
def intro():
  intro = True
#The intro variable will always be True unless the player clicks on one of the buttons which will result in the variable becoming false.
  while intro:
    font1 = pygame.font.SysFont("Myriad pro" , 100)    

    mousePosition = pygame.mouse.get_pos()
    x, y = mousePosition

    screen.fill(BLACK)

    startButton = font1.render("Start", 1, BLACK, GREEN)
    exitButton = font1.render("Exit", 1, BLACK, RED)
    instructionsButton = font1.render("Instructions", 1, BLACK, WHITE)
    titleButton = font1.render("DreamScape Survival", 1, BLACK,BLUE)

    startButton_size = startButton.get_size()
    exitButton_size = exitButton.get_size()
    instructionsButton_size = instructionsButton.get_size()
    titleSize = titleButton.get_size()

    title = screen.blit(titleButton, (w/2 - titleSize[0]/2, 25))
    start = screen.blit(startButton, (w / 2 - startButton_size[0] / 2, 150))
    exit = screen.blit(exitButton, (w / 2 - exitButton_size[0] / 2, 275))
    instructions = screen.blit(instructionsButton, (w / 2 - instructionsButton_size[0] / 2, 400))
    pygame.display.update()

#This section of code is used to render the text boxes with their respective fonts, colour, positioning, and size. it is also where the mouse position will be recorded

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN: 
        if event.type == pygame.QUIT:
          sys.exit()
        if start.collidepoint(mousePosition):  # If the user clicks on start
          intro = False
          gameLoop()
        if exit.collidepoint(mousePosition):  # If the user clicks on exit
          sys.exit("Thanks for playing! Come back next time!")
        if instructions.collidepoint(mousePosition):  # If the user clicks on the instructions button
          intro = False
          instruction()

#This section of code uses the event.type function in a for loop to check if the mouse button is being clicked which will then check if the mouse position is collding with one of the buttons using the collidepoint functon and will result in one of the other screens appearing including the gameloop, instruction screen, or exiting the entire game

#Loss scene
def GameOver(score):
  font1 = pygame.font.SysFont("Myriad pro" , 112)
  font2 = pygame.font.SysFont("Myriad pro" , 90)
  gameOver = font1.render("GAME OVER." , 1, (RED))
  finalScore = font2.render("Final score: " + str(score), 1, (RED))

  scoreSize = finalScore.get_size()
  glsize = gameOver.get_size()

  x1 = w/2 - glsize[0]/2
  y1 = h/2 - glsize[1]/2
  x2 = w/2 - scoreSize[0]/2
  y2 = h/2 + scoreSize[1]/2

  screen.blit(gameOver, (x1, y1))
  screen.blit(finalScore, (x2, y2))
  pygame.display.update()
  time.sleep(4)
  intro()

#This section of code is used for when the player encounters a loss which then freezes the screen for 4 seconds using the time.sleep() function but also render 2 pieces of text including the GAME OVER text and the Final score that the player had before losing which is found using a parameter

#Win screen
def GameWon(score):
  font1 = pygame.font.SysFont("Myriad pro" , 112)
  font2 = pygame.font.SysFont("Myriad pro" , 90)
  gameWon = font1.render("GAME WON!" , 1, (GREEN))
  finalScore = font2.render("Final score: " + str(score), 1, (GREEN))

  scoreSize = finalScore.get_size()
  gwsize = gameWon.get_size()

  x1 = w/2 - gwsize[0]/2
  y1 = h/2 - gwsize[1]/2
  x2 = w/2 - scoreSize[0]/2
  y2 = h/2 + scoreSize[1]/2

  screen.blit(gameWon, (x1, y1))
  screen.blit(finalScore, (x2, y2))
  pygame.display.update()
  time.sleep(4)
  intro()

#This section is virutally the same as the loss screen but instead the Game over text is replaced with game won and the text colour is replaced with green instead of red

#intructions
def instruction():
  instruction = True
  while instruction:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        instruction = False
        intro()

#This section of code will check if the mouse button is being clicked which will result in either the intro screen appearing or the program exiting

    screen.fill(BLACK)

    font1 = pygame.font.SysFont("Myriad pro" , 100)
    font2 = pygame.font.SysFont("Myriad pro" , 33)

    title = font1.render("Instructions", 1, (WHITE))
    txt1 = font2.render("You are in a dream, your goal is to escape this place and wake up.", 1, (BLUE))
    txt2 = font2.render("Press the left and right arrow keys to move and up to jump.", 1, (BLUE))
    txt3 = font2.render("Dodge incoming blocks to score points.", 1, (BLUE))
    txt4 = font2.render("Scoring 50 points results in a win and an escape from the DreamScape.", 1, (BLUE))
    txt5 = font2.render("If you get hit you will gradually lose health and die resulting in a loss.", 1, (BLUE))
    back = font2.render("Click anywhere to go back", 1, (WHITE))

    titleSize = title.get_size()
    txt1Size = txt1.get_size()
    txt2Size = txt2.get_size()
    txt3Size = txt3.get_size()
    txt4Size = txt4.get_size()
    txt5Size = txt5.get_size()
    backSize = back.get_size()

    screen.blit(title, (w/2 - titleSize[0]/2, 0))
    screen.blit(txt1, (w/2 - txt1Size[0]/2, 100))
    screen.blit(txt2, (w/2 - txt2Size[0]/2, 130))
    screen.blit(txt3, (w/2 - txt3Size[0]/2, 160))
    screen.blit(txt4, (w/2 - txt4Size[0]/2, 190))
    screen.blit(txt5, (w/2 - txt5Size[0]/2, 220))
    screen.blit(back, (w-backSize[0], h-backSize[1]))

    pygame.display.update()

#This section of code renders all of the text in the instruction screen including the fonts, the texts, the size function and the bliting of the text all seperated into categories by numerical order

#Total score
def totalScore(count):
  font = pygame.font.SysFont("Myriad pro", 25)
  score = font.render("Score: " + str(count) , 1, (GREEN))
  scoreSize = score.get_size()
  screen.blit(score, (w - scoreSize[0],0))

#This function is used to total the score (The score being the amount of times a block exits the screen) and render it into the top right corner of the screen using the count parameter

#Number of HP
def totalHealth(num):
  font = pygame.font.SysFont("Myriad pro", 25)
  hp = font.render("HP: " + str(num) , 1, (RED))
  screen.blit(hp, (0,0))

#This function is used to total the health points of the player and render it into the top left corner of the screen using the num parameter

#The Game loop
def gameLoop():

  #Player physics
  GROUND = h
  onPlat = False
  RUN_SPEED = 12
  JUMP_SPEED = -28
  GRAVITY = 2
  chVx = 0
  chVy = 0

  #Player characteristics
  character = pygame.image.load("images/ch1.png")
  chRect = character.get_rect()
  chW = chRect.width
  chH = chRect.height 
  chX = w/2 - chW/2
  chY = h - chH

#Player images and animation
  chPicNum = 1
  chDir = "left"
  chPic = [0]*6

  for i in range(6):
    chPic[i] = pygame.image.load("images/ch" + str(i) + ".png")

  nextLeftPic  = [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0]
  nextRightPic = [3, 4, 4, 4, 3, 4, 3, 4, 3, 3, 4, 4]

#Platform characteristics
  platformX1 = 25
  platformY1 = GROUND-180
  platformW1 = 250
  platformH1 = 20

  platformX2 = 525
  platformY2 = GROUND-180
  platformW2 = 250
  platformH2 = 20

  platformX3 = 275
  platformY3 = GROUND-385
  platformW3 = 250
  platformH3 = 20


#Drawing the platforms
  def drawplat():
    pygame.draw.rect(screen,WHITE,(platformX1,platformY1,platformW1,platformH1),OUTLINE)
    pygame.draw.rect(screen,WHITE,(platformX2,platformY2,platformW2,platformH2),OUTLINE)
    pygame.draw.rect(screen,WHITE,(platformX3,platformY3,platformW3,platformH3),OUTLINE)

#Detecting the platforms
  def platform(obX, obY, obW, obH, platX, platY, platW, platH, vy):
    if obX + obW > platX and obX < platX + platW and obY + obH > platY and obY < platY + platH and vy > 0:
      return True
    else:
      return False

#Generating the blocks
  def generateRect(x,y,w,h,colour):
    return pygame.draw.rect(screen, colour, [x, y, w, h])


#Block 1 characteristics (Vertical)
  rectWidth1 = 100
  rectHeight1 = 100
  rectStartx1 = random.randrange(0, w - rectWidth1)
  rectStarty1 = -300
  rectSpeed1 = 8 

#Block 2 characteristics (Vertical)
  rectWidth2 = 200
  rectHeight2 = 200
  rectStartx2 = random.randrange(0, w - rectWidth2)
  rectStarty2 = -300
  rectSpeed2 = 9 

#Block 3 characteristics (Horizontal)
  rectWidth3 = 150
  rectHeight3 = 150
  rectStartx3 = 700
  rectStarty3 = random.randrange(0, h - rectHeight3)
  rectSpeed3 = 9 

#Health and Score counters
  health = 100
  score = 0

  inPlay = True

  while inPlay:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: 
        sys.exit() 
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      if chY + chH == GROUND or onPlat == True:
        chVy = JUMP_SPEED
      if chDir == "left":          
        chPicNum = 2         
      elif chDir == "right":       
        chPicNum = 5  
    if keys[pygame.K_LEFT]:
      chVx = -RUN_SPEED
      chDir = "left"
      if chY == GROUND - chH or onPlat == True:
        chPicNum = nextLeftPic[chPicNum]
    elif keys[pygame.K_RIGHT]:
      chVx = RUN_SPEED
      chDir = "right"
      if chY == GROUND - chH or onPlat == True:
        chPicNum = nextRightPic[chPicNum]
    else:
      chVx = 0
      if chDir == "left":          
        chPicNum = 0           
      elif chDir == "right":       
        chPicNum = 3

#This section of code is used for the character movement including the left, right, and up buttons which result in the character moving along with animation both on ground or on a platform. This section also accounts for the value of the velocity as well as the direction the player is facing

    chX += chVx

    chVy += GRAVITY
   
    chY += chVy

#This section of code is used to update the horizontal and vertical velocity, and gravity

    if chY + chH >= GROUND:
      chY = GROUND - chH
      chVy = 0
    elif chY < 0:
      chY = 0

    if chX + chW >= w:
      chX = w - chW
    elif chX < 0:
      chX = 0
  
#This section of code is used as the boundaries for the player so that they don't disappear into the screen horizontally and vertically

    screen.fill(BLACK)
    screen.blit(chPic[chPicNum], (chX, chY))

    drawplat()

#This section of code is used to fill the screen and draw both the image files and the platforms using drawplat()

  #Detected platforms
    platform1 = platform(chX, chY, chW, chH, platformX1, platformY1, platformW1, platformH1, chVy)
    platform2 = platform(chX, chY, chW, chH, platformX2, platformY2, platformW2, platformH2, chVy)
    platform3 = platform(chX, chY, chW, chH, platformX3, platformY3, platformW3, platformH3, chVy)

    if platform1:
      chY = platformY1 - chH
      chVy = 0
      onPlat= True
    elif platform2:
      chY = platformY2 - chH
      chVy = 0
      onPlat = True
    elif platform3:
      chY = platformY3 - chH
      chVy = 0
      onPlat = True
    else:
      onPlat = False

#This section of code is used to check if the player is on the platform and if onPlat is true, it will also allow the player to jump and move on the platform with animations

    chRect = pygame.Rect(chX,chY,chW,chH)

#This line replaces the chRect variable with the pygam.rect() using the characteristics of the player so that it can be used in the colliderect function

    block1 = generateRect(rectStartx1,rectStarty1,rectWidth1,rectHeight1,GREEN)
    rectStarty1 += rectSpeed1

#This section of code generates the first block

    if rectStarty1 > h: 
      rectStarty1 = 0 - rectHeight1 
      rectStartx1 = random.randrange(0, w - rectWidth2)
      score += 1
      if score == 5:
        rectSpeed1 += 1
    if block1.colliderect(chRect) == True:
      health -= 1

#This section of code checks if the block is off the screen which will change the y coordinate to make it appear from the top of the screen and the x coordinate will be randomized. The score variable will also increase by 1 each time the disappears and once the score hits 5, the speed of the block will increase. There is also an if statement using the colliderect function which will check if the 1st block is colliding with the character and if true, the health of the player will decrease by 1 point each time
    
    if score >= 5:
      block2 = generateRect(rectStartx2,rectStarty2,rectWidth2,rectHeight2,BLUE)
      rectStarty2 += rectSpeed2
      if rectStarty2 > h: 
        rectStarty2 = 0 - rectHeight2 
        rectStartx2 = random.randrange(0, w - rectWidth2)
        score += 1
      if block2.colliderect(chRect) == True:
        health -= 1

#This section of code is virtually the same as the previous section but is instead used for the 2nd block which is generated when the score reaches 5 so that the difficulty of the game increases overtime

    if score >= 15:
      block3 = generateRect(rectStartx3,rectStarty3,rectWidth3,rectHeight3,RED)
      rectStartx3 -= rectSpeed3
      if rectStartx3 < 0 - rectWidth3: 
        rectStartx3 = w + rectWidth3 
        rectStarty3 = random.randrange(0, h - rectHeight3)
        score += 1
      if block3.colliderect(chRect) == True:
        health -= 1
  
#This section of code differs from the previous two as not only is it for the 3rd block, but instead of falling down vertically, it moves horizontally so I switched out what would have been the y-coordinate, into the x-coordinate so that it would appear randomly on the x-axis from the right once it disapears on the left. This block also only appears once the score reaches 15 so that the player won't expect it

    totalScore(score)

#This is where the totalScore() function is used and takes the score variable as it's parameter

    totalHealth(health)

#This is where the totalHealth() function is used and takes the health variable as it's parameter

    if health <= 0:
      GameOver(score)
    
    if score >= 50:
      GameWon(score)

#This section of code is used for when either the player loses all of their health or reaches a score of 50 which will cause either the game over screen or the game won screen respectively

    pygame.display.update()
    clock.tick(30)
intro()
gameLoop()

#This is where the into() and gameloop() fucntions are implemented