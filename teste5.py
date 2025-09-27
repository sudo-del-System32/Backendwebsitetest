
def prime(num: int) -> bool:
    if num < 2:
        return 0
    if num == 2: return 1
    if not num % 2: return 0
    for x in range(3, num, 2):
        if not (num % x) :
            return 0
    return 1

num = int(input("NUMERO = "))

x = prime(num)

if x:
    print("E PRIMO\n")
    
else:
    print("N E PRIMO\n")
