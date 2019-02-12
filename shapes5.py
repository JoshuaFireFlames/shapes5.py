from graphics import*


window = GraphWin("shapes5.py", 300, 300)
window.setCoords(0,0, 1000, 1000)

triB = Polygon(Point(100, 100), Point(150, 200), Point(200,100))
triB.setFill(color_rgb(30,30, 230))
triB.draw(window)

sqR = Rectangle(Point(900,100), Point( 800,200))
sqR.setFill(color_rgb(255, 0,0))
sqR.draw(window)

ovM = Oval(Point(900,960), Point(800, 700))
ovM.setFill(color_rgb(165,42,42))
ovM.draw(window)



window.getMouse()
window.close()


