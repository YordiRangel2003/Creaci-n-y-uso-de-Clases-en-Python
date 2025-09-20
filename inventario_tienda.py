class InventarioTienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.lista_productos=[]
    def agregar_producto(self,nombre,precio,cantidad):
        if precio > 0 and cantidad > 0:
            self.lista_productos.append({'nombre':nombre,'precio':precio,'cantidad':cantidad}) 
            print(f"Producto '{nombre}' agregado")
        else:
            print("Error los precios y las cantidades deben de ser positivas ")
    def vender_producto(self,nombre,cantidad):
        for producto in self.lista_productos:
            if producto['nombre'].lower()==nombre.lower():
                if producto['cantidad']>=cantidad:
                    producto['cantidad']-=cantidad
                    total_de_venta=producto['precio'] * cantidad
                    print(f"La venta fue exitosa :{cantidad} unidades de '{nombre}' vendidas por {total_de_venta}")
                else:
                    print(f"No hay suficiente stock de '{nombre}'")
                return
        print(f"error: producto '{nombre}' no encontrado ")   
    
    def mostrar_inventario(self):
        print(f"\n inventario de {self.nombre}:")
        for producto in self.lista_productos:
            print(f" {producto['nombre']}// $ {producto['precio']}// {producto['cantidad']}unidades")
    def producto_mas_caro(self):
        if not self.lista_productos:
            print("no hay productos en el inventario")
            return
        mas_caro=self.lista_productos[0]
        for producto in self.lista_productos:
            if producto['precio'] > mas_caro['precio']:
                mas_caro=producto
        print(f"el producto mas caro: {mas_caro['nombre']} ${mas_caro['precio']}")

tiendita=InventarioTienda("La tiendita")
while True:
    print("\n-----MENU-----")
    print("(A). Agregar productos")
    print("(B). Vender productos")
    print("(C). ver el inventario ")
    print("(D). Consultar el producto mas caro ")
    print("(E). Salir")

    opcion=input("Elige una opcion : ").upper()
    
    if opcion == "A":
        nombre=input("Ingresa el nombre del producto :")
        precio=float(input("Precio: "))
        cantidad=int(input("cantidad : "))
        tiendita.agregar_producto(nombre,precio,cantidad)
    elif opcion == "B":
        nombre=input("Nombre del produto:")
        cantidad=int(input("Cantidad a vender "))
        tiendita.vender_producto(nombre,cantidad)
    
    elif opcion =="C":
        tiendita.mostrar_inventario()
    elif opcion =="D":
        tiendita.producto_mas_caro()
    elif opcion=="E":
        print("gracias por su tiempo")
        break
    else:
        print("Opcion no valida. Elige  A-E.")




        
