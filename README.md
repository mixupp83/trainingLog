# Журнал тренировок

Это простое приложение на Python с использованием библиотеки Tkinter для ведения дневника тренировок. Приложение позволяет добавлять записи о выполненных упражнениях, просматривать, редактировать и удалять записи, а также анализировать прогресс с помощью графиков.

## Функционал

- **Добавление записи:** Пользователь может ввести название упражнения, вес и количество повторений, после чего запись будет сохранена в файл.

- **Просмотр записей:** Пользователь может просмотреть все сохраненные записи в удобном виде.

- **Фильтрация записей:**
  - **По дате:** Пользователь может фильтровать записи за определенный период.
  - **По упражнению:** Пользователь может просматривать записи только по конкретному упражнению.

- **Экспорт данных:** Пользователь может экспортировать все записи в файл формата CSV.

- **Импорт данных:** Пользователь может импортировать записи из файла формата CSV.

- **Редактирование записи:** Пользователь может редактировать выбранную запись.

- **Удаление записи:** Пользователь может удалить выбранную запись.

- **Статистика по упражнениям:** Отображение суммарного веса и количества повторений для каждого упражнения.

- **Визуализация прогресса:** Пользователь может построить графики изменения веса и повторений для выбранного упражнения за определенный период.

## Установка и запуск

1. Убедитесь, что у вас установлен Python 3.x.
2. Скачайте или клонируйте репозиторий.
3. Перейдите в директорию с проектом.
4. Установите зависимости, если они не установлены:

```bash
pip install matplotlib
```

```python
python main.py
```

## Использование

1. **Добавление записи:**
    - Введите название упражнения в поле "Упражнение".
    - Введите вес в поле "Вес".
    - Введите количество повторений в поле "Повторения".
    - Нажмите кнопку "Добавить запись".

2. **Просмотр записей:**
    - Нажмите кнопку "Просмотреть записи".
    - Откроется новое окно с таблицей, содержащей все сохраненные записи.

3. **Фильтрация записей:**
    - Нажмите кнопку "Фильтр по дате", чтобы отфильтровать записи за определенный период.
    - Выберите упражнение в окне "Визуализация прогресса", чтобы отфильтровать записи по упражнению.

4. **Экспорт данных:**
   - Нажмите кнопку "Экспорт в CSV", чтобы сохранить все записи в файл формата CSV.

5. **Импорт данных:**
    - Нажмите кнопку "Импорт из CSV", чтобы загрузить записи из файла формата CSV.

6. **Редактирование записи:**
    - В окне просмотра записей выберите запись и нажмите кнопку "Редактировать".
    - Внесите изменения и нажмите "Сохранить".

7. **Удаление записи:**
    - В окне просмотра записей выберите запись и нажмите кнопку "Удалить".

8. **Статистика по упражнениям:**
    - Нажмите кнопку "Статистика по упражнениям", чтобы увидеть суммарный вес и количество повторений для каждого упражнения.
9. **Визуализация прогресса:**
    - Нажмите кнопку "Визуализация прогресса".
    - Выберите упражнение и нажмите "Построить график", чтобы увидеть графики изменения веса и повторений.

## Структура проекта
- **main.py:** Основной файл приложения.
- **training_log.json:** Файл для хранения данных о тренировках.
- **training_log.csv:** Файл для экспорта и импорта данных.

## Зависимости
- Python 3.x
- Tkinter (входит в стандартную библиотеку Python)
- Matplotlib (для визуализации прогресса)

## Автор
Вереин Михаил Павлович 
verein83@mail.ru