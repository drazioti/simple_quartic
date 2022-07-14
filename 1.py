''' code for solving the diophantine equation : y^2 = (x+a)(x+a+k)(x+b)(x+b+k)
    sage:H(1,2,41)
    [[7, 420], [-51, 420], [-22, 420], [-1, 0], [-43, 0], [-2, 0], [-42, 0]]
    
    It returns the non trivial integer solutions
'''

def resultant_singular(a,b,i):
    S = singular.ring(0, '(x,z)', 'dp')
    g1s = singular(a)
    g2s = singular(b)
    if i==0:
        res = singular.resultant(g1s,g2s,'x')
    if i==1:
        res = singular.resultant(g1s,g2s,'z')        
    return res

var('x,y,a,b')
P.<x,z,a,b> = PolynomialRing(QQ, 4)
def H(a,b,k):
    O = 0
    L = []
    f = (x+a)*(x+(a+k))*(x+b)*(x+(b+k)).subs(a=a,b=b)
    f_=diff(f,x)
    res = resultant_singular(P(f+z),P(f_),0).sage()
    n = (k*(a-b))^2
    DIV = divisors(n)
    DIV_minus = [-O for O in DIV]
    for d1 in DIV:
        d2 = n/d1
        if mod((d1-d2),2)==0 and d1<=d2:
            B,C1,C2 = 2*(a+b+k),2*a*b+k*a+k*b-(d1+d2)//2,2*a*b+k*a+k*b+(d1+d2)//2
            Delta1 = B^2 - 8*C1
            Delta2 = B^2 - 8*C2
            #print Delta1,is_square(Delta1),int(sqrt(Delta1)),d1,d2
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
    return f
