from itertools import islice
import os

i = 0
while(i < 10):
#Prompt user for filename
    print("MD5 hash grabber for NCMEC Cybertips")
    print("Enter the filename containing your list (example: data.txt): ")
    filename = input()
##Prompting for starting line and number of iterations to skip
    print("What line within " + filename + " contains the first hash? (First line within .txt would be 0): ")
    startln = input()
    print("Hash is found within how many other lines? Every other, every third (ex: 2, 3): ")
    iteration = input()
#Printing hashes
    print ("Printing hashes from " + filename)
    with open(filename) as f:
        #Printing iterated lines up to length of 32char/length of MD5
        for line in islice(f, int(startln), None, int(iteration)):
        #for line in islice(f, 2, None, 3):
            hashonly = line[:32]
            print(hashonly.rstrip())

    print("Hashes printed.")