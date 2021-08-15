def pong():
    import turtle

    win = turtle.Screen()
    win.title("Pong by @Canthelpit")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)


    # Paddle A
    paddle_a = turtle.Turtle()   #class call
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)      #paddle side

    # Paddle B
    paddle_b = turtle.Turtle()   #class call
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()   #class call
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2   #dx and dy are for change and 2 is the speed in pixel
    ball.dy = -0.2

    # Pen
    pen = turtle.Turtle()
    pen. speed(0)   #animation speed
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier",24,"normal"))

    #Score
    score_a = 0
    score_b = 0


    # Function
    def paddle_a_up():
        y = paddle_a.ycor()  #returns y cordinate
        y += 20
        paddle_a.sety(y)   #setting y to the new y

    def paddle_a_down():
        y = paddle_a.ycor()  #returns y cordinate
        y -= 20
        paddle_a.sety(y)   #setting y to the new

    def paddle_b_up():
        y = paddle_b.ycor()  #returns y cordinate
        y += 20
        paddle_b.sety(y)   #setting y to the new y

    def paddle_b_down():
        y = paddle_b.ycor()  #returns y cordinate
        y -= 20
        paddle_b.sety(y)   #setting y to the new
    # Keyboard binding
    win.listen()
    win.onkeypress(paddle_a_up, "w")
    win.onkeypress(paddle_a_down, "s")
    win.onkeypress(paddle_b_up, "Up")
    win.onkeypress(paddle_b_down, "Down")



    # Main game loop
    while True:
        win.update()

        # move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:   #upper border
            ball.sety(290)
            ball.dy *= -1  #reverse the direction of the ball


        if ball.ycor() < -290:  #lower border
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:   #left border
            ball.goto(0, 0)
            ball.dx *= -1
            score_a +=1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:   #right border
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

            # Paddle and ball collosions
        if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1








