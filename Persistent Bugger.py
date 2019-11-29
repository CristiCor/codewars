Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.

 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number



My first ugly solution:
def persistence(n):
    # by recursion function
    if n < 10:
        return 0
    n_str = str(n)
    total = 1
    
    print(n_str)
    
    for i in n_str:
        total = total * int(i)
    return 1 + persistence(total)


Beautiful sol: 
import functools

def persistence(n):
    # with functools.reduce
    
    times = 0
    
    while n > 9:
        n = functools.reduce(lambda x, y: x*y, [int(i) for i in str(n)])
        times += 1
    return times

