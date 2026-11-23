import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_NAME = "inventario.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            marca TEXT NOT NULL,
            categoria TEXT NOT NULL,
            tono TEXT,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def index():
    busqueda = request.args.get("buscar", "").strip()
    conn = get_db_connection()
    
    if busqueda:
        query = """
            SELECT * FROM productos 
            WHERE nombre LIKE ? OR marca LIKE ? OR categoria LIKE ?
            ORDER BY id DESC
        """
        param = f"%{busqueda}%"
        productos = conn.execute(query, (param, param, param)).fetchall()
    else:
        productos = conn.execute("SELECT * FROM productos ORDER BY id DESC").fetchall()
        
    # Calcular métricas rápidas
    total_productos = len(productos)
    valor_inventario = sum(p["precio"] * p["stock"] for p in productos)
    stock_bajo = sum(1 for p in productos if p["stock"] <= 5)
    
    conn.close()
    return render_template(
        "index.html",
        productos=productos,
        busqueda=busqueda,
        total_productos=total_productos,
        valor_inventario=valor_inventario,
        stock_bajo=stock_bajo
    )

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    marca = request.form["marca"]
    categoria = request.form["categoria"]
    tono = request.form.get("tono", "N/A")
    precio = float(request.form["precio"])
    stock = int(request.form["stock"])

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO productos (nombre, marca, categoria, tono, precio, stock) VALUES (?, ?, ?, ?, ?, ?)",
        (nombre, marca, categoria, tono, precio, stock)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/actualizar_stock/<int:id>", methods=["POST"])
def actualizar_stock(id):
    accion = request.form["accion"]
    conn = get_db_connection()
    producto = conn.execute("SELECT stock FROM productos WHERE id = ?", (id,)).fetchone()
    
    if producto:
        nuevo_stock = producto["stock"]
        if accion == "sumar":
            nuevo_stock += 1
        elif accion == "restar" and nuevo_stock > 0:
            nuevo_stock -= 1
            
        conn.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, id))
        conn.commit()
        
    conn.close()
    return redirect(url_for("index"))

@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)