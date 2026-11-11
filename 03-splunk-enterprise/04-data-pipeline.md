# 04. Etapas de la canalización de datos

**Duración:** 3 minutos.

## Objetivo
Comprender las etapas principales que atraviesan los datos en Splunk.

El documento identifica tres etapas generales: Data Input, Data Storage y Data Searching. El diagrama también muestra Input, Parsing, Indexing y Searching.

~~~mermaid
flowchart LR
    A[Data Input] --> B[Parsing / Event Parsing]
    B --> C[Indexing / Writing to Disk]
    C <--> D[(Disk / Index)]
    D --> E[Searching]
~~~

| Etapa | Función |
|---|---|
| Data Input | Recibir datos de archivos, sistemas, aplicaciones y fuentes de red. |
| Parsing | Interpretar la entrada, identificar límites de eventos y metadatos. |
| Indexing | Escribir eventos en estructuras de índice para su recuperación. |
| Searching | Consultar datos indexados y analizar resultados. |

**Relación con el procesamiento:**
- Index-time: procesamiento de ingesta, parsing y preparación antes y durante la indexación.
- Search-time: procesamiento realizado al ejecutar búsquedas sobre los datos indexados.

Imagen de referencia: página 1 del documento fuente, diagrama de etapas de la canalización.
