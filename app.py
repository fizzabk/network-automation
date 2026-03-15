from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_NAME = "network.db"

@app.route("/")
def dashboard():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT device, ip, status, time
    FROM status
    ORDER BY time DESC
    LIMIT 20
    """)

    data = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)