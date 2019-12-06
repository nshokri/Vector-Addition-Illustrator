import pygame

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Vector Calculator")

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode([screenWidth, screenHeight])
screen.fill([255, 255, 255])


creatingVector = False

#Classes
class Vector2d:

    def __init__(self, x1, y1, color):
        #Start Position
        self.x1 = x1
        self.y1 = y1
        #End Position
        self.x2 = None
        self.y2 = None
        #Color of line
        self.color = color
        
    def getVector(self):
        return [self.x2 - self.x1, self.y2 - self.y1]
    
#Functions
def drawVector(vector):
    coord1 = (vector.x1, vector.y1)
    coord2 = (vector.x2, vector.y2)
    pygame.draw.line(screen, vector.color, coord1, coord2, 5)

VectorList = []

run = True
while run:
    pygame.time.delay(60)

    #Clear screen
    screen.fill((255,255,255))
    
    #Draw Vectors
    for vector in VectorList:
        if vector.y2 != None:
            drawVector(vector)
            
    #Event tracker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:

            mousePos = pygame.mouse.get_pos()

            if creatingVector == False:
                creatingVector = True
                newVector = Vector2d(mousePos[0], mousePos[1], (0,0,0))
                VectorList.append(newVector)

            else:
                #Adding the x2, y2 components of Vector so the next click will create a new Vector
                creatingVector = False
                #The last Vector in the list is the current Vector always
                currentVector = VectorList[len(VectorList) - 1]
                currentVector.x2 = mousePos[0]
                currentVector.y2 = mousePos[1]

    keysPressed = pygame.key.get_pressed()
    
    #Checks to see if the 'c' key has been pressed
    if keysPressed[pygame.K_c]:
        #removes all vectors in the list
        VectorList.clear()
        #Resets the variable keeping track of whether or not a vector is being created
        creatingVector = False
        
    #Checks to see if the '1' key has been pressed
    elif keysPressed[pygame.K_1]:
        #Add up all the vectors (start position in middle of screen)
        initialX = screenWidth / 2
        initialY = screenHeight / 2
        SumOfVectors = Vector2d(initialX, initialY, (255,0,0))
        SumOfVectors.x2 = initialX
        SumOfVectors.y2 = initialY
        
        for vector in VectorList:
            SumOfVectors.x2 += vector.getVector()[0]
            SumOfVectors.y2 += vector.getVector()[1]
        #VectorList.clear()
        VectorList.append(SumOfVectors)

        #Move the vectors and stack them
        if (len(VectorList) >= 1):
#######################
            firstVector = VectorList[0]
            storeVector = firstVector.getVector()
            
            firstVector.x1 = initialX
            firstVector.y1 = initialY

            firstVector.x2 = firstVector.x1 + storeVector[0]
            firstVector.y2 = firstVector.y1 + storeVector[1]


            for i in range(1, len(VectorList) - 1):
                currentVector = VectorList[i].getVector()
                
                VectorList[i].x1 = VectorList[i - 1].x2
                VectorList[i].y1 = VectorList[i - 1].y2
                VectorList[i].x2 = VectorList[i].x1 + currentVector[0]
                VectorList[i].y2 = VectorList[i].y1 + currentVector[1]

       ########################## 

            
    pygame.display.update()


pygame.quit()



