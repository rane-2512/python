def cf(n):
    freq=[0]*10

    while(n!=0):
        ld=n%10
        freq[ld]+=1
        n//=10

    return freq
n=1269874501
res=cf(n)

for i in range(len(res)):
    print(f"{i} -> {res[i]}")
