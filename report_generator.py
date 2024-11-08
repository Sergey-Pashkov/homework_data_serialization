import json
from datetime import datetime

# Данные об анализе выполнения заданий
tasks_analysis = [
    {
        "task_number": 1,
        "description": "Создание структуры директорий и запись данных в файлы.",
        "challenges": "Не возникло значительных сложностей, кроме необходимости учитывать существование директорий при создании.",
        "solutions": "Использовалась функция os.makedirs() с параметром exist_ok=True для предотвращения ошибок.",
        "time_spent": "15 минут",
        "conclusions": "Этот шаг заложил основу для дальнейших заданий и обеспечил базовую структуру проекта."
    },
    {
        "task_number": 2,
        "description": "Чтение, преобразование и сериализация данных.",
        "challenges": "Определение кодировки при чтении файлов.",
        "solutions": "Попробовано несколько кодировок с помощью цикла и перехвата исключения UnicodeDecodeError.",
        "time_spent": "30 минут",
        "conclusions": "Необходимость корректного чтения и преобразования данных подчеркивает важность обработки кодировок."
    },
    {
        "task_number": 3,
        "description": "Создание резервных копий и восстановление данных.",
        "challenges": "Создание архива с учетом структуры директорий.",
        "solutions": "Использовался модуль zipfile для архивации с сохранением структуры директорий.",
        "time_spent": "20 минут",
        "conclusions": "Архивирование файлов важно для резервного копирования и восстановления данных."
    },
    {
        "task_number": 4,
        "description": "Работа с пользовательскими классами и валидация JSON.",
        "challenges": "Установка и использование библиотеки jsonschema.",
        "solutions": "Установлена библиотека jsonschema и создана схема для валидации данных.",
        "time_spent": "35 минут",
        "conclusions": "Работа с пользовательскими классами и валидация помогают обеспечить целостность данных."
    },
    {
        "task_number": 5,
        "description": "Создание итогового отчета.",
        "challenges": "Сбор и структурирование информации о предыдущих шагах.",
        "solutions": "Создан отдельный скрипт для генерации отчета.",
        "time_spent": "10 минут",
        "conclusions": "Отчет помогает оценить проделанную работу и выявить области для улучшения."
    }
]

# Сохранение отчета в формате JSON
report_path = "project_root/output/final_report.json"
with open(report_path, "w", encoding="utf-8") as report_file:
    json.dump(tasks_analysis, report_file, indent=4, ensure_ascii=False)

print(f"Итоговый отчет создан и сохранен в {report_path}")
