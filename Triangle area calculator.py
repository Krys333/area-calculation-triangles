from time import sleep

print("This program will help you calculate an area of a triangle")

def Countdown():
    print("calculating, please wait..."), print("3"), sleep(1), print("2"), sleep(1), print("1"), sleep(1), print("done")


def areaCalc():
    height = int(input("Please input the height of your triangle: "))
    base = int(input("Please input the width of the base of your triangle: "))
    
    return height,base



while True:
    height,base = areaCalc()
    Countdown()
    answer = height*base/2
    print("The area of yout triangle is: ",answer)

    if input("Would you like to calculate another one? (y/n): ") == "y":
        continue
    else:
        break
