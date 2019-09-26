#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""
#comment
import arcade #Imports pip arcade
#comment
SCREEN_WIDTH = 640 #sets the width resolution variable to 640
SCREEN_HEIGHT = 480 #set the height resoltion variable to 480
SCREEN_TITLE = "Move Mouse Example" #Creates a variable to contain a string for a title
#comment
#comment
class Ball: #creates class Ball
    def __init__(self, position_x, position_y, radius, color): #def function __init__ and the variables it should expect to recieve
#comment
        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x #sets its x position as the recieved x position
        self.position_y = position_y #sets its y position as the recieved y position
        self.radius = radius #sets radius to recieved radius
        self.color = color # sets color to recieved color
#comment
    def draw(self):#defines function draw, taking the variable self
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)#draws the circle onto the screen
#comment
#comment
class MyGame(arcade.Window):#creates class MyGame
#comment
    def __init__(self, width, height, title):#defines __init__ function
#comment
        # Call the parent class's init function
        super().__init__(width, height, title)#I mean, it says what this does in the line before
#comment
        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)#again says what it does
#comment
        arcade.set_background_color(arcade.color.ASH_GREY)#sets the background color
#comment
        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)#creates ball
#comment
    def on_draw(self):#defines on draw
        """ Called whenever we need to draw the window. """
        arcade.start_render()#starts rendering
        self.ball.draw()#calls the draw function of class Ball
#comment
    def on_mouse_motion(self, x, y, dx, dy):#defines function on_mouse_motion
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x#sets ball position x to the recieved x value
        self.ball.position_y = y#sets ball position y to the recieved y value
#comment
    def on_mouse_press(self, x, y, button, modifiers):#defines on mouse press function
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")#prints text displaying a button number
        if button == arcade.MOUSE_BUTTON_LEFT:#checks if left mouse is the button pressed
            self.ball.color = arcade.color.BLACK#changes ball color
#comment
    def on_mouse_release(self, x, y, button, modifiers):#defines on mouse release
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:#checks if left mouse is the button released
            self.ball.color = arcade.color.AUBURN#changes ball color
#comment
#comment
def main():#defines main
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)#creates game window
    arcade.run()#runs the arcade
#comment
#comment
if __name__ == "__main__":#checks the name of the function
    main()#runs main