number = int(input("Enter a natural number: "))

if number < 1:
    print("the number needs to be greater than 1")
elif number == 1:
    print("1 is neither prime or composite")
else:
    for divisor in range(2,(number//2)+1):
        if (number % divisor) == 0:
            print(number," is a composite number")
            break
    else:
        print(number," is a prime number!")