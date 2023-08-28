# Space-Invaders
Python Master Class
**Class 01: Install Python 3.x and PyCharm + First Python Program**
Download Python 3.x from here Download Python | Python.org then installs it according to the instructions in the installation window.  
Download PyCharm from here Download PyCharm: Python IDE for Professional Developers by JetBrains and install according to the installation instruction. Just remember to mark bin directory.
After installing the Pycharm, create a new project and write the code which is given below,
				print(“Hello World”)
You will see the printed result of your code in the program console.

**Class 02: Into to PyGame and Window Call **
PyGame: Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language. 
Making games is made easier because of this PyGame. We can easily call window, screen, sound and many more libraries using PyGame. 
Code: 
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
**Class 03: Adding Title, Logo and Background **
Using pygame’s library, we can add the title, logo and background of our console window. Here, as we are developing a Space Invaders game our title will be “SPACE INVADERS” and we will pick a logo from google. We will write the code outside the while loop as it will be one time implemented code.
Code:
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

After integrating the logo and title, we will add the background image. For that we have to download an image from google and draw it using blit syntax inside the loop and we need to update the window. 
Code:
	background = pygame.image.load('background.jpg')
	
	
After loading the image, now we are going to blit it inside the while loop.
screen.fill((0, 0, 0))
screen.blit(background, (0,0))


First, I have to define a background color using screen.fill((RGB Code)) and then we are going to blit the background image. For drawing the image we are going to use blit(image_name, (x,y)) here x,y are the coordinates of the window.
**Class 04: Adding images of the Player and giving the position of the player**
First, we have to download a player image then we are going to load the image and give it a position for display in the window. For that we are going to use the same library that we have used in icon and background and we are going to define the position together.
Code: 
player = pygame.image.load(‘plyaer.png’)
playerX= 370
playerY= 480

Now, we are going to make a function for player called player. 
	def player(x, y):
    	screen.blit(playerIMG, (x,y))


And in the main loop, we have to call the player function.
	player(playerX,playerY)

**Class 05: Player movement mechanism, keyboard event and adding boundaries.**
After declaring the player position, we are going to make the player move using a keyboard event. In python, event means doing some changes using any kind of actions like keyboard button press or moving the mouse. For that we have to give a moveable direction with a number of changes of quadrants. Like
	Code: 
	playerX_change = 0
Then we are going to tell python to change the direction when our button is being pressed. 
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        playerX_change = -0.3
    if event.key == pygame.K_RIGHT:
        playerX_change = 0.3


Here the event will start when any button will be pressed using event.type == pygame.KEYDOWN and then program will search for the pressed button identity. Then it will move the player using event.key.

if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0
When the button is up it means “No button pressed!” It will stop the player ship in the current position until any other button is being pressed.

For boundaries, we have to define the frame size using if loop,
if playerX <= 0:
    playerX = 0
elif playerX >= 736:
    playerX =736

Using this code, the player ship will not go out of the window. It will be inside the window size which is 800x600. 
**Class 06: Adding images of the enemy and movement (x,y)**
	For making it actionable, we have to add some enemies which will be the space invaders. Like player ship, we will 	add the enemy ship using the same method. 
	Code: 
enemyimg = pygame.image.load('enemy.png')
enemyX = 0
enemyY = 0
	
Then we will define the function for enemy using the same method def enemy()
	def enemy(x, y):
   	screen.blit(enemyimg, (x, y))


      then we are going to call this function inside the while loop using 
	enemy(enemyX, enemyY)


	
For moveable mechanism, we are going to create some more lines; 
First we are going to set 2 variables;
enemyX_change = 0.3
enemyY_change = 40

Then we are going to use;
 if enemyX <= 0:
    enemyX_change = 0.3
    enemyY += enemyY_change

elif enemyX >= 736:
    enemyX_change = -0.3
    enemyY += enemyY_change

enemyX += enemyX_change

Here if the enemy ship touches 0 of the X-axis it will change it’s direction by 0.3 to X and 40 to Y. and if it touches 736 of the X-axis, it will change it’s direction by -0.3 to X and 40 to Y. And it will change its X position regularly using enemyX += enemyX_change this code.



**Class 07: Creating Bullet, shooting mechanism and multiple bullet**
First, we have to load the bullet image here using the pygame package. Then we are going to give the bullet a position and make it READY for firing just to call it when we need. 
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_status = "ready"

Now we have to create a function so that we can call the action easily without making the code too complex. 
def fire_bullet(x,y):
global bullet_status
bullet_status = "fire"
screen.blit(bulletimg, (x, y - 10))

Here using global syntax, we are calling the bullet status after that we are drawing the bullet using screen.blit and setting up its position. We use y-10 here so that the bullet won’t overlay with the ship or doesn’t look like the bullet is coming from another place. 
Now let’s get into the firing mechanism event. We are going to fire the bullet using the space button. Whenever the space button is pressed, it will check for the availability of the bullet. If the bullet is “ready” it will start moving from bottom to top using the coordinate that was given in bulletX and bulletY. Here is going to call the fire_bullet()function. 
if event.key == pygame.K_SPACE:
    if bullet_status == "ready":
        bulletX = playerX
        fire_bullet(bulletX, bulletY)




After declaring the key event, we are going to define when the bullet will be ready to fire. 
if bulletY <= 0:
    bulletY = 480
    bullet_status = "ready"


After that we are going to declare that if the bullet status is “fire” then it will start shooting.
if bullet_status == "fire":
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change




**Class 08: Collision between the bullet and the enemy **
	
We have to create a function for collision which will define that when it will mark it as a collision. And we need to calculate the distance between the bullet and the enemy ship using the MATH package. So, first, we are going to import the math package. 


	import math
	def iscollision(enemyX, enemyY, bulletX,bulletY):
    dX = (math.pow((enemyX-bulletX),2))
    dY = (math.pow((enemyY-bulletY),2))
    distance = math.sqrt(dX + dY)
    if distance < 27:
        return True
    else:
        return False
	
Here in the collision function, we have used a mathematical equation which is called the distance between 2 coordinates  we have defined that if the distance between the bullet and enemy is less than 27. It will declare it as a collision.


After that we are going to define what will happen when there will be a collision. Call the function in the main loop. 


collision = iscollision(enemyX, enemyY, bulletX, bulletY)
if collision:
    bulletY = 480
    bullet_status = "ready"
    score += 1
    enemyX= 0
    enemyY = 0


here we have defined that whenever the collision will happen the enemy will respawn in their initial position and the bullet will also respawn and the bullet_status will become ready to fire.


**Class 09: Multiple Enemy**


As we have done the collision part now, we have to make multiple enemies so that we can have many enemies to shoot. For that we have to make an enemy list. In python, we use [ ] to make a list. So, in that case, I am going to make a list of all enemy variable like. 


                                     


And we have to bring all the enemy variables inside the for loop which will be inside the main while loop. And also we have to redefine the function for multiple enemies like 
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


Then we are going to make the for loop;


for i in range(number_of_enemy):
    if enemyX[i] <= 0:
        enemyX_change[i] = 0.2
        enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 736:
        enemyX_change[i] = -0.2
        enemyY[i] += enemyY_change[i]

    enemyX[i] += enemyX_change[i]

    collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_status = "ready"
        score += 1
        enemyX[i] = 0
        enemyY[i] = 0

    enemy(enemyX[i], enemyY[i], i)


**Class 10: Score Label and Game Over**
	
Now it’s time for showing the score. For that we have to declare the value of the score value. And make a function so that we can call it inside the while loop. So, the code will be;


Code:
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
textY = 10


Then we are going to make a function called show_score.
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))


As we are using font here, we can not directly blit the score on the screen. First, we have to render that font then we can blit it on the screen. That is why we have used the font.render to render the font. 


Now we have to call the show_score function inside the main while loop.


show_score(textX, textY)




**Class 11: Game Over**
	
To wrap up the game, we have to declare when the game will be over. So just like score we are going to give a variable for game over font.  
go_font = pygame.font.SysFont('freesansbold.ttf', 70)


Then just like the score, now we are going to render and blit the game over text. 
def game_over():
    go = font.render("GAME OVER", True, (255,255,255))
    screen.blit(go, (330, 300))


As we have rendered the font now, we have to call the function so that whenever enemy ships are going to touch the player ship it will move the enemy ship out of the screen and break out from the main while loop. 
if enemyY[i] > 440:
    for j in range(number_of_enemy):
        enemyY[j] = 850
    game_over()
    break


So, whenever the enemy Y axis touches 440, it will move all of the enemy ship to 850, as our screen window size is 800. So, 850 is out of the window. And it will call the game over function and after that the for IF loop will break-down. As we haven’t declared any action when enemy y axis is 850, so the while loop will not meet any condition and it will break out of the loop. 
