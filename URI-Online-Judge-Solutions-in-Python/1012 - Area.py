
a,b,c = map(float,input().split())
d = float(0.5*a*c)
e = float(c*c*(3.14159))
f = float(1/2*(a+b)*c)
g = float(b**2)
h = float(a*b)
print("TRIANGULO: %.3f"%d)
print("CIRCULO: %.3f"%e)
print("TRAPEZIO: %.3f"%f)
print("QUADRADO: %.3f"%g)
print("RETANGULO: %.3f"%h)