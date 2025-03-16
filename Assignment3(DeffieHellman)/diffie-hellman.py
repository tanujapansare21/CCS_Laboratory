import math

p= int(input("Enter first prime number (p): "))
g = int(input("Enter primative root (g): "))

a= int(input("Enter first private key (a): "))
if(a<p):
    print(f'{a}private key is valid')

else:
    print("enter valid private key")

b = int(input("Enter second private key (b): "))
if(b<p):
    print(f'{b}private key is valid')

else:
    print("enter valid private key")
    
x=int(pow(g,a,p))
print(f'The public key of user a is :{x}')

y=int(pow(g,b,p))
print(f'The public key of b is:{y}')

ka=int(pow(y,a,p))
print(f'secret key of a is :{ka}')
kb=int(pow(x,b,p))
print(f'secret key of b is :{kb}')

if(ka==kb):
    print("keys are exchanged!")
else:
    print("Failed")