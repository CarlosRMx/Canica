from django.db import models

# Create your models here.

class Producto(models.Model):
    """Model definition for Producto."""

    # TODO: Define fields 
    nombre_producto=models.CharField(max_length=30)
    image=models.ImageField(upload_to="img")
    descripcion=models.TextField()
    fecha_ingreso=models.DateField(auto_now_add=True)
    unidades=models.IntegerField()
    fecha_vencimiento=models.DateField()
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre_producto
    
    def get_absolute_url(self):
        return u'/gestion_inventario/%d' % self.id 

class Categoria_Producto(models.Model):
    """Model definition for Categoria_Producto."""

    # TODO: Define fields here
    nombre_categoria=models.CharField(max_length=30)
    descripcion=models.TextField()
    producto=models.ManyToManyField(Producto)
    estado=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Categoria_Producto."""

        verbose_name = 'Categoria_Producto'
        verbose_name_plural = 'Categoria_Productos'

    def __str__(self):
        return self.nombre_categoria

