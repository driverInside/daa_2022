'''
Algorithm gdc(m, n)

Find the gdc of two numbers
Input 2 natural numbers
Output the gdc
'''

def gdc(x, y):
    greatest = max(x, y)
    smaller = min(x, y)
    reminder = greatest % smaller
    
    if (reminder == 0):
        return smaller
    
    if (reminder != 0):
        return gdc(smaller, reminder)
    
m = 105
n = 33    

print(gdc(105, 33))