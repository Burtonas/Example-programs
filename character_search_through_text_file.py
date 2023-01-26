import re
import numpy as np

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1691340.txt"
file = open(name)

numbers = []

for line in file:
    words = line.split()
    for word in words:
        number = re.findall('[0-9]+', word)
        if len(number) >= 1:
            for kk in number:
                numbers.append(kk)
                       
numbers = np.array(numbers, dtype=int)
final = sum(numbers)
print(final)

print(str(final)[-3:])