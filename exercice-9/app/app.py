from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        dbname=os.environ.get("DB_NAME")
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visites (
            id SERIAL PRIMARY KEY,
            ts TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM visites")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"<h1>Nombre de visites : {count}</h1>"

@app.route("/visites", methods=["POST"])
def add_visite():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO visites DEFAULT VALUES")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM visites")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"total": count}), 201

@app.route("/health")
def health():
    return {"status": "ok"}, 200

with app.app_context():
    try:
        init_db()
    except Exception:
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
