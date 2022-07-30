FILE_NAME = r"C:\Desarrollo\PythonLearning\data\bookTitles.txt"

file = open(FILE_NAME)
lines = file.readlines()
for line in lines:
    print(line[0] + str(len(line.strip())))
file.close()