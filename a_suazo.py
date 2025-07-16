#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {
'8475HD': [387990,10], 
'2175HD': [327990,4], 
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], 
'123FHD': [290890,32], 
'342FHD': [444990,7],
'GF75HD': [749990,2], 
'UWU131HD': [349990,1], 
'FS1230HD': [249990,0],
}

def stock_marca(marca): #FUNCIONANDO 100%
    encontrado = False #flag para saber si se encuentra o no.
    print(f"\nStock disponible de la marca: {marca}")
    for cod,datos in productos.items():
        marc = datos[0].lower() #Transformo los datos a minuscula para que sean iguales.
        if marc == marca:
            print(f"Modelo: {cod} - {stock[cod][1]}")
            encontrado = True #si se encuentra algun nombre se pone en verdadero y se finaliza el programa

    
    if not encontrado: #si no se encuentra nada la bandera queda en falso y se muestra el mensaje 
        print("No existe esa marca.")
        
        

def busqueda_precio(p_min,p_max): #FUNCIONANDO 100%
    encontrada = False #otra flag para que en caso de que no se encuentre muestre un mensaje.
    recolectados = [] #lista para ordenarlo todo luego.
    for code, datos in stock.items():
        if p_min <= datos[0] <= p_max and datos[1]>0:
            recolectados.append(f"{productos[code][0]} -- Modelo: {code} -- Precio: ${stock[code][0]:,}")
            
    if len(recolectados) >= 1:
        encontrada = True
        recolectados.sort()
    else:
        encontrada = False  
    if not encontrada: #si no se encuentra nada la bandera queda en falso y se muestra el mensaje 
        print("No hay notebooks en ese rango de precio.")
    else:  
        print(f"\nNotebooks en el rango de precio: ${p_min:,} - ${p_max:,} (orden alfabético)")
        for data in recolectados:
            print(f"{data}")



def actualizar_precio(modelo,p):

    encontrad = False

    for codigo, datos in stock.items():
        codigo = codigo.upper() #Transformo a mayus para q sea igual al modelo ingresado
        if codigo == modelo:
            datos[0] = p
            encontrad = True 


    if not encontrad:
        print("El modelo no Existe!!")
    else:
        print("Precio actualizado!!")
        print(f"Modelo: {modelo} - Nuevo precio: ${n_precio:,}")


#menu principal. (funcionando)
while True:
    print("""
    *** MENU PINCIPAL ***
    1. Stock marca.
    2. Búsqueda por precio.
    3. Acualizar precio.
    4. Salir
          """)
    try:
        opc_menu = int(input("Ingrese opción: "))
    except ValueError:
        print("Debe seleccionar una opción válida!!.")
        continue
    if opc_menu not in [1,2,3,4]:
        print("Debe seleccionar una opción válida!!.")
    elif opc_menu == 4:
        print("Programa Finalizado.")
    elif opc_menu == 3:
        op_tres = True
        while op_tres:
            modelo = input("Ingrese modelo a actualizar: ").upper()#Transformo a mayus para q sea igual
            try:
                n_precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                print("Debe ingresar valores enteros!!")
                continue

            actualizar_precio(modelo,n_precio)
            while True:
                opc_nueva = input("¿Desea actualizar otro precio de notebook? (s/n): ").lower()
                if opc_nueva == "s":
                    break
                elif opc_nueva == "n":
                    op_tres = False
                    break
                else:
                    print("Opción inválida intente nuevamente...")
                    continue
    elif opc_menu == 2: #LISTOOOO
        while True:
            try:
                p_min = int(input("Ingrese Precio mínimo: "))
                p_max = int(input("Ingrese Precio máximo "))
            except ValueError:
                print("Debe ingresar valores enteros!!")
                continue
            if p_min > p_max:
                print("ERROR: el precio mínimo no puede ser mayor al precio máximo.")
                continue
            else:
                busqueda_precio(p_min,p_max)
                break
            
    else: #opcion 1 LISTA
        marca = input("Escriba el nombre de algna marca (ej: lenovo): ").lower()
        stock_marca(marca)
