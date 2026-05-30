import re
handle = open("mbox-short.txt")
# for line in handle:
#     line = line.rstrip()
#     if line.find("From: "):
#         print(line)
# 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻
# This is the same as this
# 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻 :
# for line in handle:
#     line = line.rstrip()
#     if re.search("From: ",line):
#         print(line)

# for line in handle:
#     line = line.rstrip()
#     if line.startswith("From: "):
#         print(line)

# 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻
# This is the same as this
# 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻 :

# for line in handle:
#     line= line.rstrip()
#     if re.search("^From",line):
#         print(line)



# ^X.*:   ---> This regular expression is used to search for a line that 
# starts with X followed by any number of charcters 0 or more followed by a colon ":"
# ^  ---> line that starts with
# .  ---> any charcter
# *  ---> 0 or more

# ^X-\S+:   ---> Search for a line that starts with X -
# followed by -exactly after X - 1 or more non-white space 
# followed by -exaclty after the non-white space- a colon ":"

# X-DSPAM: ✔
# X DSPAM: ✖  ---> Because there is a white space before the colon

#                   ******** EXTRACTING DATA ********

name = "Ahmed"

print(re.findall('[AdEIOU]+',name))

nums = "There is 242 apples on 14 trees"

print(re.findall('[0-9]+',nums))

mail = "From: Ahmed:"
print (re.findall("^F.+:",mail))
print (re.findall("^F.+?:",mail)) #? ---> returns the shortest data

email = "ahmed.yehia.cs@gmail.com"

print(re.findall("\S+@\S+" ,email))

email2 = "From ahmed.yehia.cs@gmail.com"
print(re.findall("From (\S+@\S+)",email2)) # the extracted part will be only inside the parentheses

#  [^X] ---> Starts with everything except X

print(re.findall("@([^ ]*)",email2)) 

# 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻
# This is the same as this
# 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻 :

# print(re.findall("@(\S*)",email2)) 


# [^ ]* --->returns 0 or more non blank characters

numlist = list()
handle = open("mbox-strings.txt")
for line in handle:
    line = line.rstrip()
    pattern = re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
    if len(pattern)!=1:continue
    num = float(pattern[0])
    numlist.append(num)

print (max(numlist))