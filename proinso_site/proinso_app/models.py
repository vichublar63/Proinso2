from django.db import models
from django.conf import settings
from django.utils import timezone


class TipoDocumento(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=15,blank=False)
    def __str__(self):
        return f"{self.tipo}"
    
class TipoCargo(models.Model):
    id=models.AutoField(primary_key=True)
    tipo_cargo=models.CharField(max_length=30,blank=False)
    def __str__(self):
        return f"{self.tipo_cargo}"
    
class Metodopago (models.Model):
    id=models.AutoField(primary_key=True)
    nom_metodopago=models.CharField(max_length=20,blank=False,verbose_name='Metodo Pago')
    def __str__(self):
        return f"{self.nom_metodopago}"

class TrxComercial(models.Model):
    id=models.AutoField(primary_key=True)
    clasificacion=models.CharField(max_length=60,blank=False,verbose_name='Tipo Transaccion Comercial')
    def __str__(self):
        return f"{self.clasificacion}"

class ClasificacionCostoGasto (models.Model):
    id=models.AutoField (primary_key=True)
    clasificacion=models.CharField(max_length=50,blank=False,verbose_name='Clasificación Costo/Gasto')
    def __str__(self):
        return f"{self.clasificacion}"

class CostosGastos(models.Model):
    id_factura=models.AutoField(primary_key=True)
    id_clasificacion_costogasto=models.ForeignKey(ClasificacionCostoGasto,on_delete=models.DO_NOTHING)
    valor=models.FloatField()
    fecha_transaccion=models.DateField(default=timezone.now,verbose_name='Fecha Transaccion')
    comentario=models.CharField(max_length=300,blank=True)

class Medidas (models.Model):
    id=models.AutoField(primary_key=True)
    tipo_medida=models.CharField(max_length=10,blank=False,verbose_name='Tipo Medida')
    def __str__(self):
        return f"{self.tipo_medida}"

class Categoria (models.Model):
    id=models.AutoField(primary_key=True)
    nom_categoria=models.CharField(max_length=50,blank=False,verbose_name='Categoría Producto')
    def __str__(self):
        return f"{self.nom_categoria}"

class Subcategoria (models.Model):
    id=models.AutoField(primary_key=True)
    id_categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nom_subcategoria=models.CharField(max_length=50,blank=False,verbose_name='Subcategoria_Producto')
    def __str__(self):
        return f"{self.nom_subcategoria}"

class Insumos (models.Model):
    id=models.AutoField(primary_key=True)
    id_subcategoria=models.ForeignKey(Subcategoria,on_delete=models.CASCADE)
    nom_insumo=models.CharField(max_length=60,blank=False,verbose_name='Nombre Insumo')
    id_medida=models.ForeignKey(Medidas,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom_insumo}"

class Cliente(models.Model):
    id=models.CharField(max_length=20,primary_key=True,blank=False)
    tipo_documento=models.ForeignKey(TipoDocumento,on_delete=models.DO_NOTHING)
    fecha_nacimiento=models.DateField(default=timezone.now()-timezone.timedelta(days=10950),verbose_name='Fecha Nacimiento')
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    primer_nombre=models.CharField(max_length=50,blank=False)
    primer_apellido=models.CharField(max_length=50,blank=False)
    segundo_apellido=models.CharField(max_length=50,blank=False)
    telefono=models.CharField(max_length=50,blank=False)
    direccion=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=250,verbose_name='Email')
    def __str__(self):
        return f"{self.id}"

class Empleado(models.Model):
    id=models.CharField(max_length=20,primary_key=True,blank=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    tipo_documento=models.ForeignKey(TipoDocumento,on_delete=models.DO_NOTHING)
    fecha_nacimiento=models.DateField(default=timezone.now()-timezone.timedelta(days=10950),verbose_name='Fecha Nacimiento')
    primer_nombre=models.CharField(max_length=50,blank=False)
    primer_apellido=models.CharField(max_length=50,blank=False)
    segundo_apellido=models.CharField(max_length=50,blank=False)
    telefono=models.CharField(max_length=50,blank=False)
    direccion=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=250,verbose_name='Email')
    tipo_cargo=models.ForeignKey(TipoCargo,on_delete=models.CASCADE,default=8)
    def __str__(self):
        return f"{self.id}"

class Proveedor(models.Model):
    id=models.CharField(max_length=20,primary_key=True,blank=False)
    tipo_documento=models.ForeignKey(TipoDocumento,on_delete=models.DO_NOTHING)
    nombre=models.CharField(max_length=50,blank=False)
    apellido=models.CharField(max_length=50,blank=False)
    telefono=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=250,verbose_name='Email')
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id}"


class Inventario (models.Model):
    id=models.AutoField(primary_key=True)
    id_insumo=models.ForeignKey(Insumos,on_delete=models.CASCADE)
    cantidad=models.FloatField()
    valor_inventario=models.FloatField()
    costo_unitario=models.FloatField(verbose_name='Costo Unitario')
    fecha_ingreso=models.DateTimeField(default=timezone.now,verbose_name='Fecha Ingreso')
    id_proveedor=models.ForeignKey(Proveedor,on_delete=models.DO_NOTHING)
    factura_proveedor=models.CharField(max_length=50,blank=False)
    def __str__(self):
        return f"{self.id_insumo}"


class Venta (models.Model):
    id=models.AutoField(primary_key=True)
    id_asesor=models.ForeignKey(Empleado,on_delete=models.DO_NOTHING)
    id_cliente=models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)
    id_metodopago=models.ForeignKey(Metodopago,on_delete=models.DO_NOTHING)
    fecha_venta=models.DateTimeField(default=timezone.now,verbose_name='Fecha Venta')
    fecha_entrega=models.DateTimeField(default=timezone.now()+timezone.timedelta(days=7),verbose_name='Fecha Instalacion')
    id_trx_comercial=models.ForeignKey(TrxComercial,on_delete=models.DO_NOTHING)
    comentario=models.CharField(max_length=300,blank=True)
    def __str__(self):
        return f"{self.id}"

class ItemsVenta(models.Model):
    id=models.AutoField(primary_key=True)
    id_venta=models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_insumo=models.ForeignKey(Inventario, on_delete=models.DO_NOTHING)
    cantidad=models.FloatField(verbose_name='Cantidad Material')

class nomina (models.Model):
    id=models.AutoField(primary_key=True)
    id_empleado=models.ForeignKey(Empleado,on_delete=models.DO_NOTHING)
    valor_pago=models.IntegerField(verbose_name='Valor a Pagar')
    fecha_pago=models.DateTimeField(auto_now_add=True)
    comentario=models.CharField(max_length=300,blank=True)
    def __str__(self):
        return f"{self.id}"
