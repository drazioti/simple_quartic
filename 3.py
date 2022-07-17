''' code for solving the diophantine equation : cy^2 = cx^4+ax^2+b
    The function takes three inputs H2(c,a,b) and returns the integer solutions with y>=0.
    sage:c,a,b=2,21,1
    sage:H3(c,a,b)
    [[7, 54], [-7, 54]]
    
    sage:c,a,b=6,13,2
    sage:H3(c,a,b)
    [[2, 5], [-2, 5]]
'''
def H3(c,a,b):
    L = []
    n = a^2-4*b*c
    DIV_positive = divisors(n)
    DIV_minus = [-O for O in DIV_positive]
    DIV = DIV_positive+DIV_minus
    for d1 in DIV:
        d2 = n/d1
        if mod((d1-d2),2)==0 and d1<=d2:
            Delta =  ( d1+d2 - 2*a )/(4*c)
            if is_square(Delta):                
                sqr_delta = int(sqrt(Delta))
                x1,x2 = sqr_delta,-sqr_delta
                y = (d2-d1)/(4*c)
                L.append([x1,y])
                if [x2,y] not in L:
                    L.append([x2,y])
    print(L)
