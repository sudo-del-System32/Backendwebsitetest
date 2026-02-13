tamanho = 10
frase = "I have", tamanho, "Cars"
print(frase)

frase = "I have" + str(tamanho) + "Cars"
print(frase)

frase = "I have " + str(tamanho) + " Cars"
print(frase)

frase = "I have {tamanho} Cars"
print(frase)

frase = f"I have {tamanho} Cars"
print(frase)

frase = "I have {} Cars"
print(frase.format(tamanho))

print("I WOULD LOVE TO HAVE {} CARS".format(tamanho))
print("I WOULD LOVE TO HAVE {} CARS".format(10))
print("I WOULD LOVE TO HAVE {} CARS".format("no other"))



f1= "EU"
f2 = "amo coisas"

print(f1 + f2)
f1 = f1 + " "
print(f1 + f2)