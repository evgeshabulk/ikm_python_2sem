from logic import MinistryTree

def print_menu():
    print("\n" + "="*50)
    print(" МИНИСТЕРСТВО: РАСЧЕТ МИНИМАЛЬНОЙ ВЗЯТКИ")
    print("="*50)
    print("1. Ввести данные о чиновниках вручную")
    print("2. Загрузить данные из файла")
    print("3. Выход")
    print("="*50)

def parse_and_process(lines):
    tree = MinistryTree()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            raise ValueError(f"Неверный формат строки: '{line}'. Ожидается 3 числа.")
            
        try:
            obj_id = int(parts[0])
            boss_id = int(parts[1])
            bribe = int(parts[2])
        except ValueError:
            raise ValueError(f"Ошибка парсинга строки '{line}'. Ожидаются целые числа.")
            
        tree.add_official(obj_id, boss_id, bribe)
        
    cost, path = tree.find_min_bribe_path()
    return cost, path

def main():
    while True:
        print_menu()
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == '1':
            print("Введите данные (ID, ID_НАЧАЛЬНИКА, ВЗЯТКА) через пробел.")
            print("Для главного чиновника ID_НАЧАЛЬНИКА = 0.")
            print("Введите пустую строку для завершения ввода.")
            lines = []
            while True:
                line = input("> ")
                if not line.strip():
                    break
                lines.append(line)
                
            if not lines:
                print("[ВНИМАНИЕ] Данные не введены.")
                continue
                
            try:
                cost, path = parse_and_process(lines)
                print("\n[УСПЕХ] Расчет завершен!")
                print(f"Минимальная общая сумма: {cost} у.е.")
                print(f"Порядок подписей (от подчиненного к главному): {' -> '.join(map(str, path))}")
            except Exception as e:
                print(f"\n[ОШИБКА] {e}") #Обработка ошибок ввода [cite: 259, 268]
                
        elif choice == '2':
            filename = input("Введите имя входного файла: ").strip()
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                cost, path = parse_and_process(lines)
                print("\n[УСПЕХ] Данные успешно прочитаны и рассчитаны!")
                print(f"Минимальная общая сумма: {cost} у.е.")
                print(f"Порядок подписей: {' -> '.join(map(str, path))}")
                
            except FileNotFoundError:
                print(f"\n[ОШИБКА] Файл '{filename}' не найден.")
            except PermissionError:
                print("\n[ОШИБКА ДОСТУПА] Нет прав на чтение файла.")
            except Exception as e:
                print(f"\n[ОШИБКА АЛГОРИТМА] {e}")
                
        elif choice == '3':
            print("Завершение программы.")
            break
        else:
            print("[ОШИБКА] Некорректный выбор. Введите 1, 2 или 3.")

if __name__ == "__main__":
    main()