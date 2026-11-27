from flask import Blueprint, render_template, session
from models.producto import ProductoCosmetico

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def index():
    # Lista placeholder usando el modelo ProductoCosmetico
    productos_demo = [
        ProductoCosmetico(1, "Labial Mate Velvet", "Maybelline", "Labios", 35.00, 50),
        ProductoCosmetico(2, "Base Líquida HD Pro", "L'Oréal", "Rostro", 65.50, 30),
        ProductoCosmetico(3, "Paleta de Sombras Nude", "MAC", "Ojos", 145.00, 8),
        ProductoCosmetico(4, "Máscara Lash Sensational", "Maybelline", "Ojos", 42.50, 5)
    ]
    usuario = session.get('usuario', 'Administrador')
    return render_template('dashboard/index.html', productos=productos_demo, usuario=usuario)