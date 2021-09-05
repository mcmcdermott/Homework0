# Moira McDermott
# 9/5/2021
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

def main():
    n = int(input("> "))

    print(is_prime(n));

if __name__ == "__main__":
    main()


    
