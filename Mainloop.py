#Project 5 RYAN COX ID#31953949
import tkinter
from tkinter import *
import math
import Logic as logic


#Font
default = ('Helvetica', 14)

class Board:
    def __init__(self, row:int, col:int, first:str, how:str):
        self.rows = row
        self.columns = col
        self.turn = first
        self.how_won = how

        ######

        self.window = tkinter.Toplevel()
        self._canvas = tkinter.Canvas(master = self.window, width = 500, height = 500,
                                      background = '#B9005D')
        self._canvas.grid(row = 0, column = 0, padx = 10, pady = 10,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas.bind('<Configure>', self.resize_canvas)
        self._canvas.bind('<Button-1>', self.canvas_clicked)

        self.window.rowconfigure(0, weight = 1)
        self.window.columnconfigure(0, weight = 1)

        self.draw_grid()

        #LIST VARIABLES
        self.possible_moves = self.possible_spots_list()
        self.logic_list = self.game_logic_list()
        self.move_board = self.copy_logic_board()

        """START"""
        self.start = tkinter.Button(master = self.window, text = "START", font = default,
                               command = self.start_button)
        self.start.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.S + tkinter.E + tkinter.W)
       
        
##### CANVAS #####

    def resize_canvas(self, event: tkinter.Event) -> None:
        self._redraw_all_spots()

    def _redraw_all_spots(self) -> None:
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

    def canvas_clicked(self, event: tkinter.Event) -> None:
        pass
    
##### GRID #####

    def draw_grid(self) -> None:
        self.draw_rectangles()
        self.possible_spots_draw()

    def draw_rectangles(self):
        canvas = self._canvas
        rows = self.rows
        columns = self.columns
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        cell_height = canvas_height/rows
        cell_width = canvas_height/columns


        for i in range(rows + 1):
            x1 = 0
            y1 = 0
            for j in range(columns + 1):
                x1 = x1
                y1 = y1
                x2 = int((i * cell_width)* 500)
                y2 = int((i*cell_height)* 500)
                canvas.create_rectangle(x1,y1,x2,y2, outline = 'black')
                x1 += (cell_width*500)
                y1 += (cell_height*500)

    def possible_spots_draw(self):
        ''' finds the number of possible spots and draws them'''
        possible_spots_list = self.rows * self.columns

        canvas = self._canvas
        rows = self.rows
        columns = self.columns
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        cell_height = canvas_height/rows
        cell_width = canvas_height/columns
        radius = 1
        
        y1 = (cell_height*500)/2
        y2 = (cell_height*500)/2
        
        for i in range(rows+ 1):
            if i == 0:
                pass
            else:
                x1 = (cell_width*500)/2
                y1 = y1
                x2 = (cell_width*500)/2
                y2 = y2
                if i == 1:
                    pass
                else:
                     y1 += (cell_height*500)
                     y2 += (cell_height*500)
                for j in range(columns + 1):
                    if j == 0:
                        pass
                    else:
                        x1 = x1 - radius
                        y1 = y1 - radius
                        x2 = x2 + radius
                        y2 = y2 + radius
                        canvas.create_oval(x1,y1,x2,y2, fill = 'black')
                        x1 += radius
                        y1 += radius
                        x2 -= radius
                        y2 -= radius
                        x1 += (cell_width*500)
                        x2 += (cell_width*500)
##### COLORS #####

    def change_turn(self):
        '''submits the made turn'''
        rows = self.rows
        columns = self.columns
        turn = self.turn
        how_won = self.how_won
        board = self.logic_list
        
        game_state = logic.OthelloClass(board, rows, columns, turn, how_won)
        
        if self.turn == 'W':
            color = self.place_color_black
            self.turn = 'B'
            logic.OthelloClass.change_turn(self.game_state)
        elif self.turn == 'B':
            color = self.place_color_white
            self.turn = 'W'
            self.game_state.turn = 'W'
            logic.OthelloClass.change_turn(self.game_state)

        self._canvas.bind('<Button-1>', color)
        
    def place_color_black(self, event: tkinter.Event):
        ''' places color '''
        logic_list = self.logic_list
        canvas = self._canvas
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width
        click_point = [event.x, event.y]
        possible_spots = self.possible_moves
        circle_radius = 10
        cell_height = int((500/self.rows))
        cell_width = int((500/self.columns))
        color = ''
        letter = ''

        if self.turn == 'B':
            color = 'black'
        else:
            color = 'white'

        if self.turn == 'B':
            letter = 'B'
        else:
            letter = 'W'
        
        #circle radius
        if self.columns > self.rows:
            circle_radius = int((500/self.columns)/2) - 5
        else:
            circle_radius = int((500/self.rows)/2) - 5

        #spots
        for i in possible_spots:
            x = event.x
            y = event.y
            if x >= (i[0] - int((500/self.columns)/2)) and x <= (i[0] + int((500/self.columns)/2)) and y >= (i[1] - int((500/self.rows)/2)) and y <= (i[1] + int((500/self.rows)/2)):
                x1 = i[0] - circle_radius
                y1 = i[1] - circle_radius
                x2 = i[0] + circle_radius
                y2 = i[1] + circle_radius
                canvas.create_oval(x1,y1, x2,y2, fill = 'black', outline = 'white')
                possible_spots.remove(i)
                for i in range(self.columns):
                    for j in range(self.rows):
                        if x > (i*cell_width) and x < ((i+1)*cell_width) and y > (j*cell_height) and y < ((j+1)*cell_height):
                            self.logic_list[j][i] = letter
                            
    def place_color_white(self, event: tkinter.Event):
        ''' places color '''
        logic_list = self.logic_list
        canvas = self._canvas
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width
        click_point = [event.x, event.y]
        possible_spots = self.possible_moves
        circle_radius = 10
        cell_height = int((500/self.rows))
        cell_width = int((500/self.columns))
        color = ''
        letter = ''

        if self.turn == 'B':
            color = 'black'
        else:
            color = 'white'

        if self.turn == 'B':
            letter = 'B'
        else:
            letter = 'W'
        
        #circle radius
        if self.columns > self.rows:
            circle_radius = int((500/self.columns)/2) - 5
        else:
            circle_radius = int((500/self.rows)/2) - 5

        #spots
        for i in possible_spots:
            x = event.x
            y = event.y
            if x >= (i[0] - int((500/self.columns)/2)) and x <= (i[0] + int((500/self.columns)/2)) and y >= (i[1] - int((500/self.rows)/2)) and y <= (i[1] + int((500/self.rows)/2)):
                x1 = i[0] - circle_radius
                y1 = i[1] - circle_radius
                x2 = i[0] + circle_radius
                y2 = i[1] + circle_radius
                canvas.create_oval(x1,y1, x2,y2, fill = 'white', outline = 'black')
                possible_spots.remove(i)
                for i in range(self.columns):
                    for j in range(self.rows):
                        if x > (i*cell_width) and x < ((i+1)*cell_width) and y > (j*cell_height) and y < ((j+1)*cell_height):
                            self.logic_list[j][i] = letter




        
##### START #####
    def start_button(self):
        rows = self.rows
        columns = self.columns
        turn = self.turn
        how_won = self.how_won
        board = self.logic_list
        
        game_state = logic.OthelloClass(board, rows, columns, turn, how_won)

        self.start.destroy()
        self.build_scoreboard()

        change_turn = tkinter.Button(master = self.window, text = 'CHANGE TURN',
                                     font = default, command = self.change_turn)
        change_turn.grid(row = 3, column = 0, padx = 10, pady = 10,
                         sticky = tkinter.S + tkinter.W + tkinter.E)

    def build_scoreboard(self):
        rows = self.rows
        columns = self.columns
        turn = self.turn
        how_won = self.how_won
        board = self.logic_list
        
        game_state = logic.OthelloClass(board, rows, columns, turn, how_won)
        
        score = logic.OthelloClass.score(game_state)
        score_text = tkinter.Label(master = self.window, text = score, font = default)
        score_text.grid(row = 1, column = 0, padx = 10, pady = 10, sticky =
                        tkinter.S + tkinter.W + tkinter.E)

        turn = logic.OthelloClass.turn_output(game_state)
        turn_text = tkinter.Label(master = self.window, text = turn, font = default)
        turn_text.grid(row = 2, column = 0, padx = 10, pady = 10, sticky =
                       tkinter.S + tkinter.W + tkinter.E)

                       

##### LIST VARIABLES #####
    def possible_spots_list(self):
        ''' finds the number of possible spots and puts them in a list'''
        possible_spots_int = self.rows * self.columns
        possible_spots = []

        canvas = self._canvas
        rows = self.rows
        columns = self.columns
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        cell_height = canvas_height/rows
        cell_width = canvas_height/columns
        radius = 1
        
        y1 = (cell_height*500)/2
        y2 = (cell_height*500)/2
        
        for i in range(rows+ 1):
            if i == 0:
                pass
            else:
                x1 = (cell_width*500)/2
                y1 = y1
                x2 = (cell_width*500)/2
                y2 = y2
                if i == 1:
                    pass
                else:
                     y1 += (cell_height*500)
                     y2 += (cell_height*500)
                for j in range(columns + 1):
                    if j == 0:
                        pass
                    else:
                        possible_spots.append([x1,y1])
                        x1 = x1 - radius
                        y1 = y1 - radius
                        x2 = x2 + radius
                        y2 = y2 + radius
                        x1 += radius
                        y1 += radius
                        x2 -= radius
                        y2 -= radius
                        x1 += (cell_width*500)
                        x2 += (cell_width*500)

        return possible_spots

    def game_logic_list(self):
        ''' creates a list for game logic'''
        rows = self.rows
        columns = self.columns
        board = []

        for i in range(rows):
            periods = '. '*columns
            board.append(periods.split())

        return board

    def copy_logic_board(self):
        ''' copies the logic board'''
        board = self.logic_list
        copy = []
        blank = ''

        for i in self.logic_list:
            copy.append(i)

        for i in range(len(copy)):
            for j in range(len(copy[i])):
                if copy[i][j] == 'B':
                    copy[i][j] = '.'
                elif copy[i][j] == 'W':
                    copy [i][j] = '.'

        return copy
        


######################################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
######################################################################################

class Point:
    def __init__(self, frac_x: float, frac_y: float):
        self._frac_x = frac_x
        self._frac_y = frac_y

    def frac(self) -> (float, float):
        return (self._frac_x, self._frac_y)

    def pixel(self, width: float, height: float) -> (float, float):
        return (int(self._frac_x * width), int(self._frac_y * height))

    def frac_distance_from(self, p: 'Point') -> float:
        return math.sqrt(
            (self._frac_x - p._frac_x) * (self._frac_x - p._frac_x)
            + (self._frac_y - p._frac_y) * (self._frac_y - p._frac_y))

def from_frac(frac_x: float, frac_y: float) -> Point:
    return Point(frac_x, frac_y)

def from_pixel(pixel_x: float, pixel_y: float, width: float, height: float) -> Point:
    return Point(pixel_x / width, pixel_y / height)

######################################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
######################################################################################

class FirstInput:
    def __init__(self):
        self.window = tkinter.Tk()
        ########## VARIABES ##########
        self.rows = 0
        self.columns = 0
        self.first_move = ''
        self.how_won = ''
        ########## SIMPLE ##########
        simple_text = tkinter.Label(master = self.window, text = 'SIMPLE', font = default)
        simple_text.grid(row = 0, column = 4, padx = 10, pady = 10, sticky =
                         tkinter.W + tkinter.E + tkinter.N)
        ########## ROW BUTTONS ##########
        
        ''' text '''
        row_text = tkinter.Label(master = self.window, text = 'ROW', font = default)
        row_text.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        ''' 4 '''
        row_four = tkinter.Button(master = self.window, text = '4', font = default,
                                 command = self.r_4)
        row_four.grid(row = 1, column = 1, padx = 10, pady = 10)

        ''' 6 '''
        row_six = tkinter.Button(master = self.window, text = '6', font = default,
                                 command = self.r_6)
        row_six.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        ''' 8 '''
        row_eight = tkinter.Button(master = self.window, text = '8', font = default,
                                 command = self.r_8)
        row_eight.grid(row = 1, column = 3, padx = 10, pady = 10)

        ''' 10 '''
        row_ten = tkinter.Button(master = self.window, text = '10', font = default,
                                 command = self.r_10)
        row_ten.grid(row = 1, column = 4, padx = 10, pady = 10)

        ''' 12 '''
        row_twelve = tkinter.Button(master = self.window, text = '12', font = default,
                                 command = self.r_12)
        row_twelve.grid(row = 1, column = 5, padx = 10, pady = 10)
        
        ''' 14 '''
        row_fourteen = tkinter.Button(master = self.window, text = '14', font = default,
                                 command = self.r_14)
        row_fourteen.grid(row = 1, column = 6, padx = 10, pady = 10)

        ''' 16 '''
        row_sixteen = tkinter.Button(master = self.window, text = '16', font = default,
                                 command = self.r_16)
        row_sixteen.grid(row = 1, column = 7, padx = 10, pady = 10)

        ########## COLUMN BUTTONS ##########
        ''' text '''
        col_text = tkinter.Label(master = self.window, text = 'COLUMN', font = default)
        col_text.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        ''' 4 '''
        col_four = tkinter.Button(master = self.window, text = '4', font = default,
                                 command = self.c_4)
        col_four.grid(row = 2, column = 1, padx = 10, pady = 10)

        ''' 6 '''
        col_six = tkinter.Button(master = self.window, text = '6', font = default,
                                 command = self.c_6)
        col_six.grid(row = 2, column = 2, padx = 10, pady = 10)
        
        ''' 8 '''
        col_eight = tkinter.Button(master = self.window, text = '8', font = default,
                                 command = self.c_8)
        col_eight.grid(row = 2, column = 3, padx = 10, pady = 10)

        ''' 10 '''
        col_ten = tkinter.Button(master = self.window, text = '10', font = default,
                                 command = self.c_10)
        col_ten.grid(row = 2, column = 4, padx = 10, pady = 10)

        ''' 12 '''
        col_twelve = tkinter.Button(master = self.window, text = '12', font = default,
                                 command = self.c_12)
        col_twelve.grid(row = 2, column = 5, padx = 10, pady = 10)
        
        ''' 14 '''
        col_fourteen = tkinter.Button(master = self.window, text = '14', font = default,
                                 command = self.c_14)
        col_fourteen.grid(row = 2, column = 6, padx = 10, pady = 10)

        ''' 16 '''
        col_sixteen = tkinter.Button(master = self.window, text = '16', font = default,
                                 command = self.c_16)
        col_sixteen.grid(row = 2, column = 7, padx = 10, pady = 10)

        ########## FIRST BUTTONS #########
        ''' text '''
        first_text = tkinter.Label(master = self.window, text = 'FIRST MOVE', font = default)
        first_text.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        ''' W '''
        w = tkinter.Button(master = self.window, text = 'W', font = default,
                                 command = self.white)
        w.grid(row = 3, column = 3, padx = 10, pady = 10)

        ''' B '''
        b = tkinter.Button(master = self.window, text = 'B', font = default,
                                 command = self.black)
        b.grid(row = 3, column = 5, padx = 10, pady = 10)

        ########## HOW WON BUTTONS ##########
        ''' text '''
        won_text = tkinter.Label(master = self.window, text = 'HOW WON', font = default)
        won_text.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        ''' > '''
        greater = tkinter.Button(master = self.window, text = '>', font = default,
                                 command = self.greater)
        greater.grid(row = 4, column = 3, padx = 10, pady = 10)

        ''' < '''
        less = tkinter.Button(master = self.window, text = '<', font = default,
                                 command = self.lesser)
        less.grid(row = 4, column = 5, padx = 10, pady = 10)

        ########## DONE BUTTON ##########
        done = tkinter.Button(master = self.window, text = 'DONE', font = default,
                              command = self.done)
        done.grid(row = 5,column = 4, padx = 10, pady = 1,
                  sticky = tkinter.W + tkinter.E + tkinter.S)

        ######
        #row_scale = Scale(master = self.window, from_=4, to=16, tickinterval = 2, orient=HORIZONTAL)
        #row_scale.grid(row = 6, column = 1, padx = 10, pady = 1)

        ########## ROW CONFIGURE #########
        self.window.rowconfigure(0, weight = 1)
        self.window.rowconfigure(1, weight = 1)
        self.window.rowconfigure(2, weight = 1)
        self.window.rowconfigure(3, weight = 1)
        self.window.rowconfigure(4, weight = 1)
        self.window.rowconfigure(5, weight = 1)

        ########## COL CONFIGURE #########
        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(1, weight = 1)
        self.window.columnconfigure(2, weight = 1)
        self.window.columnconfigure(3, weight = 1)
        self.window.columnconfigure(4, weight = 1)
        self.window.columnconfigure(5, weight = 1)
        self.window.columnconfigure(6, weight = 1)
        self.window.columnconfigure(7, weight = 1)
        


        

    ########### VARIABLE SETTING ##########
    # ROWS
    def r_4(self):
        self.rows = 4
    def r_6(self):
        self.rows = 6
    def r_8(self):
        self.rows = 8
    def r_10(self):
        self.rows = 10
    def r_12(self):
        self.rows = 12
    def r_14(self):
        self.rows = 14
    def r_16(self):
        self.rows = 16
    # COLS
    def c_4(self):
        self.columns = 4
    def c_6(self):
        self.columns = 6
    def c_8(self):
        self.columns = 8
    def c_10(self):
        self.columns = 10
    def c_12(self):
        self.columns = 12
    def c_14(self):
        self.columns = 14
    def c_16(self):
        self.columns = 16
    # FIRST MOVE
    def white(self):
        self.first_move = 'W'
    def black(self):
        self.first_move = 'B'
    # HOW WON
    def greater(self):
        self.how_won = '>'
    def lesser(self):
        self.how_won = '<'
    # DONE
    def done(self):
        if self.rows != 0 and self.columns != 0 and self.first_move != '' and self.how_won != '':
            board = Board(self.rows, self.columns, self.first_move,self.how_won)
        else:
            pass

    def start(self) -> None:
        self.window.mainloop()

        


if __name__ == '__main__':
    FirstInput().start()
    

