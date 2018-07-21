import tkinter
from tkinter import *
import math

#Font
default = ('Helvetica', 14)

class Board:
    def __init__(self, row:int, col:int, first:str, how:str):
        self.rows = row
        self.columns = col
        self.turn = first
        self.how_won = how

        ######

        self.command_window = tkinter.Toplevel()
        self.window = tkinter.Toplevel()
        self._canvas = tkinter.Canvas(master = self.window, width = 500, height = 500,
                                      background = '#B9005D')
        self._canvas.grid(row = 0, column = 0, padx = 10, pady = 10,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas.bind('<Configure>', self.resize_canvas)
        self._canvas.bind('<Button-1>', self.canvas_clicked)

        self.window.rowconfigure(0, weight = 1)
        self.window.columnconfigure(0, weight = 1)


class FirstInput:
    def __init__(self):
        self.window = tkinter.Tk()

        self.rows = 0
        self.columns = 0
        self.first_move = ''
        self.how_won = ''

        self.simple_text = tkinter.Label(master = self.window, text = 'SIMPLE', font = default)
        self.simple_text.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W+
                         tkinter.E+tkinter.N)

        ## ROW ##
        self.row_text = tkinter.Label(master = self.window, text = 'ROWS', font = default)
        self.row_text.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self.row_scale = Scale(master = self.window, from_=4, to = 16, tickinterval = 2,
                          orient = HORIZONTAL, command = self.row_set, length = 300, resolution = 2)
        self.row_scale.grid(row = 1, column = 1, padx = 10, pady = 10)
        

        ## COLUMN ##
        self.col_text = tkinter.Label(master = self.window, text = 'COLUMNS', font = default)
        self.col_text.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self.col_scale = Scale(master = self.window, from_=4, to = 16, tickinterval = 2,
                          orient = HORIZONTAL, command = self.col_set, length = 300, resolution = 2)
        self.col_scale.grid(row = 2, column = 1, padx = 10, pady = 10)
        

        ## FIRST ##
        self.first_text = tkinter.Label(master = self.window, text = 'FIRST MOVE', font = default)
        self.first_text.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = tkinter.E)

        ''' W '''
        self.w = tkinter.Button(master = self.window, text = 'W', font = default,
                                 command = self.white)
        self.w.grid(row = 1, column = 3, padx = 10, pady = 10)

        ''' B '''
        self.b = tkinter.Button(master = self.window, text = 'B', font = default,
                                 command = self.black)
        self.b.grid(row = 1, column = 4, padx = 10, pady = 10)
        
        ## HOW WON ##
        self.won_text = tkinter.Label(master = self.window, text = 'HOW WON', font = default)
        self.won_text.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = tkinter.E)

        self.greater = tkinter.Button(master = self.window, text = '>', font = default, command =
                           self.greater)
        self.greater.grid(row = 2, column = 3, padx = 10, pady = 10, sticky = tkinter.E)

        self.lesser = tkinter.Button(master = self.window, text = '<', font = default, command =
                             self.lesser)
        self.lesser.grid(row = 2, column = 4, padx = 10, pady = 10, sticky = tkinter.E)

        ## DONE ##
        self.done = tkinter.Button(master = self.window, text = "DONE", font = default,
                              command = self.done)
        self.done.grid(row = 3, column = 0, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E
                  + tkinter.S)
        ## Test Slider##
            
    def row_set(self, value):
        self.rows = int(value)
    def col_set(self, value):
        self.columns = int(value)
    def white(self):
        self.first_move = 'W'
    def black(self):
        self.first_move = 'B'
    def greater(self):
        self.how_won = '>'
    def lesser(self):
        self.how_won = '<'
    def done(self):
        if self.rows != 0 and self.columns != 0 and self.first_move != '' and self.how_won != '':
            self.row_scale.destroy()
            self.col_scale.destroy()
            self.w.destroy()
            self.b.destroy()
            self.greater.destroy()
            self.lesser.destroy()
            self.row_new_text = tkinter.Label(master = self.window, text = self.rows, font = default)
            self.row_new_text.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.W)
            self.col_new_text = tkinter.Label(master = self.window, text = self.columns, font = default)
            self.col_new_text.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.W)
            self.first_new_text = tkinter.Label(master = self.window, text = self.first_move, font = default)
            self.first_new_text.grid(row = 1, column = 3, padx = 10, pady = 10, sticky = tkinter.W)
            self.won_new_text = tkinter.Label(master = self.window, text = self.how_won, font = default)
            self.won_new_text.grid(row = 2, column = 3, padx = 10, pady = 10, sticky = tkinter.W)
            board = Board(self.rows, self.columns, self.first_move, self.how_won)
        else:
            pass
        

    def start(self) -> None:
        self.window.mainloop()

if __name__ == '__main__':
    FirstInput().start()
