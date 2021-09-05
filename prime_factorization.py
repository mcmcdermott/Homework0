# Moira McDermott
# Homework 0

def is_prime(n):
    if n==2:
        return True
    d = n-1

    while d>1:
        if n%d == 0:
            return False;
        d = d-1

    return True;

def prime_factorization(n):
    factorArr = []
    d = 2;
    num = n
    if(is_prime(n)):
        factorArr.append(n);
    while d <= num/2:
        if(is_prime(d)):
            if(n%d==0):
                factorArr.append(d);
                n = n/d;
                d = d - 1
        d = d + 1

    return factorArr;

def main():
    num = int(input("> "))

    print(prime_factorization(num))


if __name__ == "__main__":
    main()



                
