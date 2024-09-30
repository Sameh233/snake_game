from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    
    def __init__(self) -> None:
        self.segments_number = 3
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]
    
                
    
    def create_snake(self):
        for i in range (self.segments_number):
            x = 0 
            position = (x,0)
            self.add_segment(position)
            x -= 20
    
    def add_segment(self, position):
        snake_segment = Turtle("square") 
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments_list.append(snake_segment)
        
        
    def reset(self):
        for seg in self.segments_list:
            seg.goto(2000,2000)
        self.segments_list.clear()
        self.create_snake()
        self.head = self.segments_list[0]
    
    def extend(self):
        self.add_segment(self.segments_list[-1].position())
        
        
        
    
    def move(self):
        for seg_num in range(len(self.segments_list) - 1, 0, -1 ):
            new_x =  self.segments_list[seg_num - 1].xcor()
            new_y = self.segments_list[seg_num - 1].ycor()
            self.segments_list[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
        
    
    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(90)
            
    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(0)          
        
    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(180)        
            
          
        
   
  
