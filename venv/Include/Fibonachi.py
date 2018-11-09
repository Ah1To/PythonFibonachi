def fibo(n):
    if n < 1: return 0;
    if n == 1: return 1;

    return fibo(n-1) + fibo(n-2)



n = int(input("Enter max Fibonachi numbers: "))
arrayList = []

for i in range(1, n + 1 ):
    arrayList.append(fibo(i))

for i in range(3):
    if i > 0: print()
    for n in range(len(arrayList)):
        if i == 0: print(arrayList[n], end=" ")
        if i == 1: print(bin(arrayList[n])[2:].zfill(4), end=" ")
        if i == 2: print(hex(arrayList[n]), end=" ")


question = str(input("Write in file : "))

if  question.lower() == "y":
    file_path = str(input("\nFile path :"))
    with open(file_path, 'w') as file:
        for i in range(3):
            if i > 0: print(file=file)
            for n in range(len(arrayList)):
                if i == 0: print(arrayList[n], end=" ",file=file)
                if i == 1: print(bin(arrayList[n])[2:].zfill(4), end=" ",file=file)
                if i == 2: print(hex(arrayList[n]).zfill(4), end=" ",file=file)