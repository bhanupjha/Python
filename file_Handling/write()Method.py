f = open("my_file2.txt", "w")
# if we open in existing file it overwrite the content of the file
# f = open("my_file.txt", "w")
f.write("hello world")
f.close()

# if we dont want want to overwrite then we use append mode
f = open("my_file2.txt", "a")
f.write("\nhello Bhanu , welcome")


# if we want to automatically close the file then we use 'with'
with open('my_file2.txt', 'r') as f:
    f = open("my_file2.txt", "a")
    f.write("\nWelcome to vs code editor")
    f.close()