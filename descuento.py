# ==========================================
# Programa: descuento_tienda.py
# Propósito: Calcular el descuento aplicable a una compra según el importe
# Autor: Alejandro Garcia Da Silva
# Fecha: 01-10-2026
# ==========================================

# ==========================================
# Valores iniciales
# ==========================================
importe_compra = 0.0
porcentaje = 0.0
descuento = 0.0
total_pagar = 0.0

# ==========================================
# ENTRADAS
# ==========================================
importe_compra = float(input("Introduce el importe de la compra (€): "))

# ==========================================
# CONTROL Y CÁLCULOS
# ==========================================
if importe_compra < 0:
    print("Error: El importe no puede ser negativo.")
else:
    # Comprobamos los tramos de descuento de mayor a menor
    if importe_compra >= 300:
        porcentaje = 0.15
    elif importe_compra >= 100:
        porcentaje = 0.10
    else:
        porcentaje = 0.0

    # Operaciones básicas
    descuento = importe_compra * porcentaje
    total_pagar = importe_compra - descuento

    # ==========================================
    # SALIDAS
    # ==========================================
    print(f"Porcentaje de descuento: {porcentaje * 100:.0f}%")
    print(f"Descuento aplicado: {descuento:.2f} €")
    print(f"Total a pagar: {total_pagar:.2f} €")