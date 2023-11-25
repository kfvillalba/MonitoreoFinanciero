
## Instalacion

### Requisitos
- Python 3.8 or higher
- Pip (Python package manager)

### Configurando un entorno virtual
Es recomendable utilizar un entorno virtual para evitar conflictos con otros proyectos de Python o paquetes instalados a nivel del sistema. Para configurar un entorno virtual, sigue estos pasos:

```bash
python -m venv venv
```

Activar el entorno virtual:


```bash
.\venv\Scripts\activate
```


### Instalar las librerias necesarias

Con el entorno virtual activado,instala las librerias necesarias utilizando el comando:

```bash
pip install -r requirements.txt
```

---

## Uso

**Antes de compilar el proyecto, asugurarse que las carpetas expecificadas en: `src/settings/config.py` existan**

### Procesar la informacion

El archivo `data_processor.py` Es usado para obtener la informacion historica de las acciones. Los "tickets" seran extraidos del archivo llamado: `stocks.json`.

Si no existe crear un archivo en la raiz del proyecto llamado: `stocks.json` debe contener el siguiente formato:

```json
{
    "data": [
        "AAPL",
        "MSFT",
        "GOOGL",
        ...
    ]
}
```

Ejecutar la script `data_processor.py`:

```bash
python data_processor.py
```

---

## Simular una inversion

usa `main.py` para simular una inversion en tiempos especificados.

1. Edita `main.py` para elegir el ticket de la accion que quieras, fecha de compra, y fecha de venta.

2. Ejecuta la script:

```bash
python main.py
```

