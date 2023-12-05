from tkinter import *
from tkinter.messagebox import showinfo
import random

width = 800
heigh = 600
grid_size = 20


class square:


    def __init__(self, x, y, color):
        self.x = x
        self.y = y 
        self.color = color
        self.velx = 0
        self.vely = 0
        self.dim = [0,0, 0,grid_size, grid_size, grid_size,grid_size, 0]


    def setVel(self, newx, newy):
        self.velx = newx
        self.vely = newy

    def pos(self):
        return [self.dim[0] + self.x, self.dim[1] + self.y, self.dim[2] + self.x, self.dim[3] + self.y, self.dim[4] + self.x, self.dim[5] + self.y, self.dim[6] + self.x, self.dim[7] + self.y]



                
    def update(self):
        if(self.x>0 and self.x<width-grid_size):
            self.x += self.velx
        if(self.y>0 and self.y<heigh-grid_size):
            self.y += self.vely
        if(self.x==0 and self.velx>0):
            self.x += self.velx
        if(self.x==width-grid_size and self.velx<0):
            self.x += self.velx
        if(self.y==0 and self.vely >0):
            self.y += self.vely
        if(self.y==heigh-grid_size and self.vely <0):
            self.y += self.vely



class Game:

    def __init__(self, game_name):
        self.window = Tk()
        self.canvas = Canvas(self.window, bg='black', width=width, heigh=heigh)
        self.canvas.pack()
        self.score = 0
        self.window.title(game_name)
        self.window.bind("<Escape>", self.quitGame) #so sai com esc
  
     
        s = square(20, 20, '#800080')
        s1 = square(20, 20 ,'#800080')
        s2 = square(20, 20, '#800080')
        s3 = square(20, 20, '#800080')

        f = square(random.randint(grid_size,( width/grid_size))*grid_size - grid_size, random.randint(grid_size, (heigh/grid_size))*grid_size - grid_size, 'purple')
        
        self.snake = [s, s1, s2, s3]
        self.food = [f]
        self.vel = [[20,0], [0,0], [0,0], [0,0]]

        self.window.bind("<Up>", self.moveUp)
        self.window.bind("<Down>", self.moveDown)
        self.window.bind("<Right>", self.moveRight)
        self.window.bind("<Left>", self.moveLeft)
    
    def eatFood(self):
        self.score += 1
        
    def showScore(self):
        self.canvas.create_text(width-50, 10, text=f"Pontuação: {self.score}", fill="white", anchor="ne")

    def moveUp(self, event):
        if(self.vel[0] != [0,20]):
            self.vel[0] = [0,-20]
    def moveDown(self, event):
        if(self.vel[0] != [0,-20]):
            self.vel[0] = [0,20]
    def moveRight(self, event):
        if(self.vel[0] != [-20,0]):
            self.vel[0] = [20,0]
    def moveLeft(self, event):
        if(self.vel[0] != [20,0]):
            self.vel[0] = [-20,0]
    def quitGame(self, event):
            self.window.destroy()
    def resetGame(self):
            self.snake[0].x = 20
            self.snake[0].y = 20
            for i in range(1, len(self.snake)):
                self.snake[i].x = -1000
                self.snake[i].y = -1000
            self.vel = [[20,0], [0,0], [0,0], [0,0]]
            self.food[0].x = random.randint(grid_size, (width/grid_size))*grid_size-grid_size
            self.food[0].y = random.randint(grid_size, (heigh/grid_size))*grid_size-grid_size
            self.score = 0

    def run(self):
        counter = 0
        while True:
            self.canvas.delete(ALL)  # Correção aqui

            self.showScore()

            for i in range(len(self.vel)-1, 0, -1):
                self.vel[i] = self.vel[i-1]

            for i in range(len(self.vel)):
                self.snake[i].velx = self.vel[i][0]
                self.snake[i].vely = self.vel[i][1]

            if self.snake[0].pos() == self.food[0].pos():
                self.food[0].x = random.randint(grid_size, (width/grid_size))*grid_size-grid_size
                self.food[0].y = random.randint(grid_size, (heigh/grid_size))*grid_size-grid_size
                self.vel.append([0, 0])
                self.snake.append(square(self.snake[-1].x, self.snake[-1].y, self.snake[0].color))
                self.eatFood()

            for s in self.snake:
                s.update()
                self.canvas.create_polygon(s.pos(), fill=s.color)

            for f in self.food:
                f.update()
                self.canvas.create_polygon(f.pos(), fill=f.color)

            for i in range(2, len(self.snake)):
                if counter < 1:
                    counter += 1
                elif self.snake[0].pos() == self.snake[i].pos():
                    score_message = f"GAME OVER!!!\nScore: {self.score}\n\nDeseja Jogar Novamente?"
                    play_again = showinfo(title="Game Over", message=score_message, type="yesno")

                    if play_again:
                        self.resetGame()
                    else:
                        self.window.destroy()
                        break

            self.canvas.update()
            self.canvas.after(100)

        self.window.mainloop()
            
g = Game("Jogo da cobrinha do rick")
g.run()
