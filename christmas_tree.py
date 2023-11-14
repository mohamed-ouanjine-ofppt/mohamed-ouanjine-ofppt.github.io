user_input = int(input("Enter a number between 2 and 9: "))

# check the user_input (input) is between 1 and 9
while user_input < 2 or user_input > 9:
  user_input = int(input("Attention! Enter a number bwtween 2 and 9: "))

# this indentation is use to center the tree draw!
forward_indentation = "          "

# before drawing. I wanna explain how this is working:

# consider this Christmas tree based on user_input = 3
#       *
#      ***
#     *****
#      ***
#     *****
#    *******
#     *****
#    *******
#   ********* < here the last line, there are 9 asterisks (*) which is [2 * 4 + 1] -> [(3 - 1) * 4 + 1] -> [(user_input - 1) * 4 + 1]
#      |||
#      |||
#      |||
#
# when a user type 3 and hit enter the last line of the tree drawing will be 9 or (3 - 1) * 4 + 1 asterisks
# and when he type 4 and hit enter the last line of thh tree drawing will be 13 or (4 - 1) * 4 + 1 asterisks 
#
# again consider:
#
#   OOOO*OOOO  <--------------------------------------------------------------------------o
#   OOO***OOO                                                                             |
#   OO*****OO                                                                             |
#   OOO***OOO                                                                             |
#   OO*****OO                                                                             |
#   O*******O                                                                             |
#   O*******O                                                                             |
#   OO*****OO                                                                             |
#   O*******O                                                                             |
#   *********                                                                             |
#      |||                                                                                |
#      |||                                                                                |
#      |||                                                                                |
#                                                                                         |
# y : "O" 'which represent space character'                                               |
# x : "*" 'which represent the tree shape'                                                |
# y + x = the tree length/width --> y + x = ((user_input - 1) * 4 + 1)                    |
#                                                                                         |
# that lead us to conclude that:                                                          |
# If we want to draw the first line where the user_input is 3 I'll do this                |
# y + x = (3 - 1) * 4 + 1                                                                 |
# y + x = 2 * 4 + 1                                                                       |
# y = (2 * 4 + 1) - x                                                                     |
#                                                                                         |
# and x is always 1 at the first line                                                     |       
# so: y = (2 * 4 + 1) - 1  --> y = (8 + 1) - 1  --> y = 9 - 1  --> y = 8: count them! <---o

# drawing the tree
for x in range(1, user_input*2, 2): # if the user_input is 3 so x will be: [1, 3, 5]
  
  # here is the y start and end
  start_y = (((user_input-1) * 4 + 1) - x) // 2 # if the user_input is 3 so start_y will be: 8 // 2 --> 4
  end_y = start_y - (user_input - 1) # end_y will be: 3
  
  for y in range(start_y, end_y-1, -1):
    print(forward_indentation + " " * y + "*" * x + " " * y)
    x += 2

# this condition specify wich tree stump to use and where is its position
if user_input != 2:
  tree_stump = "|||"
  stump_position = ((user_input - 1) * 4) // 2 - 1
else:
  tree_stump = "|"
  stump_position = (user_input - 1) * 4 // 2

# this for loop is used to draw the tree stump 
#       *
#      ***
#     *****
#      ***
#     *****
#    *******
#     *****
#    *******
#   *********
#      |||
#      |||  < this thing is the tree stump (:>!
#      |||

for _ in range(user_input):
  print(forward_indentation + " " * stump_position + tree_stump + " " * stump_position)