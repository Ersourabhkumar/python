''' Q:1 The program takes the file name from the user and reads the contents of that file.'''
# file=open(input("Enter file name: "),"r")
# print(file.read())
# file.close()

'''The program takes a string from the user and appends the string into an existing file.'''
# file_name=input("Enter the file name:  ")
# file=open(file_name,"a")
# s=input("Enter string: ")
# file.write(s)
# file.close()
# file=open(file_name,"r")
# print(file.read())
# file.close()

'''The program takes a word from the user and counts the number of occurrences of 
that word in a file.'''
# fname = input("Enter file name: ")
# word=input("Enter word to be searched:")
# k = 0
 
# with open(fname, 'r') as f:
#     for line in f:
#         words = line.split()
#         for i in words:
#             if(i==word):
#                 k=k+1
# print("Occurrences of the word:")
# print(k)

'''another mathod'''
# file_name = input("Enter file name: ")    # Ask user for the file name
# word = input("Enter word to count: ")     # Ask user which word to search

# count = 0                                 # Start count from 0

# with open(file_name, "r") as file:        # Open the file for reading
#     for line in file:                     # Go through each line in the file
#         words = line.split()              # Break the line into words
#         for w in words:                   # Go through each word
#             if w == word:                 # Check if it matches the word we want
#                 count += 1                # If yes, increase the count

# print(f"The word '{word}' appears {count} times in the file.")

"""The program copies the contents of one file and writes it into another"""
# file1=open("data.txt","r")
# contenst=file1.read()
# file1.close()
# file2=open("example.txt","w")
# new=file2.write(contenst)
#file2.close()

""""""

