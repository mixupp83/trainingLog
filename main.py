import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
import json
from datetime import datetime
import csv

# Файл для сохранения данных
data_file = 'training_log.json'

def load_data():
    """Загрузка данных о тренировках из файла."""
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    """Сохранение данных о тренировках в файл."""
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

class TrainingLogApp:
    def __init__(self, root):
        self.root = root
        root.title("Дневник тренировок")
        self.create_widgets()

    def create_widgets(self):
        # Виджеты для ввода данных
        self.exercise_label = ttk.Label(self.root, text="Упражнение:")
        self.exercise_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.exercise_entry = ttk.Entry(self.root)
        self.exercise_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

        self.weight_label = ttk.Label(self.root, text="Вес:")
        self.weight_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        self.repetitions_label = ttk.Label(self.root, text="Повторения:")
        self.repetitions_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.repetitions_entry = ttk.Entry(self.root)
        self.repetitions_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        self.add_button = ttk.Button(self.root, text="Добавить запись", command=self.add_entry)
        self.add_button.grid(column=0, row=3, columnspan=2, pady=10)

        self.view_button = ttk.Button(self.root, text="Просмотреть записи", command=self.view_records)
        self.view_button.grid(column=0, row=4, columnspan=2, pady=10)

        self.filter_button = ttk.Button(self.root, text="Фильтр по дате", command=self.filter_records_by_date)
        self.filter_button.grid(column=0, row=5, columnspan=2, pady=10)

        self.export_button = ttk.Button(self.root, text="Экспорт в CSV", command=self.export_to_csv)
        self.export_button.grid(column=0, row=6, columnspan=2, pady=10)

    def add_entry(self):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        exercise = self.exercise_entry.get()
        weight = self.weight_entry.get()
        repetitions = self.repetitions_entry.get()

        if not (exercise and weight and repetitions):
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return

        entry = {
            'date': date,
            'exercise': exercise,
            'weight': weight,
            'repetitions': repetitions
        }

        data = load_data()
        data.append(entry)
        save_data(data)

        # Очистка полей ввода после добавления
        self.exercise_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.repetitions_entry.delete(0, tk.END)
        messagebox.showinfo("Успешно", "Запись успешно добавлена!")

    def view_records(self):
        data = load_data()
        records_window = Toplevel(self.root)
        records_window.title("Записи тренировок")

        tree = ttk.Treeview(records_window, columns=("Дата", "Упражнение", "Вес", "Повторения"), show="headings")
        tree.heading('Дата', text="Дата")
        tree.heading('Упражнение', text="Упражнение")
        tree.heading('Вес', text="Вес")
        tree.heading('Повторения', text="Повторения")

        for entry in data:
            tree.insert('', tk.END, values=(entry['date'], entry['exercise'], entry['weight'], entry['repetitions']))

        tree.pack(expand=True, fill=tk.BOTH)

        # Добавляем кнопки для редактирования и удаления записей
        edit_button = ttk.Button(records_window, text="Редактировать", command=lambda: self.edit_entry(tree))
        edit_button.pack(side=tk.LEFT, padx=10, pady=10)

        delete_button = ttk.Button(records_window, text="Удалить", command=lambda: self.delete_entry(tree))
        delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    def filter_records_by_date(self):
        def apply_filter():
            start_date = start_date_entry.get()
            end_date = end_date_entry.get()

            if not (start_date and end_date):
                messagebox.showerror("Ошибка", "Введите даты начала и конца периода!")
                return

            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Ошибка", "Неверный формат даты! Используйте формат YYYY-MM-DD.")
                return

            data = load_data()
            filtered_data = [entry for entry in data if start_date <= datetime.strptime(entry['date'], '%Y-%m-%d %H:%M:%S') <= end_date]

            filter_window = Toplevel(self.root)
            filter_window.title("Отфильтрованные записи")

            tree = ttk.Treeview(filter_window, columns=("Дата", "Упражнение", "Вес", "Повторения"), show="headings")
            tree.heading('Дата', text="Дата")
            tree.heading('Упражнение', text="Упражнение")
            tree.heading('Вес', text="Вес")
            tree.heading('Повторения', text="Повторения")

            for entry in filtered_data:
                tree.insert('', tk.END, values=(entry['date'], entry['exercise'], entry['weight'], entry['repetitions']))

            tree.pack(expand=True, fill=tk.BOTH)

        filter_window = Toplevel(self.root)
        filter_window.title("Фильтр по дате")

        start_date_label = ttk.Label(filter_window, text="Начальная дата (YYYY-MM-DD):")
        start_date_label.grid(column=0, row=0, padx=5, pady=5)
        start_date_entry = ttk.Entry(filter_window)
        start_date_entry.grid(column=1, row=0, padx=5, pady=5)

        end_date_label = ttk.Label(filter_window, text="Конечная дата (YYYY-MM-DD):")
        end_date_label.grid(column=0, row=1, padx=5, pady=5)
        end_date_entry = ttk.Entry(filter_window)
        end_date_entry.grid(column=1, row=1, padx=5, pady=5)

        apply_button = ttk.Button(filter_window, text="Применить фильтр", command=apply_filter)
        apply_button.grid(column=0, row=2, columnspan=2, pady=10)

    def edit_entry(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Ошибка", "Выберите запись для редактирования!")
            return

        data = load_data()
        selected_entry = tree.item(selected_item)['values']
        entry_index = next((i for i, entry in enumerate(data) if entry['date'] == selected_entry[0]), None)

        if entry_index is not None:
            edit_window = Toplevel(self.root)
            edit_window.title("Редактировать запись")

            ttk.Label(edit_window, text="Упражнение:").grid(column=0, row=0, padx=5, pady=5)
            exercise_entry = ttk.Entry(edit_window)
            exercise_entry.insert(0, selected_entry[1])
            exercise_entry.grid(column=1, row=0, padx=5, pady=5)

            ttk.Label(edit_window, text="Вес:").grid(column=0, row=1, padx=5, pady=5)
            weight_entry = ttk.Entry(edit_window)
            weight_entry.insert(0, selected_entry[2])
            weight_entry.grid(column=1, row=1, padx=5, pady=5)

            ttk.Label(edit_window, text="Повторения:").grid(column=0, row=2, padx=5, pady=5)
            repetitions_entry = ttk.Entry(edit_window)
            repetitions_entry.insert(0, selected_entry[3])
            repetitions_entry.grid(column=1, row=2, padx=5, pady=5)

            def save_changes():
                data[entry_index]['exercise'] = exercise_entry.get()
                data[entry_index]['weight'] = weight_entry.get()
                data[entry_index]['repetitions'] = repetitions_entry.get()
                save_data(data)
                messagebox.showinfo("Успешно", "Запись успешно отредактирована!")
                edit_window.destroy()
                self.view_records()

            save_button = ttk.Button(edit_window, text="Сохранить", command=save_changes)
            save_button.grid(column=0, row=3, columnspan=2, pady=10)

    def delete_entry(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Ошибка", "Выберите запись для удаления!")
            return

        data = load_data()
        selected_entry = tree.item(selected_item)['values']
        entry_index = next((i for i, entry in enumerate(data) if entry['date'] == selected_entry[0]), None)

        if entry_index is not None:
            data.pop(entry_index)
            save_data(data)
            messagebox.showinfo("Успешно", "Запись успешно удалена!")
            self.view_records()

    def export_to_csv(self):
        data = load_data()
        if not data:
            messagebox.showerror("Ошибка", "Нет данных для экспорта!")
            return

        with open('training_log.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Дата", "Упражнение", "Вес", "Повторения"])
            for entry in data:
                writer.writerow([entry['date'], entry['exercise'], entry['weight'], entry['repetitions']])

        messagebox.showinfo("Успешно", "Данные успешно экспортированы в файл training_log.csv!")

def main():
    root = tk.Tk()
    app = TrainingLogApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()