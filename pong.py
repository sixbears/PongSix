from tkinter import *


class Fenetre(Tk):
    def __init__(self, width=1900, height=950):
        Tk.__init__(self)
        self.flag = 0

        self.quit= Button(self,text="Quit Game",command=self.destroy)
        self.quit.grid(column=4,row=2,sticky="SE")

        self.new= Button(self,text="New Game",command=self.new_game)
        self.new.grid(column=0,row=0,sticky="NW") 
  
        self.can = Canvas(self,width=width,height=height,bg="black")
        self.can.grid(column=0,row=1,columnspan=5)

           
    def new_game(self):
        if self.flag == 0 :
            self.flag=1
            self.pads = Pad(self.can,self.flag)
            self.ball = Ball(self.can,self.pads,self.flag)



class Pad:
    def __init__(self,canvas,flag):
        self.canvas = canvas
        self.flag = flag
        self.height = canvas.winfo_height()
        self.width = canvas.winfo_width()
        self.x1,self.y1 = 10,self.height/2-30
        self.x2,self.y2 = self.width-25,self.height/2-30
                
        self.Pad1 = canvas.create_rectangle(self.x1,self.y1,self.x1+15,self.y1+100,fill="white")
        self.Pad2 = canvas.create_rectangle(self.x2,self.y2,self.x2+15,self.y2+100,fill="white")

        canvas.bind_all("<z>",self.upJ1)
        canvas.bind_all("<s>",self.downJ1)

        canvas.bind_all("<p>",self.upJ2)
        canvas.bind_all("<m>",self.downJ2)


    def upJ1(self,event):
        if self.y1>5 :
            self.y1=self.y1-30
            self.canvas.coords(self.Pad1,self.x1,self.y1,self.x1+15,self.y1+100)

            
    def downJ1(self,event):
        if self.y1+60<(self.height-5):
            self.y1=self.y1+30
            self.canvas.coords(self.Pad1,self.x1,self.y1,self.x1+15,self.y1+100)


    def upJ2(self,event):
        if self.y2>5 :
            self.y2=self.y2-30
            self.canvas.coords(self.Pad2,self.x2,self.y2,self.x2+15,self.y2+100)

            
    def downJ2(self,event):
        if self.y2+60<(self.height-5):
            self.y2=self.y2+30
            self.canvas.coords(self.Pad2,self.x2,self.y2,self.x2+15,self.y2+100)


class Ball:
    def __init__(self,canvas,pad,flag):
        self.canvas = canvas
        self.pad = pad
        self.height = canvas.winfo_height()
        self.width = canvas.winfo_width()
        self.flag = flag
        self.x1,self.y1 = self.width/2,self.height/2
        self.dx,self.dy = 2,2
        self.Ball = canvas.create_oval(self.x1, self.y1, self.x1+25, self.y1+25, width=1, fill='white')
        self.pointJ1, self.pointJ2 = 0,0
        
        self.ready()

    
    def ready(self):
        self.starter=0
        self.score= Label(app,text="%d : %d" % (self.pointJ1,self.pointJ2), bg="black",fg="white")
        self.score.grid(column =2,row=0)
        self.x1,self.y1 = self.width/2, self.height/2
        app.titre = Label(app,text="PRESS SPACE TO START", bg="black",fg="white")
        app.titre.grid(column =2,row=2)
        self.canvas.bind_all("<space>",self.start)
        

    def start(self,event):
        self.starter=1
        self.move()  

        
    def move(self):
        if self.starter==1:
            self.x1 = self.x1 +self.dx
            self.y1 = self.y1 + self.dy  
            if self.y1 >self.height-20:
                self.dy = -self.dy

            if self.y1 <2:
                self.dy = -self.dy
       
            if self.x1 < self.pad.x1+20:
                if self.pad.y1 < self.y1 < self.pad.y1+100:
                    self.dx = -self.dy

            if self.x1+30 >  self.pad.x2-1:
                if self.pad.y2<self.y1+12.5<self.pad.y2+100:
                     self.dx = -self.dy

            if self.x1 < 0:
                self.starter = 0
                self.pointJ2 += 1
                self.ready()
        
            if self.x1+25 > self.width:
                self.starter=0
                self.pointJ1 += 1
                self.ready()

            self.canvas.coords(self.Ball,self.x1,self.y1,self.x1+30,self.y1+30)
            if self.flag > 0:
                self.canvas.after(8,self.move)


if __name__ == "__main__":
    app = Fenetre()
    app.mainloop()