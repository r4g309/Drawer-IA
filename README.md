# Drawer IA

¡Bienvenido a Drawer IA! Una aplicación divertida que utiliza inteligencia artificial para adivinar lo que has dibujado. Este proyecto combina tecnologías como HTML, CSS, JavaScript para la interfaz de usuario, y Python para el backend, utilizando bibliotecas como Flask para la comunicación entre el frontend y el backend.

## Requisitos Previos

- Python 3.x instalado en tu sistema.
- PIP (Python Package Installer) para instalar las dependencias.

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/r4g309/Drawer-IA
cd Drawer-IA
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

3. Activa el entorno virtual:

   - En Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - En Linux o MacOS:

     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Ejecuta la aplicación:

```bash
uvicorn main:app
```

2. Abre tu navegador y visita [http://localhost:5000](http://localhost:5000).

## Uso

1. Dibuja en el área designada.
2. Haz clic en el botón "Adivinar" para que la aplicación utilice la inteligencia artificial y trate de adivinar tu dibujo.
3. ¡Diviértete y descubre lo precisa que puede ser la aplicación!

## Estructura del Proyecto

- `static/`: Contiene archivos estáticos como CSS y JavaScript.
- `templates/`: Almacena archivos HTML para la interfaz de usuario.
- `app.py`: Archivo principal que inicia la aplicación Flask.
- `predictor.py`: Contiene la lógica para predecir el dibujo utilizando inteligencia artificial.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes una mejora, no dudes en abrir un problema o enviar un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
