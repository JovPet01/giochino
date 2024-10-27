class Nemico:
      
    def __init__(self):
        
        self.nome = '' #Nome
        self.hp = 0    #Health points MAX 
        self.mp = 0    #Magic points MAX
        self.mAtk = 0  #Attacco magico
        self.atk = 0   #Attacco normale
        self.defence = 0#Difesa
        self.stato = []#Stato

    def statisticheAdd(self):

        g.stats.insert('end', "\n \t NEMICO!:\nHP >>" + str(self.hp) + "\t MP >>" + str(self.mp) + "\n")
 

class Scheletro(Nemico):

    def __init__(self):

        self.nome = 'Scheletro'
        self.hp = 5
        self.mp = 5
        self.mAtk = 2.5
        self.atk = 2.5
        self.defence = 2
        self.stato = []
