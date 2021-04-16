def divisors(a):
    count = 1
    while count <= a:
        if(a % count == 0) :
            print(count)
        count += 1

divisors(100)