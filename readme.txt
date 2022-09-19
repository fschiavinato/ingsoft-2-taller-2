# Librerías externas necesarias

Las librerías usadas fueron `unittest` y `coverage`. La versión de python necesaria es >=3.7.
Por ejemplo para instalar coverage ejecutamos `pip install coverage`.

# Comandos

Para correr el test de un ejercicio ejecutamos `python -m unittest test_ejercicioX.py`.

Para ver el coverage ejecutamos `coverage run -m unittest test_ejercicioX.py`.
Luego `coverage report -m` para ver un reporte del coverage en la consola, o `coverage html` para ver una presentación html línea por línea del código mostrando las líneas cubiertas.
