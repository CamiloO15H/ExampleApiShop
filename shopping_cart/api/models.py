from django.db import models
#Estructura de la base de datos para el carrito de compras


# Create your models here.
class CartItem(models.Model): #Modelo para los items del carrito de compras
    product_name = models.CharField(max_length=100) #Nombre del producto Chardfield = Cadena de caracteres
    product_quantity = models.PositiveIntegerField(default=1) #Cantidad del producto 
    product_price = models.FloatField() #Precio del producto

    def __str__(self):
        return f"{self.product_name} - Cant {self.product_quantity} $ {self.product_price}"