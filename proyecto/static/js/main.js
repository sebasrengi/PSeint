document.addEventListener('DOMContentLoaded', () => {
    console.log('GlowStock Cosmetics JS cargado correctamente.');
});

function confirmarEliminacion(nombreProducto) {
    return confirm(`¿Estás seguro de que deseas eliminar "${nombreProducto}" del inventario?`);
}