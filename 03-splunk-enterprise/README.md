# Complemento técnico. Introducción a Splunk Enterprise

## Objetivo
Documentar los fundamentos de Splunk Enterprise desde la recepción de machine data hasta su indexación, búsqueda, análisis y visualización. El módulo toma como fuente principal el documento de estudio SPLUNK-INTRO.odt, sus diagramas y el índice de 11 videos del curso.

> Este módulo organiza el contenido de estudio. Las prácticas que requieran una instancia Splunk, capturas o resultados de ejecución se consideran realizadas únicamente cuando se incorporen evidencias reales. Los ejemplos ilustrativos no representan ejecuciones verificadas.

## Contenido del curso

| N.º | Lección | Duración | Contenido |
|---:|---|---:|---|
| 01 | [Carrera de Splunk](./01-carrera-splunk.md) | 8 min | Ecosistema y despliegue. |
| 02 | [Splunk vs. ELK vs. Sumo Logic](./02-comparativa-plataformas.md) | 7 min | Comparación de alternativas. |
| 03 | [Casos de uso de Splunk](./03-casos-de-uso.md) | 8 min | Visibilidad operacional, seguridad e investigación. |
| 04 | [Etapas de la canalización](./04-data-pipeline.md) | 3 min | Input, parsing, indexing y searching. |
| 05 | [Componentes](./05-componentes.md) | 9 min | Forwarder, Indexer y Search Head. |
| 06 | [Arquitectura](./06-arquitectura.md) | 3 min | Componentes, flujos y despliegue distribuido. |
| 07 | [Campos de Splunk](./07-fields.md) | 11 min | Fields, pares clave-valor y extracción. |
| 08 | [Conceptos de archivos .conf](./08-conceptos-conf.md) | 4 min | Archivos de configuración y buenas prácticas. |
| 09 | [Archivos .conf comunes](./09-archivos-conf.md) | 7 min | Inputs, outputs, props, saved searches, indexes y acceso. |
| 10 | [Index-time vs. Search-time](./10-index-vs-search-time.md) | 2 min | Procesamiento de ingesta y búsqueda. |
| 11 | [Preguntas de entrevista](./11-preguntas-entrevista.md) | 31 min | Arquitectura, Knowledge Objects, clustering y SPL. |

## Imágenes del documento fuente

Los archivos gráficos se entregan en el paquete ZIP complementario y deben subirse a esta carpeta para activar las referencias visuales.
Las imágenes se guardarán en la carpeta assets cuando se incorporen al repositorio:
- 01-data-pipeline.png
- 02-componentes.png
- 03-arquitectura-internals.png
- 04-fields-extraction.png
- 05-configuracion-conf.png
- 06-archivos-conf-comunes.jpg
- 07-index-vs-search-time.jpg

## Estructura
Cada lección incluye objetivo, conceptos principales, tablas o diagramas y ejemplos cuando el documento fuente los permite. La información que depende de la versión o licencia se identifica como tal y debe verificarse antes de aplicarse en producción.

## Fuente
Documento de estudio SPLUNK-INTRO.odt, páginas 1–6, e índice de 11 videos proporcionado para este módulo.

## Criterios de evidencia
- No publicar direcciones IP, nombres de host, usuarios, tokens ni datos sensibles reales.
- Separar comandos, configuración, resultados esperados y observaciones verificadas.
- No afirmar que un laboratorio fue ejecutado sin evidencia.
- Verificar parámetros y comportamiento con la documentación de la versión instalada.
