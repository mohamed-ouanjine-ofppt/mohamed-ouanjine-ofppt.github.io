number = int(input("Enter a number between 1 and 19: "))

# check the input (number)
while number < 1 or number > 19:
  number = int(input("Attention! Enter a bwtween 1-19: "))

# draw the pyramid

# x represent * character
x = 1
# y represent space (" ") character
y = number - x

for i in range(number):
  print(" "*y, "*"*x, " "*y)
  y -= 1
  x += 2