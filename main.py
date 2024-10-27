from GUI import *
from levels import *
import pygame

pygame.init()

if __name__ == "__main__":

      a = GUI()
      l = Livelli()
      pygame.mixer.music.load(r"suoni\\background.wav")
      pygame.mixer.music.play(-1)
      l.cicloLivelli()
      a.mainloop()