import os
import json
import uuid
from datetime import datetime

def get_cursor_telemetry_path():
    
    appdata_path = os.getenv('APPDATA')
    storage_path = os.path.join(appdata_path, "Cursor", "User", "globalStorage", "storage.json")
    return storage_path

def generate_fake_telemetry():
   
    fake_data = {
        "telemetry.machineId": str(uuid.uuid4()),
        "telemetry.macMachineId": str(uuid.uuid4()),
        "telemetry.devDeviceId": str(uuid.uuid4()),
        "telemetry.sqmId": str(uuid.uuid4()),
        "lastModified": "9999-12-31T23:59:59.999Z",
        "version": "1.0.1"
    }
    return fake_data

def overwrite_telemetry_file():
        storage_path = get_cursor_telemetry_path()
    
    if os.path.exists(storage_path):
        with open(storage_path, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}

     
        fake_telemetry = generate_fake_telemetry()
        existing_data.update(fake_telemetry)

        with open(storage_path, "w") as file:
            json.dump(existing_data, file, indent=4)
        print("[+] Телеметрия в storage.json успешно изменена!")
    else:
        print("[-] Файл storage.json не найден!")

if __name__ == "__main__":
    overwrite_telemetry_file()
