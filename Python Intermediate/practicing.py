file = open("practice.txt")
contents = file.read()
with open("new 2.t2t", mode = "a") as file2:
    file2.write("\nPretty woman!")

with open("new_file.t2t", mode = "w") as file3:
    file3.write("heyyy")
    
print(contents)