# 10. Index-time vs. Search-time

**Duración:** 2 minutos.

## Objetivo
Distinguir el procesamiento anterior a la indexación del procesamiento realizado durante una búsqueda.

## Index-time Processing
El documento enumera:
1. Default Source Type.
2. Source Type Customization.
3. Index-time Field Extraction.
4. Event Timestamping.
5. Event Line Breaking.
6. Event Segmentation.

Como ejemplos de metadatos asociados menciona source, host y timestamp; también aborda sourcetype.

## Search-time Processing
El documento enumera:
1. Event Segmentation.
2. Event Type Matching.
3. Search-time Field Extraction.
4. Field Aliasing.
5. Field Lookups desde fuentes externas.
6. Sourcetype Renaming.
7. Tagging.

También menciona búsquedas, alertas y lookups como operaciones relacionadas con la etapa de búsqueda.

## Comparación

| Index-time | Search-time |
|---|---|
| Parsing y separación de eventos | Extracciones de campos al buscar |
| Reconocimiento de timestamp | Field aliases |
| Asignación de metadatos | Lookups |
| Personalización de sourcetype | Event types y tags |
| Transformaciones de ingesta | Renombrado de sourcetype, cuando se configura |

~~~mermaid
flowchart LR
    A[Raw event] --> B[Index-time processing]
    B --> C[(Indexed event)]
    C --> D[Search-time processing]
    D --> E[Search results]
~~~

## Ejemplo de búsqueda
Evento sintético:

~~~text
Nov 10 18:30:12 server01 sshd[1520]: Failed password for admin from 192.168.1.50 port 5522 ssh2
~~~

~~~spl
index=security sourcetype=linux_secure "Failed password"
| rex "Failed password for (?<user>\\S+) from (?<src_ip>\\d+\\.\\d+\\.\\d+\\.\\d+)"
| stats count by user src_ip
| sort - count
~~~

En este ejemplo, rex extrae user y src_ip durante la búsqueda.

**Nota:** la lista conserva los términos del video/documento. Event segmentation y event line breaking son conceptos distintos y no deben confundirse.
