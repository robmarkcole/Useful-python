import os
f = open("file_list.txt","a") #opens file with name of "file_list.txt", creates if doesnt exist
for file in os.listdir("/Users/path_to_folder"):
    f.write(file)
    f.write("\n")
f.close()
