x = int(input("primul numar= "))
y= int(input("al doilea numar= "))
z= int(input("al treilea numar= "))
#a)'cel mai mare divizor comun'
div=[]
def div_maxim(a,b,c):
    n=0
    for i in range(1, min(a, b, c)+1):
        if a%i==b%i==c%i==0:
            n+=1
            div.append(i)
div_maxim(x,y,z)
print("cel mai mare divizor comun= ",div[-1])

#b) 'cel mai mic multiplu comun'
multiplii=[]
def multiples(a,b,c):
    maxDin3 = max(a,b,c)
    for j in range(1, 1000):
        mtpl=j*maxDin3
        if ((mtpl%a==0) and (mtpl%b==0) and (mtpl%c==0)):
           multiplii.append(mtpl)
    return multiplii
print('cel mai mic multiplu comun=',min(multiples(x,y,z)))
#c) 'Numarul minim'
def min(a,b,c):
    if ((a<b) and (a<c)):
        min=a
    if ((b<a) and (b<c)):
        min=b
    if ((c<b) and (c<a)):
        min=c
    return min
print("minimul= ", min(x,y,z))
#d) 'Numarul maxim'
def max(a,b,c):
    if ((a>b) and (a>c)):
        max=a
    if ((b>a) and (b>c)):
        max=b
    if ((c>b) and (c>a)):
        max=c
    return max
print("maximul= ",max(x,y,z))

#e) 'Toti divizorii comuni'
divizori=[]
def divz(a, b, c):
    for i in range(1, min(a,b,c) + 1):
        if a%i==b%i==c%i== 0:
            divizori.append(i)
    return divizori 
print("toti divizorii comuni= ", divz(x,y,z))
#f) 'cei mai mici 3 multipli comuni'
print('3 multipli comuni:',multiples(x,y,z)[0],',',multiples(x,y,z)[1],',',multiples(x,y,z)[2])
#g1) 'verifica daca laturile pot forma triunghi + aria lui'
def aria_triunghiului(a,b,c):
    if (a+b)>c:
        s = (a + b +c)/2
        aria=((s*(s-a)*(s-b)*(s-c))**0.5)
    if (a+b)<=c:
        print('laturile date nu pot forma triunghi')
    return aria
print('aria triunghiului este= ', aria_triunghiului(x,y,z))
#g2) 'verifica daca laturile pot forma triunghi + perimetru'
def perimetrul_triunghiului(a,b,c):
    if (a+b)>c:
        perimetru = (a + b + c)
    if (a+b)<=c:
        print('laturile date nu pot forma triunghi')
    return perimetru
print('perimetrul este= ',perimetrul_triunghiului(x,y,z))