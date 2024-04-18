#  **************To open file for writing*************
# import os
# # Open the file in write-only mode
# f = os.open(f"data/Tutorial 5/tutorial.md", os.O_WRONLY) # here first f is descriptor and 2nd f is f-string

# # Write to the file
# # The b prefix before the string indicates that it should be treated as a sequence of bytes rather than a regular string.
# os.write(f, b"Welcome, Bhanu!")

# # Close the file
# os.close(f)



# ***********To open file for reading*****************
# import os
# # Open the file in read-only mode
# # It returns a file descriptor (f), which is an integer representing the file that was opened.
# f = os.open("myfile.txt", os.O_RDONLY)

# # This line reads up to 1024 bytes of data from the file specified 
# # by the file descriptor f and stores it in the variable contents.
# contents = os.read(f, 1024)
# print("Contents read successfully:", contents) #  it returns a bytes object, which is indicated by the 'b' prefix.

# # This line closes the file specified by the file descriptor f.
# os.close(f)
