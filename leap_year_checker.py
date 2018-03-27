'''
Created on Mar 26, 2018

@author: faronr
'''

def leap_year(rawinput):
    year = rawinput[0]
    leap = False
    if (year%4) == 0:
        leap = True
    
    if leap == True and (year%100) == 0:
        leap = False
        
    if leap == False and (year%400) == 0:
        leap = True
    return leap
        