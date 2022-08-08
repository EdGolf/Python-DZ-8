list = [['1', 'Креп Анатолий Евген', '19.11.1999', 'отл', 'муж'], ['2', 'Анат Ната Конст', '22.03.2000', 'средн', 'жен'], ['3', 'Контр Кат Стан', '02.01.2001', 'отл', 'муж']]
def read_file(file):
    f = open(file, 'r') # encoding='utf-8')
    data = f.read().splitlines()
    list = []
    for line in data:
        line = line.split(';')
        list.append(line)
    f.close()
    return list
# data = 'processing_model.csv'
# print(read_file(data))


def write_file(list, mod):
    f = open('result.csv', mod)
    # for line in list:
    #     f.writelines(line)  ДЛЯ ОБЫЧНОГО СПИСКА
    #     f.writelines(';')
    for i in range(len(list)):
        for j in range(len(list[i])):
            f.writelines(list[i][j])
            f.writelines(';')
        f.writelines('\n')
    f.close()
    if mod == 'a':
        print('Данные записаны!')
    if mod == 'w':
        print('Данные перезаписаны!')

mod = 'w'
write_file(list, mod)