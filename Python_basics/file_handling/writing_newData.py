file = open("Python_basics/file_handling/demoFile.txt", "w")


file.write("This is first line.\n")
file.write("This is demo file.\n")
file.write("used for testing purpose.\n")
file.close()

file = open("Python_basics/file_handling/demoFile.txt", "r")
print(file.read())  # this will read entire file
file.close()
