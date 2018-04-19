import chardet

def file_open(filename):
    encode = None
    data = None
    with open("files_to_read/{}".format(filename), "rb") as f:
        specimen = (f.readline())
        encode = chardet.detect(specimen)
    with open("files_to_read/{}".format(filename), encoding=encode["encoding"]) as f:
        data = f.read()
    return data


def calculate_frequency(filename):
    data = file_open(filename)
    strings = data.strip().split(" ")
    temp_dict = {}
    for word in values:
        if len(word) < 6:
            strings.remove(word)
        elif word in calc_dict.keys():
            temp_dict[word] += 1
        else:
            temp_dict[word.lower()] = 1
    print("\nСамые частые слова в файле {}:".format(filename))
    for k in (sorted(temp_dict, key=temp_dict.get, reverse=True)[:10]):
        print("слово '{}' присутствует {} раз".format(k, temp_dict[k]))

def main():
    answer = " "
    while answer is not "q":
        try:
            answer = input("\nВыберите нужный файл ('newsafr.txt', 'newscy.txt', 'neewsfr.txt' "
                           "и 'newsit.txt') \nВведите название файла"
                           "\nq - выход из программы\n")
            if "q" not in answer:
                count_frequency(answer)
        except FileNotFoundError:
            print("Ошибка '{}'. Не существует".format(answer))
            continue
    print("Хорошего дня!")


main()
