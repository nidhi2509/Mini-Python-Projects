'''
File name: interfaces.py
Author username(s): denneyen, jaltarnr
Date: 11/28/2017

interfaces.py

Please mess around with this program, have fun with this game!

For part I of the assignment, ignore the Graphics stuff

 by Andy Exley
'''

import sys
try: 
    import graphics 
except ImportError:
    sys.stderr.write("Couldn't import graphics.py (the Zelle graphics module.)\n")
    sys.stderr.write("This is fine for Part I of the assignment.\n")
    sys.stderr.write("For Part II you should make sure that graphics.py" +
                             " is in the same directory as this code.\n\n")


class TextLanderInterface:
    """Text-based interface for lander game. Use this one for testing"""

    def show_info(self, lander):
        """Display lander's status to user"""
        print ("Lander Status: Altitude %d, Velocity %d, Fuel %d" % 
            (lander.get_altitude(), lander.get_velocity(), lander.get_fuel()))

    def get_thrust(self):
        """Get thrust amount from user"""
        amtstr = input("Thrust amount?")
        return int(amtstr)

    def show_crash(self):
        """Display to user that we crashed"""
        print("Crash! Oh noes!")

    def show_landing(self):
        """Display to user that we landed safely"""
        print("Hooray, the Eagle has landed!")

    def close(self):
        """Close the interface"""
        print("Goodbye")
        
class Button:
    """A class that creates very simple buttons using the Zelle graphics module
    """

    def __init__(self, point, width, height, text):
        """Constructor
            Parameters:
                point: The center point of the button
                width: The width of the button
                height: The height of the button
                text: The text written inside of the button
        """
        p1 = graphics.Point(point.getX() - width / 2, point.getY() - height / 2)
        p2 = graphics.Point(point.getX() + width / 2, point.getY() + height / 2)
        self.rect = graphics.Rectangle(p1, p2)
        self.text = graphics.Text(graphics.Point(point.getX(), point.getY()), text)
       
        
        
    def wasClicked(self, point):
        """Returns true if the given point is inside this button
            Parameter:
                point: The point that a user clicked

            Return Value: True if the given point is inside this button's area, False otherwise
        """
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        if (p1.getX() <= point.getX() <= p2.getX() and
                p1.getY() <= point.getY() <= p2.getY()):
            return True
        return False
       

    def draw(self, win):
        """Draws the button in the given window"""
        self.rect.draw(win)
        self.text.draw(win)
      
        
        
class GraphicLanderInterface:
    """GraphicLanderInterface class is a graphical interface 
        for your lunar lander game"""

    def __init__(self):
        """Constructor that initializes the graphics window
        and shapes that we will use for drawing things"""

        # initialize window
        self.win = graphics.GraphWin("Lunar Lander Game", 300, 500)
        
        # transform coordinates
        self.win.setCoords(0, -10, 300, 600)

        self.surface_polygon = self.create_surface()
        self.surface_polygon.draw(self.win)
        self.background()
   

        self.lander_polygon = None
        # Draws two different thrust buttons
        self.b1 = Button(graphics.Point(100, 560), 80, 20, 'Thrust')
        self.b2 = Button(graphics.Point(200, 560), 80, 20, 'No Thrust')
        self.b1.draw(self.win)
        self.b2.draw(self.win)
        
        # Draws text values for altitude, velocity, and fuel
        self.alt_num = graphics.Text(graphics.Point(50, 400), 'Altitude: ')
        self.vel_num = graphics.Text(graphics.Point(50, 450), 'Velocity: ')
        self.fuel_num = graphics.Text(graphics.Point(50, 500), 'Fuel: ')
        self.alt_num.draw(self.win)
        self.vel_num.draw(self.win)
        self.fuel_num.draw(self.win)

    def show_info(self, lander):
        """This method currently gets the lander info then draws it and displays the values of the altitude, velocity, and fuel."""
        alt = lander.get_altitude()
        vel = lander.get_velocity()
        fuel = lander.get_fuel()
        

        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, alt),
                graphics.Point(self.win.width/2 - 3, alt + 10),
                graphics.Point(self.win.width/2 + 3, alt + 10),
                graphics.Point(self.win.width/2 + 10, alt))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.win)
        
        # Changes altitude, velocity, and fuel values
        self.alt_num.setText('Altitude: ' + str(alt))
        self.vel_num.setText('Velocity: ' + str(vel))
        self.fuel_num.setText('Fuel: ' + str(fuel))
        

    def get_thrust(self):
        """This method waits for a user's mouse click on the button then returns 1 if the "thrust" button is clicked and returns 0 if the "no thrust" button is clicked. """
        self.win.getMouse()
        
        # Identifies if certain button was clicked
        while True:
            pt = self.win.getMouse()
            if self.b1.wasClicked(pt):
                return 1
            elif self.b2.wasClicked(pt):
                return 0

    def show_crash(self):
        """Displays a graphical crash message."""  
        # Allows lander to crash on to moon's surface
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, 0),
                graphics.Point(self.win.width/2 - 3, 10),
                graphics.Point(self.win.width/2 + 3, 10),
                graphics.Point(self.win.width/2 + 10, 0))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.win)
        
        self.text = graphics.Text(graphics.Point(150, 90), 'You crashed! Oh no!')
        self.text.draw(self.win)
        
        # Draws fire around crashed lander
        self.fire = graphics.Polygon(graphics.Point(110, 0), graphics.Point(110, 20), graphics.Point(120, 15), graphics.Point(130, 20), graphics.Point(130, 0), graphics.Point(110, 0))
        self.fire.setFill('red')
        self.fire.draw(self.win)
        
        # Draws more fire around crashed lander
        self.fire_2 = graphics.Polygon(graphics.Point(170, 0), graphics.Point(170, 20), graphics.Point(180, 15), graphics.Point(190, 20), graphics.Point(190, 0), graphics.Point(170, 0))
        self.fire_2.setFill('red')
        self.fire_2.draw(self.win)
        print("Crash! Oh noes!")

    def show_landing(self):
        """Displays a graphical landing message."""
        # Allows lander to land on to moon's surface
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, 0),
                graphics.Point(self.win.width/2 - 3, 10),
                graphics.Point(self.win.width/2 + 3, 10),
                graphics.Point(self.win.width/2 + 10, 0))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.win)
        
        self.land = graphics.Text(graphics.Point(150, 90), 'You landed successfully! Hooray!')
        self.land.draw(self.win)
        
        # Draws ballons to celebrate landing
        self.balloon = graphics.Circle(graphics.Point(250, 50), 15)
        self.balloon.setFill('red')
        self.balloon.draw(self.win)
        self.string_1 = graphics.Line(graphics.Point(250, 35), graphics.Point(250, 15))
        self.string_1.setFill('black')
        self.string_1.draw(self.win)
        
        self.balloon_2 = graphics.Circle(graphics.Point(20, 50), 15)
        self.balloon_2.setFill('red')
        self.balloon_2.draw(self.win)
        self.string_2 = graphics.Line(graphics.Point(20, 35), graphics.Point(20, 15))
        self.string_2.setFill('black')
        self.string_2.draw(self.win)
        print("Hooray, the Eagle has landed!")

    def close(self):
        self.win.getMouse()
        self.win.close()
        
    def background(self):
        """Draws the background sun, earth, and stars"""
        sun = graphics.Circle(graphics.Point(200, 310), 50)
        sun.setFill('yellow')
        sun.draw(self.win)
        
        earth = graphics.Circle(graphics.Point(40, 250), 30)
        earth.setFill('blue')
        earth.draw(self.win)
        continent = graphics.Circle(graphics.Point(30, 265), 10)
        continent.setFill('green')
        continent.draw(self.win)
        cont_2 = graphics.Circle(graphics.Point(30, 235), 10)
        cont_2.setFill('green')
        cont_2.draw(self.win)
        cont_3 = graphics.Circle(graphics.Point(55, 245), 10)
        cont_3.setFill('green')
        cont_3.draw(self.win)
        
        stars =  graphics.Circle(graphics.Point(250, 250), 5)
        stars.setFill('white')
        stars.draw(self.win)
        star1 =  graphics.Circle(graphics.Point(100, 250), 5)
        star1.setFill('white')
        star1.draw(self.win)
        star2 =  graphics.Circle(graphics.Point(150, 150), 5)
        star2.setFill('white')
        star2.draw(self.win)
        star3 =  graphics.Circle(graphics.Point(50, 100), 5)
        star3.setFill('white')
        star3.draw(self.win)
        star3 =  graphics.Circle(graphics.Point(100, 50), 5)
        star3.setFill('white')
        star3.draw(self.win)
        star4 =  graphics.Circle(graphics.Point(250, 80), 5)
        star4.setFill('white')
        star4.draw(self.win)
        star4 =  graphics.Circle(graphics.Point(200, 60), 5)
        star4.setFill('white')
        star4.draw(self.win)
        

    def create_surface(self):
        """Draws the surface of the moon"""
        oval = graphics.Oval(graphics.Point(5,0), graphics.Point(300, -10))
        oval.setFill("gray")
        return oval
