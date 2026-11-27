def formatear_moneda(valor):
    """Formatea un número flotante a moneda USD."""
    return f"${valor:,.2f} USD"

def validar_datos_producto(nombre, precio, stock):
    """Valida reglas básicas antes de guardar en BD."""
    if not nombre or precio <= 0 or stock < 0:
        return False
    return True