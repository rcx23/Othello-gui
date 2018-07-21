#Ryan Cox ID# 31953949

#OTHELLO GUI

import tkinter
from tkinter import *
import math
import Logic as logic


#Font
default = ('Helvetica', 14)

######################################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
######################################################################################

class Board:
    def __init__(self, row:int, col:int, first:str, how:str):
        ########## VARIABES ##########
        self.rows = row
        self.columns = col
        self.turn = first
        self.how_won = how
        
        ##############################

        self.command_window = tkinter.Toplevel()
        self.window = tkinter.Toplevel()
        self._canvas = tkinter.Canvas(master = self.window, width = 500, height = 500,
                                      background = '#A9A9A9')
        self._canvas.grid(row = 0, column = 0, padx = 10, pady = 10,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.bind('<Configure>', self.resize_canvas)
        self._canvas.bind('<Button-1>', self.canvas_clicked)

        self.window.rowconfigure(0, weight = 1)
        self.window.columnconfigure(0, weight = 1)

        self.draw_grid()

        #LIST VARIABLE
        self.possible_moves = self.possible_spots_list()
        self.logic_list = self.game_logic_list()
        self.move_board = self.copy_logic_board()

        self.game_state = logic.OthelloClass(self.logic_list, self.rows,self.columns, self.turn, self.how_won)
        ########## BUTTONS (START/BLACK/WHITE) ##########
        ''' START '''
        start_text = tkinter.Label(master = self.command_window, text = 'START', font = default)
        start_text.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.S)
        
        start = tkinter.Button(master = self.command_window, text = 'START', font = default,
                                 command = self.start_button)
        start.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.S)

        #INITIAL PLACEMENT
        ''' TEXT '''
        initial_text = tkinter.Label(master = self.command_window, text = 'INITIAL DISK PLACEMENT',
                                     font = default)
        initial_text.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.S)
        
        ''' Black Button'''
        black = tkinter.Button(master = self.command_window, text = 'BLACK', font = default,
                               command = self.black_button)
        black.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.S)

        ''' White Button '''
        white = tkinter.Button(master = self.command_window, text = 'WHITE', font = default,
                               command = self.white_button)
        white.grid(row = 2, column = 3, padx = 10, pady = 10, sticky = tkinter.S)

        #Configure
        self.window.rowconfigure(1, weight = 1)
        self.window.rowconfigure(2, weight = 1)
        self.window.columnconfigure(1, weight = 1)
        self.window.columnconfigure(2, weight = 1)
        self.window.columnconfigure(3, weight = 1)
    

    ### POSSIBLE SPOTS ###
    def possible_spots_list(self) -> list:
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

    ### GAME LOGIC LIST ###
    def game_logic_list(self) -> list:
        ''' creates a list for game logic'''
        rows = self.rows
        columns = self.columns
        board = []

        for i in range(rows):
            periods = '. '*columns
            board.append(periods.split())

        return board

    def copy_logic_board(self) -> [[list]]:
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
################################################
    ### ALL FUNCTIONS AFTER A GAME START ###
################################################
    ### START BUTTON FUNCTION ###
    def start_button(self):
        ''' handles start button'''
        rows = self.rows
        columns = self.columns
        turn = self.turn
        how_won = self.how_won
        board = self.logic_list
        
        game_state = logic.OthelloClass(board, rows, columns, turn, how_won)
        self.destroy_initial_buttons()

        

        '''Turn'''
        turn = logic.OthelloClass.turn_output(self.game_state)
        turn_text = tkinter.Label(master = self.window, text = turn, font = default)
        turn_text.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.S)
        '''Score'''
        score = logic.OthelloClass.score(game_state)
        score_text = tkinter.Label(master = self.window, text = score, font = default)
        score_text.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.S)
        ''' Change Turn '''
        change_turn = tkinter.Button(master = self.window, text = 'CHANGE TURN', font = default,
                                     command = self.change_turn)
        change_turn.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.S)

        if self.turn == 'W':
            color = self.place_color_white
        else:
            color = self.place_color_black
        self._canvas.bind('<Button-1>', color)

        if logic.OthelloClass.game_over(game_state) == False:
            self.game_over_window(game_state)

    def change_turn(self):
        '''submits the made turn'''
        
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

    def make_move(self, event: tkinter.Event):
        ''' sets up move making'''
        x = event.x
        y = event.y

        move_board = self.move_board

        canvas = self._canvas
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width
        possible_spots = self.possible_moves
        cell_height = int((500/self.rows))
        cell_width = int((500/self.columns))

        #spots
        for i in possible_spots:
            if x >= (i[0] - int((500/self.columns)/2)) and x <= (i[0] + int((500/self.columns)/2)) and y >= (i[1] - int((500/self.rows)/2)) and y <= (i[1] + int((500/self.rows)/2)):
                possible_spots.remove(i)
                for i in range(self.columns):
                    for j in range(self.rows):
                        if x > (i*cell_width) and x < ((i+1)*cell_width) and y > (j*cell_height) and y < ((j+1)*cell_height):
                            if self.turn == 'B':
                                self.move_board[j][i] = 'B'
                                
                            else:
                                self.move_board[j][i] = 'W'
        

    def possible_move(self, game_state: logic.OthelloClass):
        '''move runner'''
        while logic.OthelloClass.game_over(game_state) == True:
            if logic.OthelloClass.test_for_move(game_state) == True:
                self._canvas.bind('<Button-1>', self.make_move)
                break
        self._redraw
        logic.OthelloClass.change_turn(game_state)

        self.possible_move(game_state)

        if logic.OthelloClass.game_over(game_state) == False:
            self.game_over_window(game_state)
            
                
        
                        
    def coordinates_move(self, event: tkinter.Event):
        '''finds the move and converts it to a list coordinate'''
        logic_list = self.logic_list
        canvas = self._canvas
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width
        click_point = [event.x, event.y]
        possible_spots = self.possible_moves
        circle_radius = 10
        cell_height = int((500/self.rows))
        cell_width = int((500/self.columns))

        if self.turn == 'B':
            color = 'black'
        else:
            color = 'white'
        
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
                possible_spots.remove(i)
                for k in range(self.columns):
                    for j in range(self.rows):
                        if x > (i*cell_width) and x < ((i+1)*cell_width) and y > (j*cell_height) and y < ((j+1)*cell_height):
                            x1 = i[0] - circle_radius
                            y1 = i[1] - circle_radius
                            x2 = i[0] + circle_radius
                            y2 = i[1] + circle_radius
                            if self.turn == 'B':
                                self.logic_list[j][i] = 'B'
                                x1 = x1 - circle_radius
                                y1 = y1 - circle_radius
                                x2 = x2 + circle_radius
                                y2 = y2 + circle_radius
                                canvas.create_oval(x1,y1,x2,y2, fill = 'black', outline = '#7BFF1B')
                                x1 += circle_radius
                                y1 += circle_radius
                                x2 -= circle_radius
                                y2 -= circle_radius
                                x1 += (cell_width*500)
                                x2 += (cell_width*500)
                            else:
                                self.logic_list[j][i] = 'B'
                                x1 = x1 - circle_radius
                                y1 = y1 - circle_radius
                                x2 = x2 + circle_radius
                                y2 = y2 + circle_radius
                                canvas.create_oval(x1,y1,x2,y2, fill = 'black', outline = '#7BFF1B')
                                x1 += circle_radius
                                y1 += circle_radius
                                x2 -= circle_radius
                                y2 -= circle_radius
                                x1 += (cell_width*500)
                                x2 += (cell_width*500)                            
                            print(self.logic_list)
                            
    def destroy_initial_buttons(self):
        ''' destroys the initial buttons'''
        self.command_window.destroy()

    def _redraw(self):
        '''redraws the board'''
        board = self.logic_list
        #
        #self._canvas.delete(tkinter.ALL)
        #
        canvas = self._canvas
        rows = self.rows
        columns = self.columns
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        cell_height = canvas_height/rows
        cell_width = canvas_height/columns
        circle_radius = 10
        dot_radius = 1

        y1 = (cell_height*500)/2
        y2 = (cell_height*500)/2

        #circle radius
        if self.columns > self.rows:
            circle_radius = int((500/self.columns)/2) - 5
        else:
            circle_radius = int((500/self.rows)/2) - 5

        self.draw_rectangles()
        
        for row in range(len(board)):
            if row == 0:
                pass
            else:
                x1 = (cell_width*500)/2
                y1 = y1
                x2 = (cell_width*500)/2
                y2 = y2
                if row == 1:
                    pass
                else:
                     y1 += (cell_height*500)
                     y2 += (cell_height*500)
                for col in range(len(board[row])):
                    if col == 0:
                        pass
                    else:
                        if board[row][col] == '.':
                            x1 = x1 - dot_radius
                            y1 = y1 - dot_radius
                            x2 = x2 + dot_radius
                            y2 = y2 + dot_radius
                            canvas.create_oval(x1,y1,x2,y2, fill = 'black')
                            x1 += dot_radius
                            y1 += dot_radius
                            x2 -= dot_radius
                            y2 -= dot_radius
                            x1 += (cell_width*500)
                            x2 += (cell_width*500)
                        elif board[row][col] == 'B':
                            x1 = x1 - circle_radius
                            y1 = y1 - circle_radius
                            x2 = x2 + circle_radius
                            y2 = y2 + circle_radius
                            canvas.create_oval(x1,y1, x2,y2, fill = 'black', outline = '#7BFF1B')
                            x1 += circle_radius
                            y1 += circle_radius
                            x2 -= circle_radius
                            y2 -= circle_radius
                            x1 += (cell_width*500)
                            x2 += (cell_width*500)
                        elif board[row][col] == 'W':
                            x1 = x1 - circle_radius
                            y1 = y1 - circle_radius
                            x2 = x2 + circle_radius
                            y2 = y2 + circle_radius
                            canvas.create_oval(x1,y1, x2,y2, fill = 'white', outline = '#7BFF1B')
                            x1 += circle_radius
                            y1 += circle_radius
                            x2 -= circle_radius
                            y2 -= circle_radius
                            x1 += (cell_width*500)
                            x2 += (cell_width*500)


    ### GAME OVER FUNCTION ###
    def game_over_window(self, game_state: logic.OthelloClass):
        ''' Displays the game over window'''
        self.game_over = tkinter.Toplevel()
        #Game Over
        game = tkinter.Label(master = self.game_over, text = "GAME OVER", font = default)
        game.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.N)
        

        #Score
        score = logic.OthelloClass.score(game_state)
        score_text = tkinter.Label(master = self.game_over, text = score, font = default)
        score_text.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        #Winner
        winner = "WINNER: " + logic.OthelloClass.game_over_output(game_state)
        winner_text = tkinter.Label(master = self.game_over, text = winner, font = default)
        winner_text.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
                        
                    
                
            
################################################
################################################
################################################
       
    ### BLACK BUTTON FUNCTION ###
    def black_button(self):
        ''' handles black button'''
        self._canvas.bind('<Button-1>', self._black_place)

    def _black_place(self, event: tkinter.Event):
        ''' places black discs '''
        logic_list = self.logic_list
        canvas = self._canvas
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width
        click_point = [event.x, event.y]
        possible_spots = self.possible_moves
        circle_radius = 10
        cell_height = int((500/self.rows))
        cell_width = int((500/self.columns))
        
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
                            self.logic_list[j][i] = 'B'

    ### WHITE BUTTON FUNCTION ###
    def white_button(self):
        ''' handles white button'''
        self._canvas.bind('<Button-1>', self._white_place)

    def _white_place(self, event: tkinter.Event):
        ''' places white discs'''
        logic_list = self.logic_list
        canvas = self._canvas
        height = self._canvas.winfo_height()
        width = self._canvas.winfo_width
        click_point = [event.x, event.y]
        possible_spots = self.possible_moves
        circle_radius = 10
        cell_height = int((500/self.rows))
        cell_width = int((500/self.columns))
        
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
                            self.logic_list[j][i] = 'W'
                            
######### OTHER FUNCTIONS #########
        
        

    def resize_canvas(self, event: tkinter.Event) -> None:
        self._redraw_all_spots()

    def canvas_clicked(self, event: tkinter.Event) -> None:
        pass

    def _redraw_all_spots(self) -> None:
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

    def draw_grid(self) -> None:

        self.draw_rectangles()
        self.possible_spots_draw()

    def draw_columns(self):
        canvas = self._canvas
        columns = self.columns
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        ''' winfo height/width always returns 1. fix later for resizing'''
        #Construct list of points to draw line at
        cell_height = canvas_height/columns

        for i in range(columns):
            if i == 0:
                pass
            else:
                x1 = int((i * cell_height)*(500))
                y1 = 0
                x2 = int((i* cell_height)*(500))
                y2 = 500
                canvas.create_line(x1,y1, x2,y2, fill = 'black')

    def draw_rows(self):
        canvas = self._canvas
        rows = self.rows
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        #Construct list of points to draw line at
        cell_height = canvas_height/rows

        for i in range(rows):
            if i == 0:
                pass
            else:
                
                x1 = 0
                y1 = int((i * cell_height)*(500))
                x2 = 500
                y2 = int((i* cell_height)*(500))
                canvas.create_line(x1,y1, x2,y2, fill = 'black')

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
        self.done.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E
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

