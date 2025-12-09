def newtext(text):
    while '(' in text:
        start = text.rfind('(')
        end = text.find(')', start)
        text = text[:start] + text[end + 1:]
    return text
s = input("Введите текс со скобками: ")
print(newtext(s))