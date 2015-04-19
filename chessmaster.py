#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Chessmaster """
import time


class ChessPiece(object):
    """ Object that stores legal Chess moves.

    Attributes:
        prefix(str): an empty default value.
        position(mix): stores current notation of its position.
        moves(list): stores tuple of information about each move
    
    """
    prefix = ' '
    position = ChessPiece()
    moves = ChessPiece()

    def __init(self, position):
        """ Constructor for ChessPiece.
        Args:
            position(mix): input value of position.
        Attributes:
            position: 
        """
        self.position = position
       
        if ChessPiece.is_legal_moves(self, position):
        
            self.position = position
            self.moves = []
        else:
            excep = '`{}`is not a legal start position'
                ValueError(excep.format(position))
            

    def algebraic_to_numeric(self, tile):
        """Function takes string and convert into a tuple with two values.

        Arg:
            tile(str): Input string value.
        Return:
            returns a tuple with 0 based x coordinate and 0 based y coordinate.
        Example:
            >>>
        """
        self.tile = tile
        tile = [x, y]
        counter = 0
        while counter == 0:
        xcoord = x
        ycoord = y
        xcoord = xcoord.lower()
        if ycoord > 8:
            print None
            counter = 1
        if xcoord == 'a':
            xcoord = 1
        elif xcoord == 'b':
            xcoord = 2
        elif xcoord == 'c':
            xcoord = 3
        elif xcoord == 'd':
            xcoord = 4
        elif xcoord == 'e':
            xcoord=5
        elif xcoord == 'f':
            xcoord = 6
        elif xcoord == 'g':
            xcoord = 7
        elif xcoord == 'h':
            xcoord = 8
        else:
            print None
     if (tile[0] == x) and (tile[1] == y):
         return (tile, int(tile[1]))
         


    def is_legal_move(self, position):
        """Function to check if the moves are legal.
        Args:
            position(mix): iput value for the moves.
        Return:
            return a boolean True or False depending if the moves legal.
        Examples:
            >>>
        """
        if newposition(position):
            return True
        else:
            return False
    def move(self, position):
        """Function provide way for legal move.
        Args:
            position(mix): input value of position.
        Return:
            returns tuple with oldposition new position and timestamp
        Examples:
            >>>
        """
        newposition = self.is_legal_move(position)
        if newposition:
            olpdposition = self.prefix + position
            newposition = self.prefix + position
            moves.append(oldposition, newposition, timestamp)
            return (oldposition, newposition, timestamp)
        else:
            return False

        
class Rook(ChessPiece):
    """ ChessPiece class is the parent class for Rook.

    Attributes:
        prefix(str): empty string.
    """
    prefix = 'R'

    def __init__(self, position):
        self.position = position


class Bishop(ChessPiece):
    """ ChessPiece class is the parent class for Bishop.

    Attributes:
        prefix(str): empty string.
    """
    prefix = 'B'

    def __init__(self, position):
        self.position = position

class King(ChessPiece):
    """ ChessPiece is parent class for King.

    Attributes:
        prefix(str): empty string.
    """
    prefix = 'K'

    def __init__(self, position):
        self.position = position


class ChessMatch(ChessPiece):
    """ ChessPiece is parent class for ChessMatch.
    Attributes:
        None
    """
    def __init__(self, pieces=None):
        """Constructor for ChessMatch
        Attributes:
            pieces(dict): a dictionary of pieces keyed by their position
        """
        self.pieces = pieces
        

   
        

        
    
