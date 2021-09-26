"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        square = board.find_piece(self)
        squareToMoveTo = Square.at(square.row + 1, square.col)
        if self.player == Player.WHITE:
            return [
                squareToMoveTo
            ]
        else:
            return [
                square
            ]

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        square = board.find_piece(self)
        squareMoveWhite = Square.at(square.row + 1, square.col)
        squareMoveWhite2 = Square.at(square.row + 2, square.col)
        squareMoveBlack = Square.at(square.row - 1, square.col)
        squareMoveBlack2 = Square.at(square.row - 2, square.col)
        if self.player == Player.WHITE:
            if square.row == 7:  # top of board
                return []
            if board.get_piece(square.at(square.row + 1, square.col)) is not None:  # obstruction
                return []
            if square.row == 1:  # starting position
                return [
                    squareMoveWhite,
                    squareMoveWhite2
                ]
            else:
                return [
                    squareMoveWhite
                ]
        else:
            if board.get_piece(square.at(square.row - 1, square.col)) is not None:
                return []
            if square.row == 6:
                return [
                    squareMoveBlack,
                    squareMoveBlack2
                ]
            elif square.row == 0:
                return []
            else:
                return [
                    squareMoveBlack
                ]


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []