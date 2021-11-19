"""
Tarea 2.9 Consulta sobre Minimax con poda Alfa-Beta

Equipo: 3

Nombre: Piña Rosales Cristian Gabriel 
Número de Control: 18130588

Nombre: Adame Sandoval José Misael
Número de Control: 18131209

Nombre: Castro Luna Ricardo Raúl
Número de Control: 18131227

Nombre: Flores Ramos José Luis
Número de Control: 18131237

Nombre: Ruiz Martínez Kevin Alejandro
Número de Control: 18131280
"""


# Esto es un codigo realizado por omegadeep10 de github
# El algoritmo solo usa el minimax en su forma mas simple
# Se señalaron las partes importantes del codigo
# y se realizo una modificacion para lograr que el algoritmo se transformara en minmax poda alfa beta.
# Esta modificacion puede ser vista en la linea 169 de este codigo.

import random

class TicTacToe:

    def __init__(self):
        """Initialize with empty board"""
        self.board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == "X":
            return "X"
        elif self.checkWin() == "O":
            return "O"
        elif self.gameOver() == True:
            return "Nobody"

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        """Make a move on the board"""
        self.board[position] = player

    def checkWin(self):
        """Return the player that wins the game"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    # Para hacer que este algoritmo sea minmax poda alfa beta
    # Solo hay que modificar la operacion de retorno
    def minimax(self, node, depth, player):
        """
        Recursively analyze every possible game state and choose
        the best move location.
        node - the board
        depth - how far down the tree to look
        player - what player to analyze best move for (currently setup up ONLY for "O")
        """
        # Retorn a un resultado final
        if depth == 0 or node.gameOver():
            if node.checkWin() == "X":
                return 0
            elif node.checkWin() == "O":
                return 100
            else:
                return 50
        
        # Maximzar al la maquina
        if player == "O":
            bestValue = 0
            for move in node.availableMoves():
                node.makeMove(move, player) # Hace el movimiento
                moveValue = self.minimax(node, depth-1, changePlayer(player)) # Analiza las probabilidades
                node.makeMove(move, " ") # Deshace el movimiento
                bestValue = max(bestValue, moveValue) # Regresa el maximo
            return bestValue
        
        # Minimizar al jugador
        if player == "X":
            bestValue = 100
            for move in node.availableMoves():
                node.makeMove(move, player)
                moveValue = self.minimax(node, depth-1, changePlayer(player))
                node.makeMove(move, " ")
                bestValue = min(bestValue, moveValue)
            return bestValue

def changePlayer(player):
    """Returns the opposite player given any player"""
    if player == "X":
        return "O"
    else:
        return "X"


# Para hacer que este algoritmo sea minmax poda alfa beta
# Solo hay que modificar la operacion de retorno
def make_best_move(board, depth, player):
    """
    Controllor function to initialize minimax and keep track of optimal move choices
    board - what board to calculate best move for
    depth - how far down the tree to go
    player - who to calculate best move for (Works ONLY for "O" right now)
    """
    neutralValue = 50
    choices = []
    for move in board.availableMoves():
        board.makeMove(move, player)
        moveValue = board.minimax(board, depth-1, changePlayer(player))
        board.makeMove(move, " ")
        # Aqui es donde hacemos la poda para agilizar el algoritmo
        # solo tenemos que detener el algoritmo al encontrar el movimiento con mayor valor posible
        # Se pusieron  estos parametros de debug para ver como se comporta
        # Dado a que el algoritmo tiene posibilidad de ser empatado,
        # El mismo juego nos invita a ver los demas resultados hasta encontrar el maximo valor para la IA
        # en este caso solo se agrego una comparacion para evitar revisar o "podar" todos los demas nodos  

        print("posicion de movimiento: "+str(move))
        print("Valor de  movimiento: "+str(moveValue))

        if moveValue == 100 : # Se opto por esta condicion dado a que cualquier movimiento que sea mayor que 0 nos da mejor velocidad
            return move
        ## Aqui termina mi modificacion para hacer que el algoritmo sea minimax poda alfa beta
        
        if moveValue > neutralValue:
            choices = [move]
            break
        elif moveValue == neutralValue:
            choices.append(move)
    print("choices: ", choices)

    # El mismo algoritmo nos hace considerar que hay posibilidades de que no encontremos jugadas ganadoras
    if len(choices) > 0:
        return random.choice(choices) # Si hay mas de una jugada de 100, devuelve cualquiera de esos movimientos
    else:
        return random.choice(board.availableMoves()) # Si no hay jugadas ganadoras, devuelve cualquier jugada posible




#Actual game
if __name__ == '__main__':
    game = TicTacToe()
    game.show()
    print("Codigo analizado y modificaco por el equipo 3")

    while game.gameOver() == False:
        person_move = int(input("You are X: Choose number from 1-9: "))
        game.makeMove(person_move-1, "X")
        game.show()

        if game.gameOver() == True:
            break

        print("Computer choosing move...")
        ai_move = make_best_move(game, -1, "O")
        print("movimiento de la maquina: ")
        print(str(ai_move))
        game.makeMove(ai_move, "O")
        game.show()

    print("Game Over. " + game.whoWon() + " Wins")

