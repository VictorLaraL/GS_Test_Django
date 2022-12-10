# GS_Test

Consideraciones principales:
* Tener instalado python en una version igual o superior a 3.7.
* Tener instalado el manejador de paquetes pip.


## Entorno virtual

### MacOs / Unix
Abrir un shell y navegar hasta la carpeta donde se situará el proyecto.
Dentro de la carpeta creará un entorno virtual ejecutando en la consola:
```
    python3 -m venv env
```

### MacOs / Unix
Abrir un shell y navegar hasta la carpeta donde se situará el proyecto.
dentro de la carpeta creará un entorno virtual ejecutando en la consola:

```
    python -m venv env
```

Es importante tener en cuenta que ya deberia haber registrado dentro de
las variables de entorno el PATH de python para poder utilizar el comando
"python"

Nota: Si ocurre algún problema con el entorno virtual, siempre se puede consultar 
la documentación oficial: https://docs.python.org/3/library/venv.html

Una vez creado nuestro entorno virtual lo activaremos de la siguiente forma:

para MacOs o Unix:

```
    source env/bin/activate
```

para windows:
```
    env\Scripts\activate
```

Una vez tengamos activo el entorno virtual, procedemos a instalar todas las 
dependencias del proyecto.

## Instalacion de dependecias

Dentro del shell con nuestro entorno virtual activo escribimos el siguiente comando:
```
    pip insall -r requirements/local.txt
```

## Instalacion de dependecias

## Consideraciones 
Por utlimo, llevo más o menos 5 años utilizando python y sus múltiples herramientas (Bibliotecas o frameworks), Fast api es una herramienta con la que no había tenido tanto contacto y no estaba para nada actualizado, sin embargo decidí realizarlo con esta misma para probarme a mí mismo y a ustedes si es que tengo el nivel adecuado que buscan.

Utilice todas las herramientas que encuentre a la mano además de nunca dejar a un lado las buenas prácticas que desde hace un tiempo implemento en todos mis desarrollos. 
