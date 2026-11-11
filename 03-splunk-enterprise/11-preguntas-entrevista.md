# 11. Preguntas de entrevista de Splunk

**Duración:** 31 minutos.

Este repaso organiza las preguntas y respuestas de las páginas 5 y 6 del documento fuente. Los valores de licencias, defaults y funcionalidades dependientes de versión deben verificarse antes de una entrevista técnica.

## Conceptos fundamentales

**¿Qué es Splunk?**  
Una plataforma para obtener visibilidad sobre machine data generada por hardware, redes, servidores, dispositivos IoT y otras fuentes.

**¿Por qué se utiliza para analizar machine data?**
- Business Insights.
- Operational Visibility.
- Proactive Monitoring.
- Search & Investigation.

**¿Cuáles son los componentes principales?**  
Forwarders, Indexers y Search Heads. En despliegues grandes aparecen roles adicionales de administración.

**¿Cómo funciona Splunk?**  
El Forwarder recolecta y envía datos; el Indexer los procesa y almacena; el Search Head permite buscar, analizar y visualizar.

**¿Qué beneficios tienen los Forwarders?**  
Control de ancho de banda, transporte TCP/TLS, balanceo, caché local y reenvío cuando un Indexer no está disponible.

## Arquitectura y administración

**¿Qué roles pueden compartir máquina?**  
En despliegues pequeños pueden coexistir varios roles. En despliegues grandes se suelen dedicar recursos a Indexers y Search Heads. La distribución debe diseñarse según capacidad y carga.

**¿Para qué sirve la administración de licencias?**  
Controla el volumen de datos indexados frente al derecho de uso contratado. Los nombres y comportamientos del rol dependen de la arquitectura y versión.

**¿Qué es una License Violation?**  
Una situación en la que se supera el volumen permitido. Los umbrales y consecuencias consignados en apuntes antiguos no deben tratarse como reglas universales actuales.

## Knowledge Objects

**¿Qué casos de uso tienen?**  
El documento menciona seguridad física, monitoreo de aplicaciones, seguridad de red, listas de bloqueo mediante lookups y simplificación de búsquedas con Event Types y Tags.

**¿Por qué utilizar alertas?**  
Para notificar condiciones que requieren atención, por ejemplo más de tres intentos de login fallidos. El documento cita email, webhook, creación de tickets, throttling y adjuntar CSV/PDF.

**¿Qué son Workflow Actions?**  
Acciones que automatizan pasos después de reportes o búsquedas, como drill-down, transferencia de parámetros a otra búsqueda o envío de datos a otro servicio.

**¿Qué son Data Models y Pivot?**  
Los Data Models organizan datos en estructuras jerárquicas; Pivot facilita crear vistas y filtros visuales.

## Clustering

**¿Qué es Search Factor (SF) y Replication Factor (RF)?**
- RF: número total de copias de los datos.
- SF: número de copias disponibles para búsqueda.
- SF debe ser menor o igual que RF.
- El documento distingue Indexer Cluster y Search Head Cluster.

## SPL y lookups

**Comandos de filtrado mencionados:** search, where, sort y rex.

**¿Qué es Lookup?**  
Enriquece eventos con información externa o tablas auxiliares.

**Diferencia entre inputlookup y outputlookup:**
- inputlookup: lee registros desde una tabla lookup.
- outputlookup: escribe resultados en una tabla lookup.

**Diferencia entre eval, stats, chart y timechart:**
- eval: calcula o crea campos.
- stats: genera estadísticas agregadas.
- chart: genera resultados tabulares orientados a gráficos.
- timechart: agrega datos en intervalos temporales.

## Inputs y campos

**¿Qué tipos de inputs menciona el documento?**  
Files & Directories, puertos de red, scripts, Windows Registry, Print, Network y Active Directory Monitor.

**¿Cuáles son campos por defecto?**  
El documento enumera host, source, sourcetype, index y timestamp. La disponibilidad y comportamiento dependen de la fuente y el contexto.

**¿Cómo extraer campos?**  
Desde la lista de eventos, el panel lateral, Settings o mediante reglas Regex en props.conf.

**¿Cómo excluir eventos de la indexación?**  
El documento cita el enrutamiento a nullQueue mediante transforms.conf. La implementación requiere configuración cuidadosa en el punto de parsing adecuado.

**¿Por qué es importante Time Zone?**  
Para correlacionar eventos de distintas zonas geográficas y asignar correctamente el tiempo. Revisar la zona horaria de origen y las reglas configuradas.

**¿Qué es Sourcetype?**  
Identifica el formato de los datos y permite aplicar configuraciones como reconocimiento de timestamps y separación de eventos.

## Apps y visualización

**¿Diferencia entre App y Add-on?**  
El documento describe una App como una colección que puede incluir dashboards, reports, alerts y lookups; un Add-on suele centrarse en integraciones y conocimiento de datos sin una interfaz visual amplia.

**¿Cómo asignar colores en un gráfico?**  
El documento indica editar el panel del dashboard y modificar su configuración de visualización, incluyendo valores hexadecimales cuando la visualización lo permite.

## Preparación para entrevista
- Explicar el flujo Forwarder → Indexer → Search Head.
- Diferenciar parsing, indexing y searching.
- Explicar index-time frente a search-time.
- Describir la función de los archivos .conf.
- Construir búsquedas SPL con filtros, extracción y agregación.
- Explicar lookups, alertas y Knowledge Objects.
- Distinguir RF y SF.
- Separar conceptos aprendidos de experiencias realmente ejecutadas.
