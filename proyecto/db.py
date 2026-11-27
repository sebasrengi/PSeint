# Placeholder para conexión y consultas de base de datos
def get_db_connection():
    # Aquí irá tu lógica real con psycopg2 o sqlite3
    print("Conectando a la base de datos de cosméticos...")
    return None

def obtener_productos_placeholder():
    # Datos simulados para probar la vista del inventario
    return [
        {"id": 1, "nombre": "Labial Mate Velvet", "marca": "Maybelline", "categoria": "Labios", "precio": 35.00, "stock": 50},
        {"id": 2, "nombre": "Base Líquida HD Pro", "marca": "L'Oréal", "categoria": "Rostro", "precio": 65.50, "stock": 30},
        {"id": 3, "nombre": "Paleta de Sombras Nude", "marca": "MAC", "categoria": "Ojos", "precio": 145.00, "stock": 12},
        {"id": 4, "nombre": "Máscara Lash Sensational", "marca": "Maybelline", "categoria": "Ojos", "precio": 42.50, "stock": 5},
    ]