

        #Arcade Trivia : There three different collisions in Arcade. Collide with Sprite, Collide with Point and Collide with List. You can also set up a collision radius for any sprite you want.
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