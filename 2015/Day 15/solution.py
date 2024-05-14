'''
Math Problem!
The whole problem can be simplified into maximizing:
(2a + 0b + 0c + 0d) * (0a + 5b + 0c + (-1)d) * ((-2)a + (-3)b + 5c + 0d) * (0a + 0b + (-1)c + 5d)
= 2a * (5b - d) * (-2a - 3b + 5c) * (-1c + 5d)
Because a component is 0 when it is negative:
= (abs(2a) + 2a)/2 * (abs(5b - d) + (5b - d))/2 * ... you get the point

with constraint:
a + b + c + d = 100

(task 2) 3(a+b) + 8(c+d) = 500

is it even possible to solve it without brute-forcing?
not even input is needed here since we already got our equation
'''
def calculateScore(a, b, c, d):
    x = 2 * a
    y = 5*b + (-1)*d
    z = (-2)*a + (-3)*b + 5*c
    t = (-1)*c + 5*d
    return int((abs(x) + x)/2 * (abs(y) + y)/2 * (abs(z) + z)/2 * (abs(t) + t)/2)

def taskOne():
    maxScore = 0

    for a in range(0, 101):
        for b in range(0, 101-a):
            for c in range(0, 101-a-b):
                d = 100 - a - b - c
                score = calculateScore(a, b, c, d)
                if score > maxScore:
                    maxScore = score

    print(maxScore)

def taskTwo():
    maxScore = 0

    for a in range(0, 101):
        for b in range(0, 101-a):
            for c in range(0, 101-a-b):
                d = 100 - a - b - c
                score = calculateScore(a, b, c, d)
                if score > maxScore and (3*(a+b) + 8*(c+d)) == 500:
                    maxScore = score
    
    print(maxScore)

taskOne()
taskTwo()