''' code for solving the diophantine equation : y^2 = c^2x^4+ax^2+b
    The function takes three inputs H2(c,a,b) and returns the integer solutions with y>=0.
    sage:H2(3,7,-8)
    [[7, 420], [-51, 420], [-22, 420], [-1, 0], [-43, 0], [-2, 0], [-42, 0]]
'''

def H2(c,a,b):
    L = []
    n = a^2-4*b*c^2
    DIV = divisors(n)
    for d1 in DIV:
        d2 = n/d1
        if mod((d1-d2),2)==0 and d1<=d2:
            Delta =1/(2*c^2) * ( ( d1+d2 )/2 - a )
            if is_square(Delta):                
                sqr_delta = int(sqrt(Delta))
                x1,x2 = sqr_delta,-sqr_delta
                y = abs((d1-d2)/4)
                L.append([x1,y,d1,d2])
                if [x2,y,d1,d2] not in L:
                    L.append([x2,y,d1,d2])
    print(L)
    return 
