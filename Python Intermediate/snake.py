from turtle import Screen, Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    #creating the snake body
    def create_snake(self):
        snakebody = [(0, 0), (-20, 0), (-40, 0)]
        for n in snakebody:
            snakeb = Turtle()
            snakeb.color("white")
            snakeb.shape("square")
            snakeb.penup()
            snakeb.goto(n)
            self.segments.append(snakeb)        
    
    #creating the move functionality
    def move(self):
        for m in range(len(self.segments) - 1, 0, -1):
            x = self.segments[m - 1].xcor() 
            y = self.segments[m - 1].ycor()
            self.segments[m].goto(x, y)
        if self.segments[0].distance(food) < 15:
            self.segments.append(snakeb)
            food.goto(new_x, new_y)
            score += 1
            board.penup()
            board.goto(450, 300)
            board.color("white")
            board.clear()
            board.write(f"{score}", align = "center", font = ("Comic Sans MS", 22, "bold"))
        segments[0].forward(20)
    
    #creating the user functionality
    def forward(self):
            self.head.setheading(90)
            self.head.forward(30)
    def backward(self):
            self.head.setheading(270)
            self.head.forward(30)