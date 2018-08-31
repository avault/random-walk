#Imma do many good comments dis time
s = 0 #Step
r = 150 #Radius
l = 5 #Lenght per step
sa = [] #Step ammount

def setup():
    size(500,500, P3D)
    set_zero() #I bet youll never guess wat this does (Hint: Its sets things to zero)

def draw():
    global x, y, z, r, s, sa, l
    background(0)
    pushMatrix()
    translate(width/2,height/2,0) #Default "centering"
    noFill()
    strokeWeight(1) #Creates the spear for the ball to move in
    stroke(255)
    sphereDetail(10)
    rotateX(radians((height/2)-mouseY))
    rotateY(radians(mouseX-(width/2))) #rotates the spear on mouse position
    sphere(r)
    
    
    move_step()
    fill(255,0,0)
    strokeWeight(10) #Makes a point and plots it
    stroke(255,0,0)
    point(x, y, z)
    popMatrix()
    if mousePressed: #Click 2 diplay textzzz
        pushMatrix()
        fill(0,255,0) #Prints some texts to show off my amazing skillz
        steps = "Steps: " + str(s)
        text(steps, 5, 25)
        fill(0,0,255)
        trial = "Trial: " + str(len(sa))
        text(trial, width - 50, 25)
        fill(0,255,255)
        radius = "Radius: " + str(r)
        text(radius, 5, height - 25)
        fill(255,0,255)
        leng = "Step Length: " + str(l)
        text(leng, width - 100, height - 25)
        popMatrix()
    else:
        pushMatrix()
        translate(25,25,0)
        rotateX(radians((height/2)-mouseY))
        rotateY(radians(mouseX-(width/2)))
        strokeWeight(2)
        stroke(255,0,0)
        line(0,0,0,20,0,0)
        stroke(0,255,0)
        line(0,0,0,0,20,0)
        stroke(0,0,255)
        line(0,0,0,0,0,20)
        popMatrix()
    
    if dist(0, 0, 0, x, y, z) > r: #if the ball has left the spear
        reset()
    
    if keyPressed:
        if key == "s":
            show_stats()

def move_step():
    global x, y, z, s, l
    v = PVector().random3D() #random unit vector
    v.mult(l)
    x += v.x
    y += v.y
    z += v.z
    s += 1 #Adds thingzzz

def reset(): #Resets the ball @ 0,0,0 and adds step to list
    global s, sa
    sa.append(s)
    print s
    s = 0
    set_zero()

def set_zero():
    global x, y, z
    x = 0
    y = 0 #What a surpries, it sets zeros
    z = 0

def show_stats():
    global sa
    not_pressed = True
    noLoop()
    background(0)
    fill(0,255,0) #Prints some texts to show off my amazing skillz
    fill(0,255,0) #Prints some texts to show off my amazing skillz
    mean = "Average: " + str(get_stat(sa, "average"))
    text(mean, 5, 25)
    fill(0,0,255)
    std = "Standard Devation: " + str(get_stat(sa, "stdev"))
    text(std, 5, 50)
    fill(0,255,255)
    trial = "Trials: " + str(len(sa))
    text(trial, 5, 75)
    fill(100,100,255)
    radius = "Radius: " + str(r)
    text(radius, 5, 100)
    fill(255,0,255)
    leng = "Step Length: " + str(l)
    text(leng, 5, 125)
    while(not_pressed):
        not_pressed = not (keyPressed and key == "s")
    loop()

def get_stat(l, t):
    if len(l) > 0:
        if t == "average":
            return sum(l) / float(len(l))
        if t == "stdev":
            d = [x - (sum(l) / float(len(l))) for x in l]
            sqq = [x**2 for x in d]
            return sqrt(sum(sqq))
    else:
        return "null"