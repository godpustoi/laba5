text = input("Введите текст:")
words = text.split()
output = [word[0] for word in words]
start = 0
length = len(output)
while start != length:
    print(output[start])
    start = start + 1
