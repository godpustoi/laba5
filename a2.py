import re

text = input("Введите текст: ")
text = re.split(r'(?<=[.?!]) ', text)
count = len(text)
start = 0
while start != count:
    print(text[start])
    start = start + 1


