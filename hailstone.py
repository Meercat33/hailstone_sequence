userNum = int(input("Enter a number: "))
def hailstone(num):
    if num % 2 == 0:
        num //= 2
    elif num % 2 == 1:
        num*=3
        num+=1
    return num

while userNum != 1:
    print(hailstone(userNum))
    userNum = hailstone(userNum)
print("Press enter to close")
input()
