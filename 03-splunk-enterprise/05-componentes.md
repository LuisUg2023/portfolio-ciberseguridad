# 05. Componentes principales de Splunk

**Duración:** 9 minutos.

## Objetivo
Identificar los tres componentes principales descritos en el material.

| Componente | Responsabilidad | Función en el flujo |
|---|---|---|
| Splunk Forwarder | Recolectar y enviar datos. | Data Input. |
| Splunk Indexer | Procesar, indexar y almacenar eventos. | Parsing e Indexing. |
| Search Head | Permitir búsquedas, análisis y visualización. | Searching. |

~~~mermaid
flowchart LR
    A[Fuentes de datos] --> B[Forwarder]
    B --> C[Indexer]
    C --> D[Search Head]
    D --> E[Analista]
~~~

## Forwarders
El documento destaca:
- Control de ancho de banda.
- Conexión TCP + SSL.
- Balanceo de carga.
- Caché local de eventos.
- Reenvío automático si un Indexer deja de estar disponible.

## Roles adicionales
En despliegues grandes aparecen roles de administración, por ejemplo Deployment Server y administración de licencias. La separación física depende del tamaño y diseño del despliegue.

Imagen de referencia: página 1 del documento fuente, diagrama de componentes.
