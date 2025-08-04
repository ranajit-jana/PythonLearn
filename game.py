
import traceback


class GameOverException(Exception):
    pass

class Game:
    def __init__(self):
        self.attempt = 0
        
    def playGame(self):

        if self.attempt >= 5 :
            raise GameOverException
        self.attempt = self.attempt + 1
        print(" Playing the game now")

            
g = Game()
input(" please key to start the game")
try:
    while True:
        g.playGame()
except GameOverException:
    print(" Game over")