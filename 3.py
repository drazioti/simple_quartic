''' code for solving the diophantine equation : cy^2 = cx^4+ax^2+b
    The function takes three inputs H2(c,a,b) and returns the integer solutions with x and y>=0.
    sage:H2(3,7,-8)
    [[3, 28], [-3, 28]]
'''
def H3(c,a,b):
    L = []
    n = a^2-4*b*c
    DIV = divisors(n)
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
    return 
