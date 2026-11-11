# 09. Archivos de configuración comunes

**Duración:** 7 minutos.

## Objetivo
Reconocer los archivos comunes y su responsabilidad.

| Archivo | Responsabilidad | Ejemplos de uso |
|---|---|---|
| inputs.conf | Definir entradas de datos. | Monitor de archivos, TCP/UDP y otros inputs admitidos. |
| outputs.conf | Definir destinos de envío. | Envío de eventos desde forwarders a indexers. |
| props.conf | Definir propiedades asociadas a datos y sourcetypes. | Timestamp, line breaking y asociación con extracciones. |
| savedsearches.conf | Definir búsquedas guardadas y alertas. | Programación, acciones y condiciones. |
| indexes.conf | Configurar índices y almacenamiento. | Retención, rutas y límites de buckets. |
| authentication.conf | Configurar autenticación. | Integración con mecanismos admitidos. |
| authorize.conf | Definir roles, capacidades y restricciones. | Permisos de búsqueda y acceso a índices. |
| transforms.conf | Definir transformaciones reutilizables. | Extracciones, lookups y enrutamiento. |

## Ejemplos mínimos ilustrativos

### inputs.conf
~~~ini
[monitor:///var/log/auth.log]
disabled = 1
index = security
sourcetype = linux_secure
~~~
El input está deshabilitado intencionalmente para evitar ingesta accidental al copiar el ejemplo.

### outputs.conf
~~~ini
[tcpout]
defaultGroup = indexers

[tcpout:indexers]
server = indexer01.example.net:9997
~~~
Usar solo con un destino de laboratorio real y configurado.

### props.conf
~~~ini
[linux_secure]
TIME_PREFIX = ^
MAX_TIMESTAMP_LOOKAHEAD = 16
~~~
Ajustar la configuración temporal al formato real de los eventos.

### savedsearches.conf
~~~ini
[Linux - Failed login attempts]
search = index=security sourcetype=linux_secure "Failed password"
enableSched = 0
~~~
La programación está deshabilitada en este ejemplo.

### indexes.conf
~~~ini
[security]
homePath = $SPLUNK_DB/security/db
coldPath = $SPLUNK_DB/security/colddb
thawedPath = $SPLUNK_DB/security/thaweddb
~~~
Las rutas y políticas deben dimensionarse según el almacenamiento disponible.

### authentication.conf y authorize.conf
Estos archivos pueden contener información sensible de autenticación y permisos. No publicar credenciales, hashes, secretos, datos de identidad ni configuraciones de una organización. Los ejemplos de roles deben construirse en laboratorio y revisarse según la versión.

## Flujo recomendado
1. Identificar qué componente utiliza el archivo.
2. Crear la configuración en el contexto de aplicación adecuado.
3. Revisar sintaxis y precedencia.
4. Validar con datos sintéticos.
5. Recargar o reiniciar solo cuando el cambio lo requiera.
6. Documentar el resultado observado y adjuntar evidencia sanitizada.

Imagen de referencia: página 3 del documento fuente, resumen de archivos comunes.
