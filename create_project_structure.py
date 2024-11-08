import os
from datetime import datetime

# Определяем корневую директорию проекта
project_root = "project_root"

# Задаем структуру директорий для создания
directories = [
    os.path.join(project_root, "data/raw"),       # Директория для исходных данных
    os.path.join(project_root, "data/processed"), # Директория для обработанных данных
    os.path.join(project_root, "logs"),           # Директория для лог-файлов
    os.path.join(project_root, "backups"),        # Директория для резервных копий
    os.path.join(project_root, "output"),         # Директория для выходных данных
]

# Создаем указанные директории, если они еще не существуют
for directory in directories:
    os.makedirs(directory, exist_ok=True) # exist_ok=True позволяет избежать ошибок, если директория уже существует

# Список текстовых файлов, которые будут созданы в папке data/raw/
text_files = [
    ("file1_utf8.txt", "Привет, мир!", "utf-8"),       # Файл с текстом на русском языке и кодировкой UTF-8
    ("file2_iso.txt", "Bonjour le monde!", "iso-8859-1"), # Файл с текстом на французском языке и кодировкой ISO-8859-1
    ("file3_utf8.txt", "Hello, World!", "utf-8")       # Файл с текстом на английском языке и кодировкой UTF-8
]

# Создаем и записываем текстовые файлы в папке data/raw/
for file_name, content, encoding in text_files:
    file_path = os.path.join(project_root, "data/raw", file_name)
    with open(file_path, "w", encoding=encoding) as file: # Открываем файл для записи с указанной кодировкой
        file.write(content) # Записываем содержимое в файл

# Путь к лог-файлу в папке logs/
log_file_path = os.path.join(project_root, "logs", "execution_log.txt")
with open(log_file_path, "a", encoding="utf-8") as log_file: # Открываем лог-файл в режиме добавления
    # Получаем текущую дату и время в формате строки
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Записываем информацию о созданных директориях в лог-файл
    log_file.write(f"{timestamp} - Созданы директории:\n")
    for directory in directories:
        log_file.write(f"  {directory}\n") # Логируем каждую директорию
    
    # Записываем информацию о созданных файлах в data/raw/ в лог-файл
    log_file.write(f"{timestamp} - Созданы файлы в 'data/raw/':\n")
    for file_name, _, _ in text_files:
        log_file.write(f"  {file_name}\n") # Логируем каждый созданный файл
