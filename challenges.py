'''
Created on Mar 26, 2018

@author: faronr
'''

def find_percentage(rawinput):
# precision and round
    n = int(rawinput[0])
    student_marks = {}
    for i in range(1,n+1):
        line = rawinput[i].split()
        name, scores = line[0], line[1:]
        
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = rawinput[n+1]
    a = sum(student_marks[query_name])/len(student_marks[query_name])
    print("%.2f" % round(a,2))
    return "%.2f" % round(a,2)
        