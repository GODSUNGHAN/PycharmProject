import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ", "X", "O", "X", " ", " ", " ", " ", " "]

        def dispaly(self):
            print(" %s l %s l %s" %(self.cells[1], self.cells[2], self.cells[3]))
            print(" %s l %s l %s" %(self.cells[4], self.cells[5], self.cells[6]))
            print(" %s l %s l %s" %(self.cells[7], self.cells[8], self.cells[9]))

board = Board()
board.display()