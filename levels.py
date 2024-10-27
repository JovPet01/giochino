from GUI import *
from giocatore import *
from nemici import *
from tkinter import *
import pygame

pygame.init()

giocatore = Player()
arciere = Arciere()
guerriero = Guerriero()
mago = Mago()
scheletro = Scheletro()

g = GUI()

class Livelli():

      def __init__(self): 

            self.premuto = StringVar()
            self.inputUtente = StringVar()
            self.fraseInserita = StringVar()
            self.bottoncino()
            self.inserimenti()
            self.testo()
            
      def cicloLivelli(self):

            self.presentazione()
            self.Livello1Finale()
            self.tutorialBattaglia()
            self.finaleBeta()

      def inserisci(self):
            
            
            self.bottone.wait_variable(self.premuto)
            self.fraseInserita = self.inputUtente.get()
            self.inserimento.delete('0', END)
            return self.fraseInserita
      
      def testo(self):

            self.testo = Text(schermata, width = 110, height = 35, border = 5, bg = "black", fg ="white")
            self.testo.place( x = 400, y = 20 )

      def inserimenti(self):

            large_font = ('calibri', 15)
            self.inserimento = Entry(schermata,font=large_font, textvariable = self.inputUtente, width = 50, border = 5, bg = "black", fg ="white")
            self.inserimento.place( x = 400, y = 650)

      def bottoncino(self):

            self.bottone = Button(schermata, width = 30, height = 3, border = 5, text = "Inserisci", command = lambda:[self.inserisci, self.premuto.set('1')])
            self.bottone.place( x = 1050, y = 650)

      def presentazione(self):

            self.scrivere(">> Salve straniero, qual e' il tuo nome?\n")

            giocatore.nome = self.inserisci()

            if giocatore.nome != '':
                  self.scrivere(">> Il tuo nome e' " + giocatore.nome + "!\n>> Un nome che inspira sicurezza!\n")
                  self.scrivere(">> Ti risvegli in una stanza che non riconosci, la luce diurna illumina la casa.\n")
                  self.scrivere(">> Alzandoti apri la porta principale. 'Dove mi trovo?' pensi... beh, non lo saprai finche' non lo andrai a scoprire!.\n")
            
            while True:

                  self.scrivere(">> Resterai in quella casa oppure comincerai la tua avventura? (Scrivi 'rimarro' oppure 'andro')\n")
                  scelta1 = self.inserisci()
                  if scelta1 == 'rimarro':
                        
                        self.cancellaTesti()
                        self.scrivere(">> Decidi di rimanere li' non passera' tanto che ti renderai conto che dove ti trovi acqua non c' e' n' e' nemmeno a pagare, morirai cosi', di sete, e ancor prima di iniziare, complimenti, pochi ci riescono.")
                        sceltaSbagliata = pygame.mixer.Sound(r"suoni\morte.wav")
                        pygame.mixer.Sound.play(sceltaSbagliata)
                        g.immagineNuova("immagini//morte.png")
                        g.after(3000)
                        sys.exit()
                        break

                  elif scelta1 == 'andro':
                        
                        self.cancellaTesti()
                        self.scrivere(">> Ottimo, ci serve un guerriero cosi' ben intenzionato!\n>> Ma aspetta, da lontano vedi arrivare un'anziana donna, chi sara' mai?\n")
                        self.scrivere("DONNA >> Finalmente sei sveglio straniero, finalmente posso parlarti. Tu sei colui che salvera' il nostro regno dalla dominazione dei Rossimani.\n")
                        self.scrivere("TU >> Io? Un guerriero? Ma lei e' pazza, io nella vita sono uno che sta dalla mattina alla sera seduto su un divano a giocare i videogames!\n")
                        self.scrivere("DONNA >> La leggenda parla chiaro! Sara' un uomo di altri tempi a liberarci, e sembra che tu sia lui.\n")
                        self.scrivere("TU *IN MENTE* >> Ma che sta succedendo!?\n")
                        self.scrivere("DONNA >> Senti, come ti chiami?\n")
                        self.scrivere("TU >> " + giocatore.nome +" piacere.\n")
                        self.scrivere("DONNA >> E' arrivato il momento per te di scegliere un'arma...\n")
                        self.scrivere("TU *URLANDO*>> Cooosa?\n")
                        self.scrivere("DONNA >> Scegli fra una spada, un bastone magico e un arco.\n")
                        break
                        
                  else:
                        self.cancellaTesti()
                        self.scrivere('>> INSERIRE UNA SCELTA VALIDA\n')
                  
            while True:

                  self.scrivere("TU *IN MENTE* >> Sara' una pazza diamogli corda.(Scrivi spada, bastone o arco)\n")
                  sceltaArma = self.inserisci()
                  
                  if sceltaArma == "spada":
                        g.immagineNuova("immagini\\avventuriero.png")
                        self.scrivere(">> Ti senti pervadere da una forza.\n")
                        self.scrivere("TU *IN MENTE* >> Ma che c#*@o?!\n")
                        self.scrivere("DONNA >> Ottima scelta guerriero.\n")
                        giocatore.personaggio = 'Guerriero'
                        g.after(1000)
                        break

                  elif sceltaArma == "bastone":
                        g.immagineNuova("immagini\\mago.png")
                        self.scrivere(">> Vedi intorno al bastone un bagliore azzurro.\n")
                        self.scrivere("TU *IN MENTE* >> Ma che c#*@o?!\n")
                        self.scrivere("DONNA >> Ottima scelta mago.\n")
                        giocatore.personaggio = 'Mago'
                        g.after(1000)
                        break

                  elif sceltaArma == "arco":
                        g.immagineNuova("immagini\\arciere.png")
                        self.scrivere(">> Senti come se tu fossi piu' leggero.\n")
                        self.scrivere("TU *IN MENTE* >> Ma che c#*@o?!\n")
                        self.scrivere("DONNA >> Ottima scelta arciere.\n")
                        giocatore.personaggio = 'Arciere'
                        g.after(1000)
                        break

                  else:
                        self.cancellaTesti()
                        self.scrivere('>> INSERIRE UNA SCELTA VALIDA\n')  

            if giocatore.personaggio == 'Guerriero':
                  sceltaG = pygame.mixer.Sound(r"suoni\Guerriero.wav")
                  pygame.mixer.Sound.play(sceltaG)
                  guerriero.statisticheAdd()
            elif giocatore.personaggio == 'Arciere':
                  sceltaA = pygame.mixer.Sound(r"suoni\Arciere.wav")
                  pygame.mixer.Sound.play(sceltaA)
                  arciere.statisticheAdd()
            elif giocatore.personaggio == 'Mago':
                  sceltaM = pygame.mixer.Sound(r"suoni\Mago.wav")
                  pygame.mixer.Sound.play(sceltaM)
                  mago.statisticheAdd()    

      def scrivere(self, scrittura):

            for char in scrittura:
                  self.testo.insert("insert", char)
                  g.after(25)
                  g.update()

      def cancellaTesti(self):

            self.testo.delete('1.0',END)

      def Livello1Finale(self):

            self.cancellaTesti()
            self.scrivere( ">> Il giovane " + giocatore.nome + " era ora stranito, ma non sapeva ancora quale grande avventura l'aspettase da li' a poco...\n")
            g.update()
            g.after(2000)
            
            self.scrivere(">> Compariranno ora le statistiche nel riquadro in basso a sinistra!\n")
            g.update()
            g.after(1000)
            
      def tutorialBattaglia(self):

            self.cancellaTesti()
            self.scrivere("DONNA >> Ora che hai un'arma dovrai imparare a combattere.\n")
            self.scrivere("TU >> Cio' significa che dovro' uccidere persone?\n")
            self.scrivere("DONNA >> Se servira' farlo, si'.\n")
            self.scrivere("TU >> Servira' farlo?\n")
            self.scrivere("DONNA >> Si'.\n")
            self.scrivere("TU >> MA CHE STAI DICENDO VECCHIA PAZ..\n")
            self.scrivere("DONNA *INTERROMPENDOTI*>> Questo sara' il tuo nemico.\n")
            self.scrivere("\t \t COMPARE :" + scheletro.nome + "\n")
            pygame.mixer.music.load(r"suoni\\combattimenti.wav")
            pygame.mixer.music.play(-1)
            g.after(2500)
            g.update()
            self.cancellaTesti()
            self.scrivere("TU >> CHE C###O E' QUEL COSO!?!?!\n")
            self.scrivere("DONNA >> Uno scheletro...\n")
            self.scrivere("TU >> DA DOVE C###O E' SBUCATO\n")
            self.scrivere("DONNA >> In realta' qui in giro ce ne saranno a centinaia...\n")
            self.scrivere("TU >> COOOOSAAA!\n")
            self.scrivere("DONNA >> Ora cominciamo.\n")

            if giocatore.personaggio == 'Guerriero':

                  self.scrivere("DONNA >> Fammi vedere come te la cavi con la spada.\n")
                  self.scrivere("TU >> MA IO NON L'HO MAI FATTO, L'HO SOLO VISTO NEI VIDEOGAMES!\n")
                  self.scrivere("DONNA >> Bene allora prova a fare cio' che hai visto...\n")

                  while scheletro.hp >= 0:
                        
                        self.scrivere("\t \t SCRIVI ATTACCA PER ATTACCARE!")
                  
                        scelta1 = self.inserisci()

                        if scelta1 == 'attacca':
                              
                              danniInflitti = 0
                              danniInflitti = (guerriero.atk - scheletro.defence) - scheletro.hp
                              scheletro.hp -= danniInflitti
                              self.scrivere(">> Hai inflitto:" + str(danniInflitti) + "\n")
                              self.scrivere("TU *URLANDO*>> PRENDI QUESTO BESTIA IMMONDA!\n")
                              self.scrivere("DONNA >> Ora e' il turno del nemico.\n")

                              danniInflitti = 0

                              danniInflitti = (scheletro.atk - guerriero.defence) - guerriero.hpATM
                              
                              if danniInflitti <= 0:
                                    
                                    guerriero.hpATM = guerriero.hpATM
                                    self.scrivere(">> Il nemico ha inflitto: 0\n")
                                    self.scrivere("TU >> Ma sto coso non fa danno...\n")
                              else:

                                    guerriero.hpATM -= danniInflitti
                                    self.scrivere(">> Il nemico ha inflitto:" + str(danniInflitti) + "\n")
                                    self.scrivere("TU >> AIAH!\n")

                              guerriero.statisticheAgg()
                              
                        else:
                              self.cancellaTesti()
                              self.scrivere('>> INSERIRE UNA SCELTA VALIDA\n')
                        
                        self.scrivere("\t \t    IL NEMICO E' STATO SCONFITTO!\n")
                        guerriero.statisticheAdd()
                        pygame.mixer.music.stop()
                        vittoria = pygame.mixer.Sound(r"suoni\\vittoria.wav")
                        pygame.mixer.Sound.play(vittoria)
                        g.after(1000)
                        g.update()
                        self.scrivere("DONNA >> Ottimo, " + giocatore.nome + " e' andata meglio del previsto a quanto pare.\n")
                        self.scrivere("TU >> MA QUEL COSO MI HA MORSO.\n")
                        self.scrivere("DONNA >> Ci sono mostri peggiori di quello caro avventuriero...\n")
                        self.scrivere("TU >> E non ci tengo a incontrarli, io andrei a casa mia se non le dispia...\n")
                        self.scrivere("DONNA *INTERROMPENDOTI* >> Dai il via al tuo viaggio avventuriero! Sei pronto! *scompare*\n")
                        self.scrivere("TU >> OH E IO COME ME NE VADO DA QUA?\nTU >> Dio cosa ho fatto per meritarmi questo... vabbe' incamminiamoci, vediamo che troviamo...\n")
                        g.after(1000)
                        g.update()


            
            elif giocatore.personaggio == 'Mago':

                  self.scrivere("DONNA >> Fammi vedere come te la cavi con gli incantesimi.\n")
                  self.scrivere("TU >> MA IO NON L'HO MAI FATTO, L'HO SOLO VISTO NEI VIDEOGAMES!\n")
                  self.scrivere("DONNA >> Bene allora prova a fare cio' che hai visto...\n")
                  pass

            elif giocatore.personaggio == 'Arciere':

                  self.scrivere("DONNA >> Fammi vedere come te la cavi con l'arco.\n")
                  self.scrivere("TU >> MA IO NON L'HO MAI FATTO, L'HO SOLO VISTO NEI VIDEOGAMES!\n")
                  self.scrivere("DONNA >> Bene allora prova a fare cio' che hai visto...\n")
                  pass
            
      def finaleBeta(self):

            self.cancellaTesti()
            self.scrivere(">> PER ORA LA DEMO DEL GIOCO FINISCE QUI, FAMMI SAPERE COSA NE PENSI!")
            g.update()
            g.after(3000)     
            sys.exit()      


                  

            
