import socket
import json

def enviar_peticion(peticion):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 5000))
    cliente.sendall(peticion.encode('utf-8'))
    
    respuesta = cliente.recv(1024).decode('utf-8')
    cliente.close()
    return json.loads(respuesta)

def mostrar_menu():
    print("\n--- Gestión de Inventarios ---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def obtener_productos():
    peticion = json.dumps({'accion': 'obtener'})
    productos = enviar_peticion(peticion)
    if productos:
        print("\n--- Lista de productos ---")
        for producto in productos:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}")
    else:
        print("No hay productos en el inventario.")

def agregar_producto():
    id_producto = int(input("ID del producto: "))
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    
    producto = {'id': id_producto, 'nombre': nombre, 'precio': precio}
    peticion = json.dumps({'accion': 'agregar', 'producto': producto})
    respuesta = enviar_peticion(peticion)
    print(respuesta['status'])

def actualizar_producto():
    id_producto = int(input("ID del producto a actualizar: "))
    nombre = input("Nuevo nombre del producto: ")
    precio = float(input("Nuevo precio del producto: "))
    
    producto = {'id': id_producto, 'nombre': nombre, 'precio': precio}
    peticion = json.dumps({'accion': 'actualizar', 'producto': producto})
    respuesta = enviar_peticion(peticion)
    print(respuesta['status'])

def eliminar_producto():
    id_producto = int(input("ID del producto a eliminar: "))
    peticion = json.dumps({'accion': 'eliminar', 'id': id_producto})
    respuesta = enviar_peticion(peticion)
    print(respuesta['status'])

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            obtener_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
