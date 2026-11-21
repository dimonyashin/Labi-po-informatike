def Udalenie(x, y):
    main_word_1 = list(x)
    main_word_2 = list(x)
    delete_word = list(y)
    for i in range(len(delete_word)):
        delete_letter = delete_word[i]
        for j in range(len(main_word_1)):
            main_letter = main_word_1[j]
            if main_letter == delete_letter:
               if main_letter in main_word_2:
                  main_word_2.remove(main_letter)
    c = "".join(main_word_2)
    return(c)
a = "вечеринка"
b = "елка"
print(Udalenie(a, b))