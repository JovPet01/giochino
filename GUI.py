from tkinter import *
from PIL import Image, ImageTk
import time

schermata = Tk()
schermata.title("Jovan's RPG")
schermata.iconbitmap("immagini\icona.ico")

class GUI(Frame):

      def __init__(self):

              super(GUI, self).__init__()

              self.config(width=700, height=500)
              self.pack()
              self.bg()
              self.statistiche()      

      def bg(self):
            
            load = Image.open("immagini\\background.png")
            render = ImageTk.PhotoImage(load)
            img = Label(self, image = render)
            img.image = render
            img.pack()
            
      def statistiche(self):

            self.stats = Text(self, width = 40, height = 10, border = 5, bg = "black", fg ="white")
            self.stats.place( x = 10, y = 550)

      def immagineNuova(self, path):
      
            load = Image.open(path)
            render = ImageTk.PhotoImage(load)
            img = Label(schermata, image = render)
            img.image = render
            img.place( x = 10, y = 10 )    
            self.update()  


        
