def display_tasks(tasks):
    if not tasks:
        print("Liste boş.")
    else:
        print("Yapılacaklar Listesi:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Yeni görev gir: ")
    tasks.append(task)
    print(f"'{task}' eklendi.")

def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            index = int(input("Silmek istediğin görev numarasını gir: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"'{removed}' silindi.")
            else:
                print("Geçersiz numara.")
        except ValueError:
            print("Lütfen sayı gir.")

def main():
    tasks = []
    while True:
        print("\n1. Görevleri göster\n2. Görev ekle\n3. Görev sil\n4. Çıkış")
        choice = input("Seçimin: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
