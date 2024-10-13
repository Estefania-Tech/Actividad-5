import socket
import json

# Inventario en memoria (simulado como una lista)
inventario = []

def manejar_peticion(peticion):
    global inventario  # Declarar inventario como global para modificarlo dentro de la función

    peticion = json.loads(peticion)

    if peticion['accion'] == 'obtener':
        return json.dumps(inventario)

    elif peticion['accion'] == 'agregar':
        nuevo_producto = peticion['producto']
        inventario.append(nuevo_producto)
        return json.dumps({'status': 'Producto agregado'})

    elif peticion['accion'] == 'actualizar':
        producto_id = peticion['producto']['id']
        producto = next((p for p in inventario if p['id'] == producto_id), None)
        if producto:
            producto.update(peticion['producto'])
            return json.dumps({'status': 'Producto actualizado'})
        return json.dumps({'status': 'Producto no encontrado'})

    elif peticion['accion'] == 'eliminar':
        producto_id = peticion['id']
        inventario = [p for p in inventario if p['id'] != producto_id]
        return json.dumps({'status': 'Producto eliminado'})

    return json.dumps({'status': 'Acción no válida'})

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 5000))
    servidor.listen(1)
    print("Servidor escuchando en el puerto 5000...")

    while True:
        conexion, direccion = servidor.accept()
        print(f"Conexión establecida con {direccion}")
        
        peticion = conexion.recv(1024).decode('utf-8')
        respuesta = manejar_peticion(peticion)
        conexion.sendall(respuesta.encode('utf-8'))
        conexion.close()

if __name__ == '__main__':
    iniciar_servidor()
