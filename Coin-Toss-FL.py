import random
import time

class Player:

    def __init__(self):
      self.coinCount = 5
      self.curentCoinFace = ""

    def flipCoin(self):
      self.curentCoinFace = random.choice(["HEADS","TAILS"])

    def getCurentFace(self):
      return self.curentCoinFace

    def getNumOfCoins(self):
     return self.coinCount

    def addCoin(self):
      self.coinCount = self.coinCount + 1

    def subCoin(self):
       self.coinCount = self.coinCount - 1


class FlipItGame:

  def __init__(self):
    self.player1 = Player()
    self.player2 = Player()

  def flipIt(self):
    self.player1.flipCoin()
    self.player2.flipCoin()
    for i in range(3):
      print("\\")
      time.sleep(.7)
      print("/")
      time.sleep(.7)

    print(f"Player 1 {self.player1.getCurentFace()} Player 2 {self.player2.getCurentFace()}")
    print()
    if self.player1.getCurentFace() == self.player2.getCurentFace():
      self.player1.addCoin()
      self.player2.subCoin()
      print(f"  Player 1 wins the flip!")
      print(f"    Player 1 Coins: {self.player1.getNumOfCoins()}")
      print(f"    Player 2 Coins: {self.player2.getNumOfCoins()}")
    else:
      self.player1.subCoin()
      self.player2.addCoin()
      print("  Player 2 wins the flip!")
      print(f"    Player 1 Coins: {self.player1.getNumOfCoins()}")
      print(f"    Player 2 Coins: {self.player2.getNumOfCoins()}")

  def isGameOver(self):
    return self.player1.getNumOfCoins() == 0 or self.player2.getNumOfCoins() == 0

  def printWinner(self):
    if self.player1.getNumOfCoins() == 0:
      print("")
      print("**PLAYER 2 WINS THE GAME**")
      print("**GAME OVER**")
    if self.player2.getNumOfCoins() == 0:
      print("")
      print("**PLAYER 1 WINS THE GAME**")
      print("**GAME OVER**")

game = FlipItGame()

while True:
  try:
    print("Welcome to FLIP-IT")
    print(" 1  Start Game")
    print(" 2  Exit")
    startVal = int(input("Enter an option:"))

    if startVal == 1:

      while True:     
              print()
              print("Keep Playing")
              print("1  Flip")
              print("2  Exit")
              value = int(input("Enter an option:"))
              
              if value == 1:
                game.flipIt()
                if game.isGameOver():
                  game.printWinner()
                  print()
                  break
                
              elif value == 2:
                break

              else:
                  print("Please enter a number from the menu.")

              print()
    elif startVal == 2:
      break
    
    else:
       print("Please enter a number from the menu.")
    
  except ValueError:
    print("Please enter a number from the menu.")
    print()
