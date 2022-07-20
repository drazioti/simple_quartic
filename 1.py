''' code for solving the diophantine equation : y^2 = (x+a)(x+a+k)(x+b)(x+b+k)
    The function takes three inputs H(a,b,k) and returns the integer solutions with y>=0.
    sage:H(1,2,41)
    [[7, 420], [-51, 420], [-22, 420], [-1, 0], [-43, 0], [-2, 0], [-42, 0]]
    
    sage:H(1,2,1)
    [[-1, 0], [-3, 0], [-2, 0]]
    In this case the trivial roots are three since x=-2 is a double root.

    
'''

var('x,y,a,b')
P.<x,z,a,b> = PolynomialRing(QQ, 4)
def H(a,b,k):
    L = [] # In list L we keep all the integer solutions [x,y]
    n = (k*(a-b))^2
    DIV = divisors(n) # positive divisors of n
    for d1 in DIV:
        d2 = n/d1
        if mod((d1-d2),2)==0 and d1<=d2:
            # here we consider two different values for C, 
            # since we have to search in both, positive d1,d2 and negative d1,d2
            # and only C depends on d1,d2.
            B,C1,C2 = 2*(a+b+k),2*a*b+k*a+k*b-(d1+d2)//2,2*a*b+k*a+k*b+(d1+d2)//2
            Delta1 = B^2 - 8*C1
            Delta2 = B^2 - 8*C2
            if is_square(Delta1):        
                sqr_delta1 = int(sqrt(Delta1))
                x1,x2 = (-B+sqr_delta1)/4,(-B-sqr_delta1)/4
                y = abs((d1-d2)/4)              
                L.append([x1,y])
                if [x2,y] not in L:
                    L.append([x2,y])
            if is_square(Delta2):
                sqr_delta2 = int(sqrt(Delta2))
                x1,x2 = (-B+sqr_delta2)/4,(-B-sqr_delta2)/4
                y = abs((d1-d2)/4)
                L.append([x1,y])
                if [x2,y] not in L:
                    L.append([x2,y])
    print(L)
    return 
