try:
    r = open("test.txt", "r", encoding="utf-8")
    print(r.read())
    r.close()

except:
    print("Файл не знайдено")
