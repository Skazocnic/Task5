result = []
while True:
    word = input("Введите слово (или 'stop' для завершения): ")
    if word.lower() == "stop":
        break
    result.append(word)
print("Результат:", " ".join(result))