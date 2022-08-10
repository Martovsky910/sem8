from input import *
from datetime import date, datetime as dt
from time import time

def append(name, surname, location, number): 
        time = dt.now().strftime('%D - %H:%M')
        with open('log.csv', 'a') as f:
            f.write(time + '| ')
            f.write(f'{name},{surname},{location},{number}' + '\n') 
            f.close()

def show():
        with open('log.csv', 'r') as s:
            print(s.readlines())
            
