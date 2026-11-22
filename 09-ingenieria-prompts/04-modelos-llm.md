# 04. Modelos de lenguaje (LLM) y ejecución local

## 1. Modelo de lenguaje

Un **Language Model** es un modelo computacional que procesa secuencias de lenguaje y calcula continuaciones probables. Los modelos modernos se entrenan para realizar tareas como responder preguntas, resumir, clasificar y generar contenido.

Un **Large Language Model (LLM)** es un modelo de lenguaje de gran escala. Sus capacidades y limitaciones dependen de su arquitectura, datos, entrenamiento, configuración y herramientas disponibles.

## 2. Modelos alojados y modelos locales

| Característica | Modelo alojado / servicio remoto | Modelo local |
|---|---|---|
| Ejecución | Infraestructura del proveedor | Equipo o infraestructura administrada por el usuario |
| Conectividad | Normalmente requiere conexión | Puede funcionar sin conexión después de descargarlo |
| Privacidad | Depende de políticas, configuración y contrato del proveedor | Mayor control local, sujeto a la seguridad del equipo |
| Recursos | Principalmente gestionados por el proveedor | RAM, VRAM, CPU/GPU y almacenamiento propios |
| Mantenimiento | Gestionado en gran parte por el proveedor | Actualizaciones y operación a cargo del administrador |

## 3. Factores para seleccionar un modelo

- **Tamaño:** número de parámetros y requisitos de memoria.
- **Velocidad:** tiempo de respuesta y tokens generados por segundo.
- **Rendimiento:** capacidad para completar la tarea con los recursos disponibles.
- **Precisión:** corrección y consistencia de los resultados en una tarea concreta.
- **Ventana de contexto:** cantidad de información que puede procesar en una interacción.
- **Modalidades:** soporte para texto, imágenes, audio u otros tipos de entrada.
- **Privacidad y gobernanza:** tratamiento, retención y control de los datos.
- **Costo:** infraestructura, consumo o suscripción.

## 4. Equilibrio entre tamaño, velocidad y precisión

Un modelo de mayor tamaño puede requerir más memoria y cómputo, pero el tamaño por sí solo no garantiza mayor precisión. La cuantización, el hardware, la arquitectura y la tarea influyen en el rendimiento.

La selección debe realizarse mediante pruebas representativas, no únicamente por el número de parámetros.

## 5. Matriz de evaluación sugerida

| Criterio | Qué medir |
|---|---|
| Latencia | Tiempo hasta la primera respuesta y tiempo total |
| Velocidad de generación | Tokens por segundo, cuando esté disponible |
| Calidad | Exactitud, relevancia y completitud |
| Uso de recursos | RAM, VRAM, CPU/GPU |
| Contexto | Desempeño con entradas cortas y extensas |
| Privacidad | Dónde se procesan y almacenan los datos |
| Robustez | Comportamiento ante entradas ambiguas o maliciosas |

## 6. Aplicación en ciberseguridad

Antes de utilizar un LLM para analizar registros, alertas o código:
- definir si los datos pueden salir de la infraestructura;
- anonimizar o sintetizar información sensible;
- probar con muestras controladas;
- contrastar los resultados con fuentes originales;
- mantener revisión humana antes de ejecutar acciones.
