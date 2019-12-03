import turtle
import time

pisces = turtle.Turtle()
screen = turtle.Screen()

screen.screensize()
screen.setup(height = 1080, width = 1920)
screen.bgcolor('grey')

FONTSIZE = 18
FONT = ('Arial', FONTSIZE, 'normal')
pisces.hideturtle()
pisces.pencolor("white")
pisces.penup()
pisces.write('Midterm Constellation Project', align = 'center', font = FONT)
pisces.goto(-7, -42)
pisces.write('Pisces Constellation', align = 'center', font = FONT)
pisces.goto(-10, -85)
pisces.write('Luis Carmona', align = 'center', font = FONT)
pisces.pendown()
pisces.hideturtle()
time.sleep(10)
screen.clear()

myPen = turtle.Turtle()
myPen.speed('fast')
screen = turtle.Screen()
screen.bgpic('piscesConstell.gif')
myPen.color("black")
screen.setup(width = 1920, height = 1080)
time.sleep(10)
screen.clear()

def drawConstellation(constellation):
  myPen.hideturtle()
  myPen.penup()
  myPen.goto(constellation[0])
  myPen.begin_fill()
  myPen.circle(5)
  myPen.end_fill()
  myPen.pendown()

  for stars in constellation:
    myPen.goto(stars)
    myPen.begin_fill()
    myPen.circle(5)
    myPen.end_fill()
  myPen.penup()

def drawNodes(dims):
  myPen.penup()
  myPen.goto(dims[0])
  myPen.circle(5)

  for stars in dims:
    myPen.goto(stars)
    myPen.begin_fill()
    myPen.circle(5)
    myPen.end_fill()

def drawGalaxy(portal):
  myPen.color("grey")
  myPen.penup()
  myPen.goto(portal[0])
  myPen.circle(10)

  for stars in portal:
    myPen.goto(stars)
    myPen.begin_fill()
    myPen.circle(10)
    myPen.end_fill()


piscesConstell = [[-265,288],[-289,257], [-273,230], [-265,288], [-273,230], [-337,112],[-393,30],[-434,-40],[-367,-5], [-337, 5], [-250, 20], [-194,10], [160,-3], [226,-28], [268,-12], [307,-52], [272, -85], [218,-78], [226,-28]]
twinkles = [[-265,196],[-394,-35], [337,-46]]
galaxy = [[-357, 134]]
drawConstellation(piscesConstell)
drawNodes(twinkles)
drawGalaxy(galaxy)
