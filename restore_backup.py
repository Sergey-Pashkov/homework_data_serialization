import os
import zipfile

# Определение путей
project_root = "project_root"
backups_dir = os.path.join(project_root, "backups")
data_dir = os.path.join(project_root, "data")

# Поиск последнего созданного архива для восстановления
backup_files = [f for f in os.listdir(backups_dir) if f.startswith("backup_") and f.endswith(".zip")]
if not backup_files:
    print("Нет доступных резервных копий для восстановления.")
else:
    # Выбираем последний созданный архив
    latest_backup = max(backup_files, key=lambda f: os.path.getctime(os.path.join(backups_dir, f)))
    backup_file_path = os.path.join(backups_dir, latest_backup)

    # Восстановление данных из архива
    with zipfile.ZipFile(backup_file_path, "r") as backup_zip:
        backup_zip.extractall(project_root)

    print(f"Данные восстановлены из резервной копии: {backup_file_path}")
