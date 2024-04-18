# import os
# # Execute the "dir" command in the command prompt or terminal and store the output in the 'output' variable
# output = os.system("dir")

# # Print the exit status of the command execution
# # If the "dir" command executed successfully, the exit status would typically be 0.
# # If there was an error, the exit status would be a non-zero value.
# print(output)  




# import os
# # get the output as a file-like object

# f = os.popen("dir")
# # Read the contents of the output

# output = f.read()
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# # Close the file-like object
# f.close()