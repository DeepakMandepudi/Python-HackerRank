if __name__ == '__main__':
    n = int(input().strip())

val = n % 2
if (val != 0):
    print("Weird")
else:
    if(n >=2 and n <=5):
        print("Not Weird")
    elif(n>=6 and n <=20):
        print("Weird")
    elif(n > 20):
        print("Not Weird")