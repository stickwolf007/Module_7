def custom_write(file_name, strings):
    strings_positions = {}
    #
    # file = open(file_name, 'w', encoding='utf-8')
    # for i in strings:
    #     cursor = file.tell()
    #     string = (cursor)
    #     strings_positions.append(string, i)
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:

            cursor = file.tell()
            strings_positions[(strings.index(i), cursor)] = i
            file.write(i + '\n')

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)