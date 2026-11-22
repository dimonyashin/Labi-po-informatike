def Udalenie(x, y):  # Создаем функцию, которая удаляет буквы из слова
    main_word_1 = list(x)  # Превращаем исходное слово в список букв
    main_word_2 = list(x)  
    delete_word = list(y)  # Превращаем слово, из которым удаляют буквы, в список букв

    # Перебираем каждую букву, которую нужно удалить
    for i in range(len(delete_word)):
        delete_letter = delete_word[i]

        # Перебираем все буквы исходного слова
        for j in range(len(main_word_1)):
            main_letter = main_word_1[j]

            # Если буква исходного слова совпала с удаляемой и если она есть в удаляемом слове, то эта буква удалятеся из последнего
            if main_letter == delete_letter and main_letter in main_word_2:
                main_word_2.remove(main_letter)

    c = "".join(main_word_2)  # Собираем оставшиеся буквы в слово
    return c                 # Возвращаем результат функции

a = str(input("Введите слово, из которого удаляются буквы "))
b = str(input("Введите слово, которым удалют буквы из предыдущего слова "))

# Выводим слово после удаления букв
print(Udalenie(a, b))