text = input("Enter the string: ")
newText = ""

for i in range(len(text)):
    newText += (text[len(text) - 1 - i])

print(newText)
