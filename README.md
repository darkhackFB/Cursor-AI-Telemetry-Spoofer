Cursor AI Telemetry Spoofer

📦 Автоматическая Подмена Телеметрии в Cursor AI

Этот репозиторий содержит Python-скрипт для автоматической подмены телеметрических данных в Cursor AI путём редактирования системного файла storage.json.

📌 Введение

Cursor AI сохраняет телеметрию и пользовательские настройки в скрытых системных файлах. Python-скрипт автоматически найдет, изменит и перезапишет файл storage.json.

🛠️ Требования

Python 3.x – Скачать Python

Установка библиотеки JSON:

pip install json

📂 Файл Телеметрии Cursor AI

Директория: C:\Users\user\AppData\Roaming\Cursor\User\globalStorage

Целевой файл: storage.json — содержит телеметрические данные и настройки пользователя.

🧑‍💻 Как использовать скрипт

Склонируйте репозиторий:

git clone https://github.com/darkhackFB/Cursor-AI-Telemetry-Spoofer
cd Cursor-AI-Telemetry-Spoofer

Запустите Python-скрипт:

python generateTelemetryData.py

📊 Проверка изменений

Откройте файл C:\Users\user\AppData\Roaming\Cursor\User\globalStorage\storage.json

Убедитесь, что значения telemetry.machineId, macMachineId и другие поля были изменены.

✅ Готово! Телеметрия успешно подменена.
