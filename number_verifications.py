
def print_functions(n):
    if n%2==1 :
        print('Weird')
    elif n%2==0 and n>=2 and n<=5:
        print('Not Weird')
    elif n%2==0 and n>=6 and n<=20:
        print('Weird')
    elif n%2==0 and n>20 and n<=100:
        print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    if n>1 and n<=100 :
        print_functions(n)
    else:
        print('Unsuitabe number')


    
