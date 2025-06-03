# Example API Python - Shopping Cart

Este proyecto es una API REST para gestionar un carrito de compras, construida con Django y Django REST Framework.

## Características

- CRUD de ítems del carrito (`CartItem`)
- Serialización y validación de datos
- Endpoints para agregar, listar, actualizar y eliminar productos del carrito

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd example-api-python
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv env
   .\env\Scripts\Activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicia el servidor:**
   ```bash
   python manage.py runserver
   ```

## Endpoints principales

- `POST /api/cart-items/` — Agregar un ítem al carrito
- `GET /api/cart-items/` — Listar todos los ítems
- `GET /api/cart-items/<id>/` — Obtener un ítem específico
- `PATCH /api/cart-items/<id>/` — Actualizar un ítem
- `DELETE /api/cart-items/<id>/` — Eliminar un ítem

## Modelo CartItem

- `product_name`: Nombre del producto (string)
- `product_quantity`: Cantidad (entero positivo)
- `product_price`: Precio (float)

## Notas

- Asegúrate de tener Python 3.8+ instalado.
- Puedes usar herramientas como Postman para probar los endpoints.

---

¡Contribuciones y sugerencias son bienvenidas!
