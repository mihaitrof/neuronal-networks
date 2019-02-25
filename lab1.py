# Test whether or not a number is prime
def is_prime(x):
    for d in range (2,x//2):
        if x%d == 0:
            return 0
    return 1

print(is_prime(30))

# Order the words from text.txt
file = open("text.txt","r")
print(file.read().split(" "))