from GUI import *
from nemici import *


nemico = Nemico()
scheletro = Scheletro()
g = GUI()

class Player:
      
      def __init__(self):
            
            self.nome = '' #Nome
            self.hp = 0    #Health points MAX
            self.hpATM = 0 #Health points 
            self.mp = 0    #Magic points MAX
            self.mpATM = 0 #Magic points
            self.dex = 0   #Destrezza
            self.mAtk = 0  #Attacco magico
            self.atk = 0   #Attacco normale
            self.defence = 0#Difesa
            self.stato = []#Stato
            self.personaggio = ''

      def statisticheAdd(self):

            g.stats.delete('1.0', END)

            g.stats.insert('end', "HP MAX >>" + str(self.hp) + "\t MP MAX >>" + str(self.mp) + "\t HP >>" + str(self.hpATM) + "\t MP >>" + str(self.mpATM) + "\n")

            g.stats.insert('end', "########################################\n")

      def statisticheAgg(self): # DA CREARE UNA A SECONDA DEL NEMICO DA COMBATTERE
            
            g.stats.delete('1.0',END)

            g.stats.insert('end', "HP MAX >>" + str(self.hp) + "\t MP MAX >>" + str(self.mp) + "\t HP >>" + str(self.hpATM) + "\t MP >>" + str(self.mpATM) + "\n")

            g.stats.insert('end', "########################################\n")

            g.stats.insert('end', "\n \t NEMICO!:\nHP >>" + str(scheletro.hp) + "\t MP >>" + str(scheletro.mp))
            

giocatore = Player()

class Arciere(Player):
      def __init__(self):

                  self.nome = giocatore.nome
                  self.hp = 10
                  self.hpATM = 10
                  self.mp = 10
                  self.mpATM = 10
                  self.mAtk = 2.5
                  self.atk = 7
                  self.defence = 4.5
                  self.dex = 15

class Guerriero(Player):
      
      def __init__(self): #Guerriero

            self.nome = giocatore.nome
            self.hp = 25
            self.hpATM = 25
            self.mp = 10
            self.mpATM = 10
            self.mAtk = 3
            self.atk = 15
            self.defence = 10
            self.dex = 5

class Mago(Player):

      def __init__(self): #Mago

            self.nome = giocatore.nome
            self.hp = 7
            self.hpATM = 7
            self.mp = 20
            self.mpATM = 20
            self.mAtk = 15
            self.atk = 7
            self.defence = 5
            self.dex = 5

                  


