x = int(input("Enter x (between 1 and 10): "))
y = int(input("Enter y (between 1 and 10): "))

# check
while x < 1 or y < 1 or x > 10 or y > 10:
  if x < 1 or x > 9:
    x = int(input("Attention! Enter x (between 1 and 10): "))
  else:
    y = int(input("Enter y (between 1 and 10): "))