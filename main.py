def files_sorter(files):
    files_lengths = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as file1:
            count = len(file1.readlines())
            files_lengths.append(int(count))
    # print(files_lengths)
    files_zipped = sorted(zip(files_lengths, files), key=lambda x: x[0])
    # Т.к. я сортирую files_zipped по элементам files_lengths которые занимают первое/[0] место в кортежах, лямбда-функция/итератор в условии ключа нам здесь не обязателен.
    # Но я решил оставить его в целях наглядности
    with open('output.txt', 'w', encoding='utf-8') as file2:
        for length, name in files_zipped:
            file2.write(name + "\n")
            file2.write(str(length) + "\n")
            with open(name, 'r', encoding='utf-8') as file1:
                for line in file1.readlines():
                    file2.write(line)
                file2.write("\n")



    # for tuple in files_zipped:
    #     print(tuple)
    return()


files_list = ["1.txt", "2.txt", "3.txt"]
files_sorter(files_list)
