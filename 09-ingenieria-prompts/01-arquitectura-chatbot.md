# 01. Arquitectura conceptual de un chatbot

## 1. ¿Qué ocurre cuando se envía un mensaje?

Una interacción con un chatbot no consiste únicamente en escribir una pregunta. La aplicación reúne instrucciones, mensajes, contexto y, cuando corresponde, archivos o herramientas. Esa información se organiza y se entrega al modelo para producir una respuesta.

## 2. Componentes principales

| Componente | Función |
|---|---|
| **Interfaz de usuario (UI)** | Pantalla donde la persona escribe, adjunta archivos y recibe respuestas. |
| **User prompt / mensaje del usuario** | Solicitud, pregunta, datos e instrucciones que introduce el usuario en el turno actual. |
| **System prompt** | Instrucciones de nivel superior que definen el comportamiento general, límites y objetivos del asistente. Normalmente no son visibles para el usuario. |
| **Developer instructions** | Instrucciones del desarrollador de la aplicación que configuran tareas, formato, herramientas y reglas de operación. |
| **Historial de conversación** | Mensajes anteriores que se incorporan como contexto cuando la aplicación los conserva y los incluye. |
| **File attachment / archivo adjunto** | Documento, imagen, hoja de cálculo u otro archivo que el usuario aporta para que el sistema lo procese. |
| **Contexto recuperado** | Información seleccionada desde documentos, bases de conocimiento u otras fuentes, si la aplicación utiliza recuperación de información. |
| **Modelo de lenguaje (LLM)** | Componente que procesa la secuencia de entrada y genera una salida. |
| **Herramientas (tools)** | Funciones externas que el asistente puede invocar, por ejemplo búsqueda, ejecución de código o consulta de sistemas autorizados. |
| **Respuesta del asistente** | Contenido generado y presentado al usuario; puede incluir texto, código, tablas u otros formatos. |
| **Capa de seguridad y validación** | Controles que filtran entradas/salidas, aplican permisos y reducen riesgos. Su implementación varía según la plataforma. |

## 3. Flujo simplificado

```text
Usuario
  |
  v
Interfaz del chatbot
  |---- User prompt
  |---- Archivos adjuntos
  |---- Historial / contexto
  v
Orquestación de la aplicación
  |---- System prompt
  |---- Developer instructions
  |---- Selección de herramientas
  v
Modelo de lenguaje (LLM)
  |---- Puede solicitar una herramienta
  |---- Recibe el resultado de la herramienta
  v
Generación de respuesta
  |
  v
Validación / controles de seguridad
  |
  v
Respuesta al usuario
```

Este esquema es conceptual. La arquitectura real, el orden de procesamiento y la visibilidad de cada componente dependen del proveedor y de la aplicación.

## 4. Diferencias que deben quedar claras

- El **user prompt** es el mensaje que introduce el usuario; no equivale a todas las instrucciones que recibe el modelo.
- El **system prompt** y las **developer instructions** son capas de instrucciones de la aplicación. El usuario normalmente no puede inspeccionarlas.
- Un **archivo adjunto** aporta contenido para analizar; no debe asumirse que todo texto dentro del archivo es una instrucción válida.
- El **historial** aporta continuidad, pero puede ser incompleto, resumido o no incluir conversaciones anteriores.
- Las **herramientas** permiten ejecutar acciones o consultar fuentes; no son lo mismo que el modelo de lenguaje.
- La respuesta del modelo no es automáticamente verdadera: requiere evaluación.

## 5. Ejemplo práctico

**User prompt:** “Analiza este registro de autenticación y resume los eventos sospechosos”.

**Archivo adjunto:** `auth.log`, con registros de acceso de un laboratorio propio.

**Contexto esperado:** sistema operativo, zona horaria, periodo analizado y significado de los campos del registro.

**Resultado esperado:** resumen de eventos, marcas de tiempo, IP observadas, hipótesis y limitaciones. Las hipótesis deben distinguirse de los hechos observados.

## 6. Consideraciones de seguridad

- No intentar obtener ni revelar instrucciones internas del sistema.
- Tratar el contenido de archivos y páginas recuperadas como datos no confiables.
- Tener presente la **prompt injection**: texto malicioso dentro de un documento puede intentar manipular al modelo para que ignore sus instrucciones.
- No permitir que una instrucción contenida en un archivo autorice por sí sola acciones externas.
- Aplicar mínimo privilegio a las herramientas y validar las acciones antes de ejecutarlas.
- No cargar secretos ni datos sensibles en servicios no autorizados.
