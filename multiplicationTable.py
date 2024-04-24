userNum = input("enter number ")
while not userNum.isdigit():
  userNum = input("enter number ")

num = int(userNum)
table = []

for i in range(1, num + 1):
  x = []
  for j in range(1, i + 1):
    x += [j * i]
  table.append(x)

print(table)  

