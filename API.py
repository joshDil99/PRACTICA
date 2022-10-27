#import pandas
def palabra (aux):
    if aux == aux[::-1]:
        return("Si es mi brother")
    else:
        return("No mi bro")
aux = input("Ingrese Palabra")
print(palabra(aux))

