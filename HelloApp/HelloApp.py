print('Hello Python from Visual Studio!')
s="*"*30
print(s)
print("New project")
print(s)
try:
    list_of_books=sorted([x.lower()for x in input ("Введите названия книг через запятую с пробелом:\n").split(", ")])#с помощью lower книги записываются с маленькой буквы
    #split разделяет книги запятой с пробелом
    print("Упорядоченный список книг:", ', '.join(list_of_books))
    list_of_books.append(input("\nВведите название книги, которую нужно добавить:\n").lower())#добавление в список новой книги с помощью append
    list_of_books.sort() #Сортировка книг
    print("Обновленный упорядоченный список:",', '.join(list_of_books))
except SyntaxError:
    print("Ошибка чтения кода!")
except ValueError:
    print("Неправильный тип данных!")
except:
    print("Fatal error!")
    
