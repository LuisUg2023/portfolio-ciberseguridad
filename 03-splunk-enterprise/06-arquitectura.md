# 06. Arquitectura de Splunk Enterprise

**Duración:** 3 minutos.

## Objetivo
Representar la interacción entre componentes y entender un despliegue distribuido.

~~~mermaid
flowchart TB
    subgraph Sources[Fuentes]
      A[Windows / Linux]
      B[Aplicaciones]
      C[Firewall / IDS]
      D[Syslog / APIs]
    end
    subgraph Collection[Recolección]
      E[Universal Forwarder]
      F[Heavy Forwarder opcional]
    end
    subgraph Indexing[Capa de indexación]
      G[Indexer Peer 1]
      H[Indexer Peer 2]
      I[Indexer Peer N]
      J[Cluster Manager]
    end
    subgraph Search[Capa de búsqueda]
      K[Search Head]
      L[Search Head Cluster opcional]
    end
    Sources --> E
    Sources --> F
    E --> G
    F --> G
    G <--> H
    H <--> I
    J -. administra .-> G
    J -. administra .-> H
    J -. administra .-> I
    K --> G
    K --> H
    K --> I
    L -. alta disponibilidad .-> K
    K --> M[Analista / Dashboard / Alertas]
~~~

## Componentes
- Universal Forwarder: recolección y envío con bajo consumo de recursos.
- Heavy Forwarder: puede realizar procesamiento adicional antes del envío.
- Indexer: parsing, indexación y almacenamiento.
- Cluster Manager: administra el clúster de indexadores.
- Search Head: coordina búsquedas y presenta resultados.
- Search Head Cluster: proporciona alta disponibilidad y escalabilidad a la capa de búsqueda.

## Clustering
- Replication Factor (RF): número total de copias de los datos.
- Search Factor (SF): número de copias disponibles para búsqueda.
- SF debe ser menor o igual que RF.
- Los valores predeterminados citados en apuntes deben verificarse para la versión y configuración utilizadas.

Imagen de referencia: página 2 del documento fuente, arquitectura interna de Splunk Enterprise.
