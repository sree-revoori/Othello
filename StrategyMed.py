import math
import queue
from cmu_112_graphics import *


''' This file is the algorithm for the medium AI - A* graph search implemented with priority queue'''
class Strategy:

    def best_strategy(self, board, player):
        return self.ASTAR(board, player, 3)

    def ASTAR(self, board, player, depth):
        q = queue.PriorityQueue()
        q.put((self.score_board(board), board, player, 0))
        BestScore, BestMove = self.score_board(board), None
        m = {}
        while not q.empty():
            score, curr_board, curr_player, curr_depth = q.get()
            opponent = {"o": "@", "@": "o"}[player]
            if curr_depth < depth:
                for move in self.legal_moves(curr_board, curr_player):

                    new_board = self.move(board, player, move)
                    new_player = self.get_next_player(new_board, opponent)
                    new_score = self.score_board(new_board)

                    if curr_depth == 0:
                        if move not in m:
                            m[move] = [new_score]
                        else: m[move].append(new_score)

                    q.put((new_score, new_board, new_player, curr_depth + 1))

        # every original move has a list of resulting scores later in the game
        best_move = None
        best_score = math.inf
        for original_move in m:
            board_scores = m[original_move]
            avg_score = sum(board_scores) / len(board_scores)
            if best_move is None or avg_score < best_score:
                best_score = avg_score
                best_move = original_move

        return best_move

    def get_next_player(self, new_board, opponent):
        player = {"o": "@", "@": "o"}[opponent]
        moves_player = len(self.legal_moves(new_board, player))
        moves_opponent = len(self.legal_moves(new_board, opponent))

        if moves_opponent > 0:
            return opponent
        elif moves_player > 0:
            return player
        else:
            return "?"

    def score_board(self, board):

        mobility_mult = 10

        weights = [0,   0,   0,  0,  0,  0,  0,   0,   0, 0,
             0, 120, -25, 20,  5,  5, 20, -25, 120, 0,
             0, -25, -40, -5, -5, -5, -5, -40, -25, 0,
             0, 20,  -5,  15,  5,  5, 15,  -5,  20, 0,
             0,  5,  -5,   5,  5,  5,  5,  -5,   5, 0,
             0,  5,  -5,   5,  5,  5,  5,  -5,   5, 0,
             0, 20,  -5,  15,  5,  5, 15,  -5,  20, 0,
             0, -25, -40, -5, -5, -5, -5, -40, -25, 0,
             0, 120, -25, 20,  5,  5, 20, -25, 120, 0,
             0,   0,   0,  0,  0,  0,  0,   0,   0, 0
        ]

        blackrating = 0
        whiterating = 0

        for i in range(0, 100):
            if board[i] is "o":
                whiterating += weights[i]
            if board[i] is "@":
                blackrating += weights[i]

        bnum = len(self.legal_moves(board, "@"))
        wnum = len(self.legal_moves(board, "o"))

        return (mobility_mult * (bnum-wnum)) + (blackrating-whiterating)

    @staticmethod
    def move(board, symbol, index):
        board = board[0:index] + symbol + board[index + 1:]
        temp = []
        x = index
        if symbol is "o":
            enemysymbol = "@"
        else:
            enemysymbol = "o"

        if board[x - 1] is enemysymbol:
            loop = 1
            while board[x - loop] is enemysymbol:
                temp.append(x - loop)
                loop += 1
            if board[x - loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        if board[x + 1] is enemysymbol:
            loop = 1
            while board[x + loop] is enemysymbol:
                temp.append(x + loop)
                loop += 1
            if board[x + loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        if board[x - 10] is enemysymbol:
            loop = 10
            temp.append(x - loop)
            loop = 10
            while board[x - loop] is enemysymbol:
                temp.append(x - loop)
                loop += 10
            if board[x - loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        if board[x + 10] is enemysymbol:

            loop = 10
            while board[x + loop] is enemysymbol:
                temp.append(x + loop)
                loop += 10
            if board[x + loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        if board[x - 9] is enemysymbol:
            loop = 9
            while board[x - loop] is enemysymbol:
                temp.append(x - loop)
                loop += 9
            if board[x - loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        if board[x + 9] is enemysymbol:
            loop = 9
            while board[x + loop] is enemysymbol:
                temp.append(x + loop)
                loop += 9
            if board[x + loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        if board[x - 11] is enemysymbol:
            loop = 11
            while board[x - loop] is enemysymbol:
                temp.append(x - loop)
                loop += 11
            if board[x - loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        if board[x + 11] is enemysymbol:
            loop = 11
            while board[x + loop] is enemysymbol:
                temp.append(x + loop)
                loop += 11
            if board[x + loop] is symbol:
                for each in temp:
                    board = board[0: each] + symbol + board[each + 1:]
        temp = []

        return board

    @staticmethod
    def legal_moves(board, symbol):
        if symbol is "o":
            enemysymbol = "@"
        else:
            enemysymbol = "o"
        pmove = []
        for x in range(10, 89):
            if board[x] is not ".":
                continue
            if board[x - 1] is enemysymbol:
                loop = 1
                while board[x - loop] is enemysymbol:
                    loop += 1
                if board[x - loop] is symbol:
                    pmove.append(x)

            if board[x + 1] is enemysymbol:
                loop = 1
                while board[x + loop] is enemysymbol:
                    loop += 1
                if board[x + loop] is symbol:
                    pmove.append(x)

            if board[x - 10] is enemysymbol:
                loop = 10
                while board[x - loop] is enemysymbol:
                    loop += 10
                if board[x - loop] is symbol:
                    pmove.append(x)

            if board[x + 10] is enemysymbol:
                loop = 10
                while board[x + loop] is enemysymbol:
                    loop += 10
                if board[x + loop] is symbol:
                    pmove.append(x)

            if board[x - 9] is enemysymbol:
                loop = 9
                while board[x - loop] is enemysymbol:
                    loop += 9
                if board[x - loop] is symbol:
                    pmove.append(x)

            if board[x + 9] is enemysymbol:
                loop = 9
                while board[x + loop] is enemysymbol:
                    loop += 9
                if board[x + loop] is symbol:
                    pmove.append(x)

            if board[x - 11] is enemysymbol:
                loop = 11
                while board[x - loop] is enemysymbol:
                    loop += 11
                if board[x - loop] is symbol:
                    pmove.append(x)

            if board[x + 11] is enemysymbol:
                loop = 11
                while board[x + loop] is enemysymbol:
                    loop += 11
                if board[x + loop] is symbol:
                    pmove.append(x)

        k = set(pmove)
        pmove = list(k)
        return pmove


