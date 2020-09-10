

def sieve(n):

    prime_list = [True for i in range(n+1)]

    p = 2
    #import pdb; pdb.set_trace()
    while(p*p <= n):

        if prime_list[p] == True:

            for i in range(p*2, n+1, p):

                prime_list[i] = False

        p = p + 1


    for i in range(2, n):
        if(prime_list[i]):
            print(i)

# Driver code
sieve(20)


