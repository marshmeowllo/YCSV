import os
import time
import curses
from curses import wrapper
import pandas as pd
import numpy as np
import sys

def titlePosition(title:chr, width:int) -> int:
    halfwidth = width//2
    position = halfwidth - len(title)//2
    
    return position

def modifiedDate(path:chr) -> chr:
    m_time = os.path.getmtime(path)
    local_time = time.ctime(m_time)
    struct_time = time.strptime(local_time)
    T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

    return T_stamp

def rightPosition(text:chr, width:int) -> int:
    return width - len(text)

#columns width should follow by maximum lenght char of columns Note: will fix soon
def columnWidth(array_data:list) -> int:
    maxi = []
    col_max = []
    for i in range(array_data.shape[1]):
        col_max = []
        for j in range(array_data.shape[0]):
            col_max.append(len(str(array_data[j, i])))
        maxi.append(max(col_max))
    return maxi

def downData(stdscr, width:int, height:int, text:chr):
    normal_text = curses.color_pair(3)
    stdscr.addstr(height - 2, rightPosition(text, width), text, normal_text)
    stdscr.addstr(height - 2, 1, f"Height :{height} Width :{width}", normal_text)
    stdscr.refresh()
    stdscr.getch()

def updateData(stdscr, array_data:list, width:int, maximun_each_columns:list, start:int, stop:int):
    success = curses.color_pair(1)
    warning = curses.color_pair(2)
    normal_text = curses.color_pair(3)
    tab = 0
    data = 0
    size = array_data.shape
    mid_screen = (width//2)-(sum(maximun_each_columns)//2)
    for row in range(start, stop+ 1):
        tab = 0
        for column in range(size[1]):
            data = array_data[row,column]
            if row == 0:
                stdscr.addstr(6 + row, mid_screen + tab , " " * (maximun_each_columns[column] - len(str(data))), success)
                tab += maximun_each_columns[column] - len(str(data))
                stdscr.addstr(6 + row, mid_screen + tab , f"{data}", success)
            else:
                stdscr.addstr(6 + row, mid_screen + tab , " " * (maximun_each_columns[column] - len(str(data))), normal_text)
                tab += maximun_each_columns[column] - len(str(data))
                stdscr.addstr(6 + row, mid_screen + tab , f"{data}", normal_text)
            tab += len(str(data)) + 1
            stdscr.refresh()
            

def main(stdscr):
    #Header
    global height, width
    height, width = stdscr.getmaxyx()
    bar = '█'
    path = sys.argv[1] #https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
    title = os.path.basename(path)
    modified_date = modifiedDate(path)
    df = pd.read_csv(path, sep=',', header=None)
    array_data = df.values

    position = titlePosition(title, width)
    #Style
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    normal_text = curses.color_pair(3)

    stdscr.addstr(1, 1, " " * (width - 2), normal_text)
    stdscr.addstr(1, position, title, normal_text)
    stdscr.addstr(3, 1, f"last modified on: {modified_date}", normal_text)
    stdscr.refresh()
    #show columns 
    text = "Press any key to quit"
    downData(stdscr, width, height, text)
    
    maximun_each_columns = columnWidth(array_data)

    updateData(stdscr, array_data, width, maximun_each_columns, 0, 3)
    #footer

if __name__ == "__main__":

    wrapper(main)
    print(f"input {sys.argv[1]}")

