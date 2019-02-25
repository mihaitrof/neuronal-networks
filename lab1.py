# Check if a number is prime
def is_prime(x):
    for d in range (2,x//2):
        if x%d == 0:
            return 0
    return 1

print(is_prime(30))

# Sort alphabetically the words from text.txt
file = open("text.txt","r")
words = file.read().split(" ")
for i in range(0, len(words)):
    try:
        x = words[i].split(".")
        words[i] = x[0]
    except:
        pass
    words[i] = words[i].lower()

words.sort()
print(words)