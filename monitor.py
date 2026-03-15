from ping3 import ping
from config import DEVICES
import sqlite3

DB_NAME = "network.db"

def check_devices():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for device in DEVICES:

        response = ping(device["ip"], timeout=2)

        if response:
            status = "UP"
        else:
            status = "DOWN"

        cursor.execute(
            "INSERT INTO status (device, ip, status) VALUES (?, ?, ?)",
            (device["name"], device["ip"], status)
        )

        print(device["name"], status)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    check_devices()