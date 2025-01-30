import pygame
import random

colors = [(255, 191, 0), (255, 143, 0), (252, 48, 28), (112, 199, 48), (62, 181, 208), (35, 64, 143)]

forms = [[[[1, 1], # shape 1
           [1, 1]]], 
         
         [[[1, 1, 1], # shape 2
           [1, 1, 1]],
          
          [[1, 1], 
           [1, 1], 
           [1, 1]]], 
         
         [[[1, 1, 1], # shape 3
           [1, 1, 1], 
           [1, 1, 1]]],
         
         [[[1, 1, 1], # shape 4
           [1, 0, 0],
           [1, 0, 0]],
         
          [[1, 1, 1],
           [0, 0, 1],
           [0, 0, 1]],
         
          [[1, 0, 0],
           [1, 0, 0],
           [1, 1, 1]],
         
          [[0, 0, 1],
           [0, 0, 1],
           [1, 1, 1]]],
         
         [[[1, 1, 1], # shape 5
           [1, 0, 0]],
         
          [[1, 1, 1],
           [0, 0, 1]],
          
          [[0, 0, 1],
           [1, 1, 1]],
          
          [[1, 0, 0],
           [1, 1, 1]],
          
          [[1, 0],
           [1, 0],
           [1, 1]],
          
          [[0, 1],
           [0, 1],
           [1, 1]],
          
          [[1, 1],
           [0, 1],
           [0, 1]],
          
          [[1, 1],
           [1, 0],
           [1, 0]]],
         
         [[[0, 1, 1], # shape 6
           [1, 1, 0]],
          
          [[1, 1, 0],
           [0, 1, 1]],
          
          [[1, 0],
           [1, 1],
           [0, 1]],
          
          [[0, 1],
           [1, 1],
           [1, 0]]],
         
         [[[0, 1, 0], # shape 7
           [1, 1, 1]],
         
          [[1, 1, 1],
           [0, 1, 0]],
          
          [[1, 0],
           [1, 1],
           [1, 0]],
          
          [[0, 1],
           [1, 1],
           [0, 1]]],
         
         [[[1, 1]], # shape 8
         
          [[1],
           [1]]],
         
         [[[1, 1, 1]], # shape 9
         
          [[1],
           [1],
           [1]]],
         
         [[[1, 0], # shape 10
           [1, 1]],
          
          [[1, 1],
           [0, 1]],
          
          [[1, 1],
           [1, 0]],
          
          [[0, 1],
           [1, 1]]],
         
         [[[1, 1, 1, 1]], # shape 11
         
          [[1],
           [1],
           [1],
           [1]]],
         
         [[[1, 1, 1, 1, 1]], # shape 12
         
          [[1],
           [1],
           [1],
           [1],
           [1]]]]

# probability array for choosing shapes
probs = [0, 127, 202, 242, 307, 434, 561, 688, 815, 942, 1069, 1144, 1200]

class Shape:
    def __init__(self, form):
        if (form != -1):
            self.form = forms[form[0]][form[1]]
        else:
            self.form = random.choice(random.choice(forms))
        self.color = random.choice(colors)
        
def generate_shapes():
        next_shapes = []
        while len(next_shapes) != 3:
            r_int = random.randint(0, 1199)
            for i in range(12):
                if probs[i] <= r_int < probs[i + 1]:
                    current = Shape([i, random.randint(0, len(forms[i]) - 1)])
                    break
            
            valid = True
            for i in next_shapes:
                if i.form == current.form:
                    valid = False
                    break
                
            if valid:
                next_shapes.append(current)
            
        return next_shapes
