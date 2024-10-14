**Gestión de Inventario**

El sistema permite al usuario añadir, ver, eliminar, modificar la información de los vehículos disponibles en el inventario, 
el propósito es tener un sistema que me permita tener un listado de los vehículos disponibles, así como el permitir al usuario 
el de añadir un nuevo vehículo o el de eliminarlo del inventario.

**Arquitectura Cliente Servidor**

Dicha arquitectura es perfecta para implementarla en este sistema de gestión de inventarios, 
ya que con esta arquitectura me permite dividir la estructura en dos partes y me permite trabajarlas de manera independiente.
Por medio de la terminal, se ejecuta la lógica del servidor y del cliente, demostrando así la conexión que tienen 
entre ambos, por lo tanto, dicha arquitectura se adapta a la implementación del sistema desarrollado.

**Ventajas** 
  •	**Divide Responsabilidades:** Permite implementar la lógica de negocio de forma separada del cliente
  •	**Fácil mantenimiento:** Cualquier cambio o actualización en el sistema, solo se necesita realizarse en el servidor
  •	**Escalabilidad:** Se pueden añadir más clientes fácilmente, los cuales podrán conectarse al servidor que permiten acceder a los recursos compartidos
  •	**Centralización de recursos:** Todos los datos y la lógica de la aplicación se gestionan en un único servidor, facilitando la seguridad, mantenimiento y administración ya que está centralizado en un solo lugar
**Desventajas**
  •	**Dependencia del Servidor:** El sistema depende completamente de la disponibilidad del servidor, por tanto, si el servidor falla o se desconecta, todos los clientes perderán acceso a la aplicación
  •	**Costos de Infraestructura:** Mantener un servidor centralizado implica costos asociados como hosting, mantenimiento, actualización, y seguridad del servidor, puesto que a medida que crece el número de clientes, se podría necesitar de una infraestructura más robusta
  •	**Carga en la red:** A medida que aumente los clientes que se conectan al servidor, el trafico de la red aumenta, lo que puede provocar una disminución en el rendimiento

  **Herramientas utilizadas**
  • Visual Studio Code
  • Pyton 3.9.3
  • **Librerias de Python:** Socket y json
  • Terminal
  
