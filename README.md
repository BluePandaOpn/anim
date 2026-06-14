# anim - Motor de Animación Simple

anim es un framework minimalista construido sobre **Pygame** diseñado para facilitar la creación de animaciones mediante secuencias de imágenes. Utiliza una arquitectura de "inyección" para simplificar la carga de recursos y un ciclo de vida automatizado.

## 📂 Estructura del Proyecto

- `main.py`: Punto de entrada donde se define la lógica de la animación.
- `anim/`: Directorio principal del paquete.
    - `__init__.py`: Orquestador de módulos y exportación de API.
    - `anim.py`: Núcleo del motor, gestión de ventana y bucle principal.
    - `esencial.py`: Sistema de carga de imágenes y extensión de `pygame`.
    - `canva.py`: Control de dimensiones y superficie de renderizado.

## 🚀 Instalación

Asegúrate de tener Python 3 y Pygame instalados en tu entorno virtual:

```bash
pip install pygame
```

## 🛠️ Guía de Uso

Para crear una animación, solo necesitas importar `anim` y definir una función que registre tus imágenes.

```python
import anim

def mi_animacion():
    anim.init()
    anim.name("Mi Primera Animación")
    anim.render.fremis(10) # 10 FPS
    anim.canva.size(400, 400)
    
    def cargar_recursos(data):
        # El método .imagen es inyectado dinámicamente
        anim.pygame.imagen("frame1.png")
        anim.pygame.imagen("frame2.png")
        
    anim.run(cargar_recursos)

if __name__ == "__main__":
    mi_animacion()
```

## 📖 Referencia de la API

### `anim.init()`
Inicializa los módulos internos de Pygame. Debe llamarse al inicio.

### `anim.name(titulo: str)`
Define el título de la ventana de visualización.

### `anim.render.fremis(fps: int)`
Configura la velocidad de la animación en fotogramas por segundo.

### `anim.canva.size(w, h)`
Establece el tamaño de la ventana (Surface principal).

### `anim.pygame.imagen(ruta: str)`
Este método es una extensión de la librería Pygame original. Carga la imagen, la optimiza para transparencia (`convert_alpha`) y la añade automáticamente a la lista de reproducción de la animación actual.

### `anim.run(callback)`
Inicia el bucle principal del juego. Recibe una función de configuración donde se cargan los recursos antes de empezar el renderizado secuencial.