# Moira McDermott
# Homework 0

def is_prime(n):
    if n==2:
        return True
    d = n-1

    while d>1:
        if n%d == 0:
            return False
        d = d-1

    return True

def nth_prime(n):

    count = 1
    prime = 2
    d = 2

    while(count<=n):
        if(is_prime(d)):
            prime = d;
            count = count + 1
        d = d + 1

    return prime

def main():
    n = int(input("> "))

    print(nth_prime(n))

if __name__ == "__main__":
    main()
        
    
