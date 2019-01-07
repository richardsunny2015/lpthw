numbers = []

def appendList(aList, n, increment):
    #i = 0
    #while i < n:
    for i in range(0, n, increment):
        print(f"At the top i is {i}")
        aList.append(i)

        #i += increment
        print("Numbers now: ", aList)
        print(f"At the bottom i is {i}")

appendList(numbers, 10, 2)
print("The numbers: ")

for num in numbers:
    print(num)
