import os
import time
import curses
from curses import wrapper
import pandas as pd
import re
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

def removingWhitespaces(text):
     return re.sub(r"^\s+","",text)

def removingColumnsWhitespaces(data:list) -> list:
    i = 0
    temp_list = []
    for column in data:
        temp_list.append(removingWhitespaces(column))
        i+=1
    return temp_list
#columns width should follow by maximum lenght char of columns Note: will fix soon
def optimizeWidth(array_data:list) -> list:
    """optimize column width function"""
    maxi = []
    temp = np.transpose(array_data)
    for i in range(temp.shape[0]):
        maxi.append(len(max(temp[i], key = len)))
    return maxi
    

def main(stdscr):
    #Header
    height, width = stdscr.getmaxyx()
    bar = '█'
    path = "airtravel.csv" #https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
    title = os.path.basename(path)
    modified_date = modifiedDate(path)
    df = pd.read_csv(path, sep=',', header=None)
    array_data = df.values

    position = titlePosition(title, width)
    #Style
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    success = curses.color_pair(1)
    warning = curses.color_pair(2)
    text = curses.color_pair(3)

    stdscr.addstr(1, 1, " " * (width - 2), text)
    stdscr.addstr(1, position, title, text)
    stdscr.addstr(3, 1, f"last modified on: {modified_date}", text)
    pad = curses.newpad(height, width)
    stdscr.refresh()
    #show all columns 
    maximun_each_columns = optimizeWidth(array_data)

    block_lenght = width//len(str(maximun_each_columns))
    
    tab = 0
    data = 0
    size = array_data.shape
    mid_screen = (width//2)-(sum(maximun_each_columns)//2)-5
    for rowi in range(size[0]):
        tab = 0
        for columnj in range(size[1]):
            
            data = array_data[rowi,columnj]
            if rowi == 0:
                stdscr.addstr(6 + rowi, mid_screen + tab , " " * (maximun_each_columns[columnj] - len(str(data))), success)
                tab += maximun_each_columns[columnj] - len(str(data))
                stdscr.addstr(6 + rowi, mid_screen + tab , f"{data}", success)
                tab += len(str(data)) + 1
                stdscr.refresh()
            else:
                stdscr.addstr(6 + rowi, mid_screen + tab , " " * (maximun_each_columns[columnj] - len(str(data))), text)
                tab += maximun_each_columns[columnj] - len(str(data))
                stdscr.addstr(6 + rowi, mid_screen + tab , f"{data}", text)
                tab += len(str(data)) + 1
                stdscr.refresh()

    #footer
    q = "Press \"any key\" to quit"
    stdscr.addstr(height - 2, rightPosition(q, width), q, text)
    stdscr.addstr(height - 2, 1, f"Height :{height} Width :{width}", text)
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    wrapper(main)
