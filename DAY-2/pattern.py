#Write a program to print the following pattern
    #1
   #22
  #333
 #4444
#55555

for i in range(1, 6):
    print(" " * (6 - i), str(i) * i)
