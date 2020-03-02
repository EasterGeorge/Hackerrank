def squareme(n):
    i=0
    while i < n:
        print(i*i)
        i += 1

if __name__ == '__main__':
    n = int(input())
    if n>0 and n <=20:
        squareme(n)
