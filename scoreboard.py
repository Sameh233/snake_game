from turtle import Turtle

ALIGNEMENT = "center"
FONT = ('Courier', 20, 'bold')

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score_points = 0
        with open("data.txt") as file :
            self.highest_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()
            
                   
    def reset(self):
        if self.score_points > self.highest_score :
            self.highest_score = self.score_points 
            with open("data.txt", mode= "w") as file :
                file.write(f"{self.highest_score}")
        self.score_points = 0
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_points} High Score: {self.highest_score}", align= ALIGNEMENT, font= FONT)
        
        
    def add_score(self) :
        self.score_points += 1
        self.update_score()

