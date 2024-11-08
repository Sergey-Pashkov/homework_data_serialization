import os
from datetime import datetime
import zipfile

# Определение путей
project_root = "project_root"
data_dir = os.path.join(project_root, "data")
backups_dir = os.path.join(project_root, "backups")

# Создание директории backups, если она не существует
os.makedirs(backups_dir, exist_ok=True)

# Имя архива с текущей датой
current_date = datetime.now().strftime("%Y%m%d")
backup_file_name = f"backup_{current_date}.zip"
backup_file_path = os.path.join(backups_dir, backup_file_name)

# Создание архива с резервной копией
with zipfile.ZipFile(backup_file_path, "w") as backup_zip:
    for foldername, subfolders, filenames in os.walk(data_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            # Добавление файла в архив с сохранением структуры директорий
            backup_zip.write(file_path, os.path.relpath(file_path, project_root))

print(f"Резервная копия создана: {backup_file_path}")
