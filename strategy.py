import math

from cmu_112_graphics import *

#This is the hard AI's algorithm - minimax with alpha-beta pruning and IDS
class Strategy:

    def best_strategy(self, board, player):
        depth = 2

    
        if board.count(".") < 5:
            return self.minimax(board, player, board.count("."), -math.inf, math.inf)[0]
        else:
            depth += 1
            return self.minimax(board, player, depth, -math.inf, math.inf)[0]


    def minimax(self, board, player, depth, alpha, beta):
        opponent = {"o": "@", "@": "o"}[player]
        best = {"o": min, "@": max}
        if depth == 0:
            score = self.score_board(board)
            return None, score
        possible = []

        for move in self.legal_moves(board, player):

            new_board = self.move(board, player, move)
            new_player = self.get_next_player(new_board, opponent)

            if new_player == "?":
                score = (new_board.count("@") - new_board.count("o")) * 10000
                possible.append((move, score))
            else:
                score = self.minimax(new_board, new_player, depth-1, alpha, beta)[1]
                possible.append((move, score))


            if best[player] is max:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)

            if alpha >= beta:
                break

        return best[player](possible, key=lambda x: x[1])

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



