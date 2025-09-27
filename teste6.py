products_codes = [0, 0 ,0]
prices = [0, 0, 0]

for i in range(1, 3 ,1):
    value = input().split(" ")
    products_codes[i] = int(value[0])
    prices[i] = int(value[1])
    prices[i] *= float(value[2])
    prices[0] += prices[i]
    
print(f"VALOR A PAGAR: R$ {prices[0]:.2f}")
