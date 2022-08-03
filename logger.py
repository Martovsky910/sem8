from input import *

def append(name, surname, location, number): 
        with open('log.csv', 'a') as f:
            f.write(f'{name},{surname},{location},{number}' + '\n') 

def show():
        with open('log.csv', 'r') as s:
            print(s.readlines())
            
