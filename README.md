# Hemeroteca - DJango
Creación de una API simple utilizando el framework Django para Python. Esta API soporta las siguientes funcionalidades en las rutas:

- /libros:

Dependiendo del método de la petición se ejecuta una funcionalidad:

- GET: Imprime los registros almacenados de libros almacenados en la base de datos

- POST: Almacena los registros entregados en el cuerpo de la petición. Esta se debe hacer un formato JSON teniendo en cuenta la siguiente plantilla:

{
    "titulo": "Mil años de soledad",
    "tipo":"Novela",
    "fecha": "1967-05-01",
    "editorial": "Sudamericana"
}

- Ademas de esto la API soporta los metodos PUT y PATCH

- /areas:

Dependiendo del método de la petición se ejecuta una funcionalidad:

- GET: Imprime los registros almacenados las areas almacenados en la base de datos

- POST: Almacena los registros entregados en el cuerpo de la petición. Esta se debe hacer un formato JSON teniendo en cuenta la siguiente plantilla:

{
    "nombre": "Libto",
    "descipcion":"loram",
}

- Ademas de esto la API soporta los metodos PUT y PATCH
