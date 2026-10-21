def anagram(n1,n2):
    freq=[0]*10
    while (n1!=0):
        ld=n1%10
        freq[ld]+=1
        n1//=10
    while (n2!=0):
            ld=n2%10
            freq[ld]-=1
            n2//=10

    for i in freq:
         if(i!=0):
              return False

    return True

n1=1221
n2=1212

res=anagram(n1,n2)

print(f"{n1} and {n2} are in anagram:{res}")
