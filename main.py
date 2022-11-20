# f = open("filenames.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break
#   #The last line in the file will be a blank
#   #We break the loop if the line read is a blank

#   print(contents)
#   # Moved the print after the break so it won't output the final blank line.

# f.close()

# f = open("filenames.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break

#   print(contents)

# f.close()

# f = open("filenames.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break
#   print(contents)

# f.close()

# f = open("filenames.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break

#   print(contents)

# f.close()

import os, time

# while True:
#   print("                 HIGH SCORE TABLE")
#   print()
#   name = input("INITIALS > ").upper()
#   score = input("SCORE > ")
#   print()

#   f = open("high.score", "a+")
#   f.write(f"{name} {score}\n")
#   f.close()

#   print("ADDED")
#   time.sleep(1)
#   os.system("clear")

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore)
