n  = int(input(" Enter number"))

if n > 1:
    for i in range(2,int(n ** 0.5)+1):
        if n % i==0:
            print("Number is not prime.")
            break
        else:
            print("Number is prime.")
else:
    print("Number is not prime.")