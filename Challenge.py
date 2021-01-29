#You challenge for this session is to make this game 2-Player 
#Task 1 : Make the Sprite 1 a bit smaller. (Hint : Find and Make adjustments to the scale function)
#Task 2 : Add a second sprite (the files will be provided to you, they will be named d0,d1,d2,...,d8)
#Task 3 : Animate the second sprite. Just like you animated the first sprite during class.
#Task 4 : Add movements to the second sprite using ASDW keys (A for left, D for right, W for up and S for down)
#Task 5 : There should be seperate variables for storing the score of each player, both scores should be displayed on top of screen.  



import arcade
#Quick trivia, random is the name of a python library that generates random numbers in various forms. Randint is responsible for generating
#Random valued integers within a range that we can define.
from random import randint

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height, title)
        self.set_location(100,100)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        #Step 1 : Create a player_list and keep it empty. For this, we will use the Python keyword "None". Right now, our compiler doesn't know
        #Anything about player_list or the nature of this data structure. It has only reserved the name.
        self.player_list = None

        #Step 2 : Create another empty variable and set it to None
        self.player = None

        #Step 11 : Now that the Setup function has been defined, you may call it in the initializer function so that it may run at the start
        #of the game
        self.setup()


    #Step 3 : Define the setup function. In this function, we will be adding all of the initial details of many of our sprites.
    def setup(self):

        #Step 4 : The player list and player variables that we just added. Populate them with arcade.SpriteList() and arcade.AnimatedWalkingSprite()
        #arcade.SpriteList  creates a list in which you may add many sprites instead of just one. This way, whenever there's an operation
        #That you wish to perform on all the sprites, you wont have to write the code for each individual sprite, you can just write it once
        #For the list and every sprite in that list will be changed automatically.
        self.player_list = arcade.SpriteList()

        #Animeted Walking Sprite, at the backend is just another sprite. However, it has some extra functions and properties to animate itself.
        self.player = arcade.AnimatedWalkingSprite()

        #Step 5 : Create a list called stand_right_texture Add the standing-still image or c0 to it.
        #-----------------------------------
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("sprites/Session_3/c0.png"))
        # Step 6 : Create a list called stand_left_texture Add the standing-still image or c0 to it but this time mirror is to the direction is opposite.
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("sprites/Session_3/c0.png", mirrored = True))
        # -----------------------------------

        #Step 7 : Now that we've added the standing textures, we need to add the walking textures. In order to do that, we will need to add
        #a list called walk_right_textures and then append more pictures to it "c1 onwards to c8"
        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c1.png"))
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c2.png"))
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c3.png"))
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c4.png"))
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c5.png"))
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c6.png"))
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c7.png"))
        self.player.walk_right_textures.append(arcade.load_texture("sprites/Session_3/c8.png"))


        #Step 8 : We will repeat the above steps for another list called walk_left_textures. And this time we will mirror the images.
        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c1.png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c2.png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c3.png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c4.png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c5.png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c6.png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c7.png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("sprites/Session_3/c8.png", mirrored=True))

        #Step 9 : Set the speed, scale (scale == the size of the sprite) and the center coordinates of your zombie sprite here.
        self.player.speed = 5
        self.player.scale = 0.8
        #Python Trivia : The // Operator is actually a floor operator. division that results into whole number adjusted to the left in the number line
        self.player.center_x = 600 // 2
        self.player.center_y = 600 // 2

        #Step 10 : Append the player sprite into the player_list
        self.player_list.append(self.player)

        #SCROLL UP FOR STEP 11

        #Step 17 : Now that The Sprite animations are out of the way, lets add the brains to our game
        self.brain = arcade.Sprite("sprites/Session_3/object.png", center_y=16, center_x=16)
        self.brain.set_position(randint(50, 550), randint(50, 550))
        self.brain.scale = 0.1

        #Step 18 : Create a variable to store the Score and set it to 0
        self.score = 0

    #Step 19 : Define a function on_collide, this is where we handle our collision detection.
    def on_collide(self):
        if self.brain.collides_with_sprite(self.player):
            self.score += 1
            self.brain.set_position(randint(50, 550), randint(50, 550))


    def on_draw(self):
        arcade.start_render()

        #Step 12 : In the draw function, you need to call this function, otherwise the player sprite will not appear on screen.
        self.player_list.draw()

        #Step 20 : Draw the brain, and write the score on top
        self.brain.draw()
        arcade.draw_text("Score : {} ".format(self.score), 20, 580, arcade.color.BLACK, 14)

    def on_update(self, delta_time: float):

        #Step 13 - Edge Detection. We're just telling the sprite what to do in case it collides with the edge
        if self.player.center_x >= 600:
            self.player.center_x = 598
        if self.player.center_x < 0:
            self.player.center_x = 2
        if self.player.center_y >= 600:
            self.player.center_y = 598
        if self.player.center_y < 0:
            self.player.center_y = 2

        #Step 14 : Update Player_list and also update its animation.
        self.player_list.update()
        #Arcade Trivia, whenever the sprite is supposed to move forward or backward, a property of the AnimatedWalkingSprite changes.
        #This property is called change_x and change_y. If the sprite is supposed to move up, change_y will increase, it will decrease if the sprite wants to go down
        #Similarly if the sprite wishes to go right or left, change_x will be increased or decreased accordingly.
        #The bigger the increase/decrease in change_x/y, the faster the sprite will move. This movement is dealt with automatically in the following function
        # i.e. update_animation()
        self.player_list.update_animation()

        #Step 21 : Call the on_collide function
        self.on_collide()


    #Step 15 : Update the key pressed function, if you do not understand whats happening here, refere to the Arcade trivia just above.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = self.player.speed
        elif key == arcade.key.DOWN:
            self.player.change_y = -self.player.speed
        elif key == arcade.key.RIGHT:
            self.player.change_x = self.player.speed
        elif key == arcade.key.LEFT:
            self.player.change_x = -self.player.speed

    #Step 16 : Implement Key Release
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player.change_x = 0


MyGameWindow(600,600, 'My Game Window')
arcade.run()