import pgzrun

WIDTH = 600
HEIGHT = 500

def draw():
    screen.clear()
    screen.fill('black')
    screen.draw.text('Hello what are you doing', (100, 100), color = 'orange')
    screen.draw.line((200, 200), (350, 350), color = 'green')
    screen.draw.circle((350, 250), 50, color = 'green')
    screen.draw.rect(Rect((50, 50), (300, 100)), color = 'green')
    screen.draw.rect(Rect((10, 10), (30, 30)), color = 'green')

pgzrun.go()