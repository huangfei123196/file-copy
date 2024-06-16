with open ('demo1.txt')as file1:
    contents=file1.read()
print(type(contents))
contents=contents.replace("\n","")
print(contents)
a=''
for content in contents:

    a= a + str(int(content)**2)+"\n"
with open("example.txt", "w", encoding="utf-8") as file2:
    file2.write(a)