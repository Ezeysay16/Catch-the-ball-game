
import math
from graphics import Canvas
import random
import time


CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
R = 20
ANIMATION_DELAY_SECONDS = 0.02

def random_balls(canvas,balls):
    x = random.randint(0, CANVAS_WIDTH - R)
    y = random.randint(0,CANVAS_HEIGHT - R)
    ball = canvas.create_oval(x,y,x +R , y + R )
    canvas.set_color(ball, 'Red')
    balls.append(ball)
    return ball




    

def create_python(canvas,x,y,PADDLE_WIDTH):

    rect = canvas.create_rectangle(x,y,x + PADDLE_WIDTH, y + PADDLE_WIDTH)
    canvas.set_color(rect, 'black')
    return rect


# def update_paddle_location(canvas):

def add_score_label(canvas, score):
    """
    Adds a score label to the top-left corner of the screen, displaying
    the initial score of 0.
    """
    label = canvas.create_text(0, 0, "")
    canvas.set_font(label, "Courier", 20)
    update_score_label(canvas, label, score)
    return label






def update_score_label(canvas, score_label, score):

    canvas.set_text(score_label, "Score: " + str(score))

    canvas.moveto(score_label, 0, 0)


        

                
     



def playing_board(canvas,balls,PADDLE_WIDTH,rect):
    score = 0
    score_label = add_score_label(canvas, score)
    keyboard_control(canvas,balls,PADDLE_WIDTH,rect,score_label)
    

    


def keyboard_control(canvas,balls,PADDLE_WIDTH,rect,score_label):

    a = create_python(canvas, canvas.get_left_x(rect), canvas.get_top_y(rect),PADDLE_WIDTH)
    canvas.delete(a)
    ball = random_balls(canvas,balls)
    while True:
        

            
        lol = canvas.get_new_key_presses()
        for press in lol:   
                    
            if press.keysym == "w" or press.keysym == "W" :
                canvas.move(rect, 0,-20)
            if press.keysym == "s" or press.keysym == "S":
                canvas.move(rect, 0,abs(20))

            if press.keysym == "a" or press.keysym == "A":
                canvas.move(rect,-20, 0)
            if press.keysym == "d" or press.keysym == "D":
                canvas.move(rect,abs(20),0)    

            is_collided_ball = False
            ball_coords = canvas.coords(ball)
    
            colliders = canvas.find_overlapping(ball_coords[0],ball_coords[1], ball_coords[2], ball_coords[3])
            if rect in colliders:
                is_collided_ball = True
                score = 0
                while score <=10:
                    canvas.delete(ball)
                    score += 1
                    update_score_label(canvas, score_label, score)
                    k = 0
                    if k == 0:
                        for i in range(10):
                            PADDLE_WIDTH = PADDLE_WIDTH + 10
                            
                            keyboard_control(canvas,balls,PADDLE_WIDTH,rect, score_label)
                        
                ball = random_balls(canvas,balls)
            
        time.sleep(ANIMATION_DELAY_SECONDS)
        canvas.update()
            
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Breakout")
    balls = []
    PADDLE_WIDTH = 20
    
    rect = create_python(canvas, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2,PADDLE_WIDTH)
    playing_board(canvas,balls,PADDLE_WIDTH,rect)
    

    


if __name__ == '__main__':
    main()
