def setup():
    # Set the size of your sketch
    size(400, 450)

    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    w = 300
    h = 350
    for i in range(10):
        if i % 2 == 0:
            fill("#FF1F1F")
            
        else:
            fill("#FFFAFA")
        ellipse(200,200,w,h)
        w -= 30
        h -= 30
    
    # Use an if statement and modulo to alternate the color of your rings
        
    
    
    pass
