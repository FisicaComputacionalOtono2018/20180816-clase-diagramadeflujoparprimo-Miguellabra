#Autor: Miguel
#Fecha: 17/08/2018
#Funcion para numero primo

def primo(num):
     flag=False
     for i in range(2, num):
        if num%i==0:
           flag=True
           break
     return flag
num=input("Dame un numero: ")
if primo(num)==False:
   print("Es primo")
else:
   print("No es primo")
        

