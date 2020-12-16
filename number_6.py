def int_func():
    my_text, my_new_text = [], []  # задаю два пустых спсика
    text = input('Введите слово: ')
    print(text.upper())  # делаю буквы слова заглавными
    text_next = input('Введите слова через пробел: ').title()
    print(text_next)
    my_text.extend(list(map(str, text.split(' '))))  # загоняю слово в список, но можно загнать и пару слов, тут нет проблем
    my_new_text.extend(list(map(str, text_next.split(' '))))  # загоняю предложение в список
    my_text.extend(my_new_text)  # расширяю первый список вторым списком
    my_text = ' '.join(my_text).title()  # делаю из списка str и делаю первые буквы заглавными
    print(my_text)
    return my_text
int_func()

