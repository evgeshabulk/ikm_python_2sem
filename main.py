from logic import process_words

def print_menu():
    print("\n" + "="*40)
    print(" ИГРА В СЛОВА (Поиск замкнутой цепочки)")
    print("="*40)
    print("1. Ввести набор слов вручную")
    print("2. Загрузить слова из файла")
    print("3. Выход из программы")
    print("="*40)

def main():
    while True:
        print_menu()
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == '1':
            words_input = input("Введите слова через пробел: ").strip()
            if not words_input:
                print("Ошибка: Вы ввели пустую строку.")
                continue
                
            words_list = words_input.split()
            try:
                result = process_words(words_list)
                print("\n[УСПЕХ] Найденная цепочка:")
                print(" ".join(result))
            except ValueError as e:
                print(f"\n[ОШИБКА АЛГОРИТМА] {e}")
            except Exception as e:
                print(f"\n[КРИТИЧЕСКАЯ ОШИБКА] {e}")
                
        elif choice == '2':
            in_filename = input("Введите имя входного файла (например, input.txt): ").strip()
            try:
                with open(in_filename, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    
                if not content:
                    print("[ВНИМАНИЕ] Указанный файл пуст.")
                    continue
                    
                words_list = content.split()
                result = process_words(words_list)
                
                print("\n[УСПЕХ] Цепочка успешно построена!")
                print(" ".join(result))
                
                out_filename = input("\nВведите имя файла для сохранения результата: ").strip()
                with open(out_filename, 'w', encoding='utf-8') as f:
                    f.write(" ".join(result))
                print(f"[ИНФОРМАЦИЯ] Результат сохранен в файл '{out_filename}'.")
                
            except FileNotFoundError:
                print(f"\n[ОШИБКА ФАЙЛА] Файл '{in_filename}' не найден в директории.")
            except PermissionError:
                print(f"\n[ОШИБКА ДОСТУПА] Нет прав на чтение/запись файла.")
            except ValueError as e:
                print(f"\n[ОШИБКА АЛГОРИТМА] {e}")
            except Exception as e:
                print(f"\n[КРИТИЧЕСКАЯ ОШИБКА] {e}")
                
        elif choice == '3':
            print("Завершение работы программы. До свидания!")
            break
        else:
            print("[ОШИБКА ВВОДА] Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")

if __name__ == "__main__":
    main()