""" 
controlFlowExercise

should output the following

2
4
6
8
We have 4 even numbers
"""

y = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        y += 1
print(f"We have {y} even numbers")
