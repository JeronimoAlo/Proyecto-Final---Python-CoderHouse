Pre-Entrega N°3 - Proyecto Final CoderHouse

-------------------------------------------

Dentro de este directorio encontrarán los archivos correspondientes al proyecto, los cuales pueden ser ejecutados con el comando "python manage.py runserver" parados sobre el directorio raíz del proyecto.

Las funcionalidades que tiene la propuesta son:
- Langing Page página de Ropa Argentina, con visualización de Productos tales como "Remeras", "Buzos" y "Pantalones" en forma de etiquetas de bootstrap. Cada producto es un modelo con sus propios atributos (Chequear /AppPreEntreg3/models.py) *Los items de los productos están debajo de los buttons para agregar/buscar.
<img width="281" alt="image" src="https://user-images.githubusercontent.com/69547075/235325209-5d1fe43d-a0ce-414e-87ff-6a36bd91d262.png">
- Agregar prendas: En la página correspondiente a cada producto, hay un button el cual nos permite agregar nuevas prendas (Desarrollado con Forms).
- Buscar prendas: En la página correspondiente a cada producto, hay un button el cual nos permite buscar prendas ya cargadas a la BD por su atributo "nombre".
<img width="143" alt="image" src="https://user-images.githubusercontent.com/69547075/235325221-e4bc7b0f-6975-4d3d-9907-ec293628030f.png">

Pruebas a realizar:
- Agregar Producto (Remera por ejemplo) y chequear en la seccion de "Remeras" su posterior aparición.
- Buscar el producto agregado en el item anterior, el resultado debería de ser una pagina HTML con herencia de padre.html (La cual muestra el MATCH)

Espero que les guste,
Saludos!
