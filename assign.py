
def cf(n):
    freq=[0]*10  # Store the frequency of digits 0-9

    while(n!=0):
        ld=n%10  # Get the last digit
        freq[ld]+=1  # Increase the digit count
        n//=10  # Remove the last digit

    return freq  # Return the frequency list

n=1269874501
res=cf(n)  # Calculate digit frequencies

for i in range(len(res)):
    print(f"{i} -> {res[i]}")  # Print each digit and its frequency
