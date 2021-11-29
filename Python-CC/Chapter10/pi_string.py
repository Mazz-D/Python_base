filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    print(content.rstrip())
pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#with open("text_files\filename.txt") as file_object: [Files in the same directory but stored in different file extension group set]

#file_path = "C:\Users\ehmatthes\other_files\filename.txt" with open(file_path) as file_object: [THIS IS FOR ABSOULTE PATH: the files are not on the same folder or location, sometimes not existing]