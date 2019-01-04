from sys import argv

script, filename = argv
# opens file and creates a file object
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read()) # runs read method on file object that converts content into a string
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
