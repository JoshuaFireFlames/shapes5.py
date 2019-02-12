from graphics import*

window = GraphWin("shapes5.py", 300, 300)
window.setCoords(0,0, 1000, 1000)

btri = Polygon(Point(100, 100), Point(150, 200), Point(200,100))
btri.setFill(color_rgb(30,30, 230))
btri.draw(window)



window.getMouse()
window.close()


