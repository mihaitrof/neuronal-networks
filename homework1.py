import re
import numpy as np
file = open("data.txt","r")
words = re.split("[+ =]", file.read())

a = np.array()
for i in words:
    print(i)