Hemeroteca - Django
Este repositorio contiene una implementación de una API simple utilizando el framework Django para Python. La API utiliza autenticación mediante tokens JWT, los cuales se pueden obtener realizando una petición POST a las siguientes direcciones:

- /api/token/ Obtiene un token de autenticación.
- /api/token/refresh/ Refresca un token existente.
Para obtener un token de autenticación, es necesario proporcionar las credenciales de un usuario válido. En caso de no contar con un usuario válido, se puede utilizar el Administrador por defecto:

- Email: javier.aponte@hotmail.es
- Contraseña: 123456
Si se desea registrar un nuevo usuario, se puede realizar una petición POST a la siguiente dirección (sin autenticación requerida):

/users/sign-up/
Al registrar un nuevo usuario, se deberá asignar un rol, cada uno con sus respectivos permisos:

- Recepción: Usuario encargado de la gestión de préstamos y deudas de la hemeroteca. Acceso al componente loans y posibilidad de listar información de módulos, libros, almacenamiento y autores.

- Inventarios: Usuario encargado de la gestión de inventarios de la hemeroteca. Acceso a los módulos de almacenamiento y libros.

- Lector: Usuario promedio de la aplicación con acceso para listar libros y autores.

- Administrador: Control total de la aplicación, con acceso a todos los módulos.

Por motivos de seguridad, ningún rol tiene permisos para eliminar información, esta tarea queda reservada para el administrador.

La API cuenta con un sistema de multas en caso de retraso en la devolución de una copia de un libro prestada. Esta deuda (Debt) se calcula con base en la cantidad de días desde el fin del plazo de entrega hasta el día de entrega multiplicado por 5000.

Para acceder a documentación adicional o ver en detalle todos los endpoints de la API, puedes visitar la documentación generada por Swagger en las siguientes direcciones:

- /swagger/
- /redoc/