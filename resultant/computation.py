''' symbolic computation of resultant

'''
def resultant_singular(a,b,i):
    S = singular.ring(0, '(x,z,y)', 'dp')
    g1s = singular(a)
    g2s = singular(b)
    if i==0:
        res = singular.resultant(g1s,g2s,'x')
    if i==1:
        res = singular.resultant(g1s,g2s,'z')        
    return res
    if i==2:
        res = singular.resultant(g1s,g2s,'y')        
    return res


# f(x) = (x+a)*(x+a+k)*(x+b)*(x+b+k)
var('x,z,a,b,k')
f = (x+a)*(x+a+k)*(x+b)*(x+b+k)
P.<x,z,a,b,k> = PolynomialRing(QQ, 5)
f_ = diff(f,x)
res = resultant_singular(P(f+z),P(f_),0).sage()
show("f(x)=",f)
show(factor(res))
print




# f(x) = c^2x^4+bx^2+c
var('x,z,a,b,c')
f = c^2*x^4+a*x^2+b
P.<x,z,y,a,b,c,k,d> = PolynomialRing(QQ, 8)
f_ = diff(f,x)
res = resultant_singular(P(f+z),P(f_),0).sage()
show("f(x)=",f)
show(factor(res))
print

# f(x) = cx^4+bx^2+c
var('x,z,a,b,c')
f = c*x^4+a*x^2+b
P.<x,z,y,a,b,c,k,d> = PolynomialRing(QQ, 8)
f_ = diff(f,x)
res = resultant_singular(P(f+z),P(f_),0).sage()
show("f(x)=",f)
show(factor(res))
