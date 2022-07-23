''' 
    run the code here : https://tinyurl.com/79zhfpvs
    The following code solve the diophantine equation y^2=x^4+ax^3+bX^2+cx=d and also the following 
    Cy^2=Cx^4+bx^2+d and y^2=C^2x^4+bx^2+d
    
    sage:C,a,b,c,d=1,10,-205,-1150,13104 # curve y^2=x^4 + 10*x^3 - 205*x^2 - 1150*x + 13104
    sage:quartic(C,a,b,c,d)
    [[-16, 60], [-14, 0], [-13, 0], [8, 0], [9, 0], [11, 60]]
   
    sage:C,a,b,c,d=11^2,0,21,0,2 # curve y^2=121x^4 + 21x^2 + 2
    sage:quartic(C,a,b,c,d)
    [[1, 12], [-1, 12]]
    
    sage:C,a,b,c,d=12,0,-30,0,-24 # curve 12y^2=12x^4 - 30x^2 - 24
    sage:quartic(C,a,b,c,d)
    [[2, 2], [-2, 2]]
    
    References :
    [1]  D. Poulakis, A simple method for solving the diophantine equation $y^2=x^4+ax^3+bx^2+cx+d$, Elem. Math. 54 (1999), p. 32 -- 36.
    [2]  D. W. Masser, Polynomial Bounds for Diophantine Equations, Amer. Math. Monthly {\bf 93} (1986), p. 486--488.
    [3]  K. A. Draziotis, Practical solution of some families of quartic diophantine hyperelliptic equations

'''
def is_integer(x):
    if floor(x)==x:
        return 1
    else:
        return 0
        
def method_1(a,b,c,d,f):
    L=[]
    A_positive = a - 8*c + 4*a*b - a^3 
    B_positive = 8*b - 2*a^2 + 1 - 64*d + 16 * b^2 + a^4 - 8*b*a^2
    A_negative = a + 8*c - 4*a*b + a^3 
    B_negative = 8*b - 2*a^2 - 1 + 64*d - 16 * b^2 - a^4 + 8*b*a^2
    Delta1 = 64*(A_positive^2-B_positive)
    Delta2 = 64*(A_negative^2-B_negative)
    if Delta1>=0 and Delta1 in RR:
        delta1=sqrt(Delta1)
        L1 = -(8*A_positive + delta1)/32
        R1 = (-8*A_positive + delta1)/32
        for x0 in range(ceil(L1.n()),floor(R1.n()+1)):
            if is_integer(sqrt(f.subs(x=x0)))==1:
                y = sqrt(f.subs(x=x0))
                L.append([x0,y])
    if Delta2>=0 and Delta2 in RR:
        delta2=sqrt(Delta2)
        L2 = -(8*A_negative + delta2)/32
        R2 = (-8*A_negative + delta2)/32
        for x0 in range(ceil(L2.n()),floor(R2.n()+1)):
            if is_integer(sqrt(f.subs(x=x0)))==1:
                y = sqrt(f.subs(x=x0))
                L.append([x0,y])
    if -8*c + 4*a*b - a^3!=0:
        x1 = (64*d - 16 * b^2 - a^4 + 8*b*a^2) / (8*(- 8*c + 4*a*b - a^3))
        if is_integer(sqrt(f.subs(x=x1)))==1:
            y = sqrt(f.subs(x=x1))
            L.append([x1,y])
    return L
    
def H2(c,a,b):
    ''' code for solving the diophantine equation : y^2 = cx^4+ax^2+b, where c is a square.
    The function takes three inputs H2(c,a,b) and returns the integer solutions with y>=0.
    sage:H2(9,7,-8)
    [[3, 28], [-3, 28]]'''
    
    L = [] # the list that contains the solutions [x,y] with y>0
    sqrtc = int(sqrt(c))
    n = a^2-4*b*c
    DIV_positive = divisors(n)
    DIV_minus = [-O for O in DIV_positive]
    DIV = DIV_positive+DIV_minus
    for d1 in DIV:
        d2 = n/d1
        if mod((d1-d2),2)==0 and d1<=d2:
            Delta =1/(2*c) * ( ( d1+d2 )/2 - a )
            if is_square(Delta):                
                sqr_delta = int(sqrt(Delta))
                x1,x2 = sqr_delta,-sqr_delta
                y = (d2-d1)/(4*sqrtc)
                if is_integer(y)==1:
                    L.append([x1,y])
                if [x2,y] not in L and is_integer(y)==1:
                    L.append([x2,y])
                
    return L
   


def H3(c,a,b):
    ''' code for solving the diophantine equation : cy^2 = cx^4+ax^2+b
    The function takes three inputs H2(c,a,b) and returns the integer solutions with y>=0.
    sage:H2(3,7,-8)
    [[3, 84], [-3, 84]]'''
    
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
    return L

def quartic(C,a,b,c,d): 
    # f(x) = C^2x^4+ax^3+bx^2+cx+d
    f = x^4 + a*x^3+b*x^2+c*x+d 
    L=[]   
    if C!=1:
        if is_square(C):
            if a==0 and c==0:
                L = H2(C,b,d)
                return L            
            else:
                return "a and c must be zero. Input must be of the form (C^2,0,b,0,d)"            
        else:
            if a==0 and c==0:
                # now we consider the case cy^2=cx^4+bx^2+d
                L = H3(C,b,d)
                return L
            else:
                return "a and c must be zero. Input must be of the form (C,0,b,0,d) and you get the solutions of Cy^2=Cx^4+bx^2+d"   

    else:   
    #  here we assume that C = 1
    #  first apply Massers's upper bound if the height is small
        H = max([abs(a),abs(b),abs(c),abs(d)])
        if H<2^6:
            # use Masser's Bound |x|<26H^3
            M = 26*H^3
            for x0 in range(-M,M):
                if is_integer(sqrt(f.subs(x=x0)))==1:
                    y = sqrt(f.subs(x=x0))
                    L.append([x0,y])
        else:
            # now we are in the case where H>=2^6
            # Then apply [1]
            # print(f)
            L = method_1(a,b,c,d,f)
    return L
