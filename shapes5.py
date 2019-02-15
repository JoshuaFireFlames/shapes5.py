# a graphic program by Joshviper
from graphics import*


window = GraphWin("shapes5.py", 300, 300)#The name of the window and width - height of the object.
window.setCoords(0,0, 1000, 1000)#Sets the size of your window.

triB = Polygon(Point(100, 100), Point(150, 200), Point(200,100))#Polygon() will take all the points you give to retrun to staring point.
triB.setFill(color_rgb(255,215, 0))#Setting the color the object.
triB.draw(window)#Draws the triangle on the screen

sqR = Rectangle(Point(900,100), Point( 800,200))#The coordinate points it takes to draw a rectangle.
sqR.setFill(color_rgb(255, 0,0))#Setting the color the object.
sqR.draw(window)#Draws the square on the screen.

ovM = Oval(Point(900,960), Point(800, 700))#the coordinate points it takes to draw a oval.
ovM.setFill(color_rgb(165,42,42))#Setting the color the object.
ovM.draw(window)#Draws the oval on the screen.

cirG = Circle(Point(100,900), 50)#The coordinate points it takes to draw a circle.
cirG.setFill(color_rgb(0,128,0))#Setting the color the object.
cirG.draw(window)#Draws the circle in the window.

rombB = Polygon(Point(450,500), Point(500,600),Point(550,500), Point(500,400))#Polygon() will take all the points you give to retrun to staring point.
rombB.setFill(color_rgb(30,30,230))#Setting the color the object.
rombB.draw(window)#Draws the diamond in the window.



window.getMouse()
#This method pauses the program until the user clicks in a particular window.

window.close()
#This is a way to close the window.


