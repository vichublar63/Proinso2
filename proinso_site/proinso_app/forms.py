from django.forms import ModelForm,DateField,widgets,Form
from .models import Cliente,Empleado,Categoria,Subcategoria,Insumos,Venta,ItemsVenta,Inventario





class ClienteForm(ModelForm):
    #Campos de Modelo Movimientos
    class Meta:
        model= Cliente
        fields=['id','tipo_documento','primer_nombre','primer_apellido','segundo_apellido','fecha_nacimiento','telefono','direccion','email']
        widgets={'fecha_nacimiento':widgets.DateInput(attrs={'type': 'date'})}

class EmpleadoForm(ModelForm):
    #Campos de Modelo Movimientos
    class Meta:
        model= Empleado
        fields=['id','tipo_documento','primer_nombre','primer_apellido','segundo_apellido','fecha_nacimiento','telefono','direccion','email']
        widgets={'fecha_nacimiento':widgets.DateInput(attrs={'type': 'date'})}

class EmpleadoForm(ModelForm):
    #Campos de Modelo Movimientos
    class Meta:
        model= Empleado
        fields=['id','tipo_documento','primer_nombre','primer_apellido','segundo_apellido','tipo_cargo','fecha_nacimiento','telefono','direccion','email']
        widgets={'fecha_nacimiento':widgets.DateInput(attrs={'type': 'date'})}

class CategoriaForm(ModelForm):
    #Campos de Modelo Movimientos
    class Meta:
        model= Categoria
        fields=['id','nom_categoria']

class SubcategoriaForm(ModelForm):
    #Campos de Modelo Movimientos
    class Meta:
        model= Subcategoria
        fields=['id','id_categoria','nom_subcategoria']

class InsumosForm(ModelForm):    
    #Campos de Modelo Movimientos
    class Meta:
        model= Insumos
        fields=['id','id_subcategoria','nom_insumo','id_medida']

class VentasForm(ModelForm):    
    #Campos de Modelo Movimientos
    class Meta:
        model= Venta
        fields=['id_asesor','id_cliente','id_metodopago','fecha_venta','fecha_entrega','id_trx_comercial','comentario']
        widgets={'fecha_venta':widgets.DateInput(attrs={'type': 'date'}),'fecha_entrega':widgets.DateInput(attrs={'type': 'date'})}

class ItemsForm(ModelForm):    
    #Campos de Modelo Movimientos
    class Meta:
        model= ItemsVenta
        fields=['id_venta','id_insumo','cantidad']

 