def same_by(characteristic, objects):
    res = characteristic(objects[0])
    for element in objects:
        if characteristic(element) != res:
            return False
    return True

def count_vowels(line):
    count = 0
    for letter in line.lower():
        if letter in "уеыаоэяию":
            count += 1
    return count

song = input("Введите песню: ")
if same_by(count_vowels, song.split()):
    print("Парам пам-пам")
else:
    print("Пам-парам")