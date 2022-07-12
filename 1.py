''' code for solving the diophantine equation : y^2 = (x+a)(x+a+1)(x+b)(x+b+1)
    sage:H(3,10)
     >>> a,b,x0[0],x0[1],|y0|,check: 3 10 -2 -12 24
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
def H(a,b):
    f = (x+a)*(x+(a+1))*(x+b)*(x+(b+1)).subs(a=a,b=b)
    f_=diff(f,x)
    res = resultant_singular(P(f+z),P(f_),0).sage()
    print factor(res)
    DIV = divisors((a-b)^2)
    for d1 in DIV:
        d2 = (a-b)^2//d1
        if d1<d2 and mod((d1-d2),2)==0:
            A,B,C = 2,2*(a+b+1),2*a*b+a+b-(d1+d2)//2
            if is_square(B**2-4*A*C) and (d1-d2)/2!=0:
                print "a,b,x0[0],x0[1],|y0|,check:",a,b,(-B+int(sqrt(B**2-4*A*C)))/4,(-B-int(sqrt(B**2-4*A*C)))/4,abs((d1-d2)/2)
