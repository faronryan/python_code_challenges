'''
Created on Mar 26, 2018

@author: faronr
'''

def runner_up(rawinput):
    arr = map(int, rawinput[0].split(' ')) # "1 2 3 4 5 6 6"
    # set removes duplicates if they are hashable
    return sorted(set(arr), reverse=True)[1] # return runner up