import re
handle = open("regex_sum.txt")
nums=list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall("[0-9]+",line)
    for i in stuff:
        num = float(i)
        nums.append(num)

print(sum(nums))