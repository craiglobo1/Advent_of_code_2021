from typing import *
from copy import copy
from dataclasses import dataclass, field
import numpy

with open("d4_input.txt", "r") as rf:
    lines = rf.readlines()
    lines = [ val.strip()for val in lines]

@dataclass
class bingo_draw_no:
    number : int
    marked : bool = False

@dataclass
class Bingo_card:
    board : List[int]
    won : bool = False
    winning_values : List[int] = field(default_factory=lambda:[])
    winning_value : int = 0

def pt1(lines):

    draw = list(map(lambda x: int(x), lines.pop(0).split(",")))

    lines.pop(0)

    bingo_cards = []

    for i in range((len(lines)-1)//5):
        bingo_card = []
        for j in range(5):
            if len(lines) > 0:
                cur_line = lines.pop(0)
                row = filter(lambda x: x != "", cur_line.split(" "))
                row = [bingo_draw_no(int(val)) for val in row]
                bingo_card.append(row)

        bingo_cards.append(bingo_card)
        if len(lines) > 0:
            lines.pop(0)

    completed_row = False
    completed_col = False
    broken_at = 0
    number_won_at = 0
    for i, draw_no in enumerate(draw):
        for bingo_card_num, bingo_card in enumerate(bingo_cards):
            for row in bingo_card:
                for val in row:
                    if draw_no == val.number:
                        val.marked = True


                if completed_row := not (False in list(map(lambda x: x.marked, row))):
                    broken_at = bingo_card_num
                    number_won_at = draw_no
                    break
            if completed_row:
                break

            for col_idx in range(len(bingo_card)):
                col = []
                for row_idx in range(len(bingo_card)):
                    val = bingo_card[col_idx][row_idx]
                    col.append(val.marked)
                if completed_col := not (False in col):
                    broken_at = bingo_card_num
                    number_won_at = draw_no
                    break
                
        if completed_row or completed_col:
            break

    flat_board = [ val for row in bingo_cards[broken_at] for val in row]
    flat_board = list(filter(lambda x: x.marked == False, flat_board))
    sum_unmarked_nums = sum(list(map(lambda x: x.number, flat_board)))
    return sum_unmarked_nums*number_won_at

def pt2(lines):

    draw = list(map(lambda x: int(x), lines.pop(0).split(",")))

    lines.pop(0)

    bingo_cards = []

    for i in range((len(lines)-1)//5):
        bingo_card = []
        for j in range(5):
            if len(lines) > 0:
                cur_line = lines.pop(0)
                row = filter(lambda x: x != "", cur_line.split(" "))
                row = [bingo_draw_no(int(val)) for val in row]
                bingo_card.append(row)

        bingo_cards.append(Bingo_card(bingo_card))
        if len(lines) > 0:
            lines.pop(0)

    lastToWin = None
    for i, draw_no in enumerate(draw):
        for bingo_card_num, bingo_card in enumerate(bingo_cards):
            wonAlready = False
            if not bingo_card.won:
                for row in bingo_card.board:
                    for val in row:
                        if draw_no == val.number:
                            val.marked = True


                    if not (False in list(map(lambda x: x.marked, row))):
                        wonAlready= True
                        bingo_card.won = True
                        bingo_card.winning_values = row
                        bingo_card.winning_value = draw_no
                        lastToWin = bingo_card
                
                t_bingo_card = copy(bingo_card)
                t_bingo_card.board = numpy.transpose(t_bingo_card.board)

                for col in t_bingo_card.board:
                    if not (False in list(map(lambda x: x.marked, col))) and not wonAlready:
                        bingo_card.won = True
                        bingo_card.winning_values = col
                        bingo_card.winning_value = draw_no
                        lastToWin = bingo_card

    flat_board = [ val for row in lastToWin.board for val in row]
    flat_board = list(filter(lambda x: x.marked == False, flat_board))
    sum_unmarked_nums = sum(list(map(lambda x: x.number, flat_board)))
    return sum_unmarked_nums*lastToWin.winning_value

print(pt1(copy(lines)))
print(pt2(copy(lines)))



