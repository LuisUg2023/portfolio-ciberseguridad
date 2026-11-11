# 08. Conceptos relacionados con archivos .conf

**Duración:** 4 minutos.

## Objetivo
Entender el papel de los archivos de configuración en Splunk.

Los archivos .conf contienen parámetros que determinan cómo Splunk recibe, procesa, almacena, busca y protege los datos.

## Directorios habituales

~~~text
$SPLUNK_HOME/etc/
├── system/
│   ├── default/
│   └── local/
└── apps/
    └── nombre_app/
        ├── default/
        └── local/
~~~

## Recomendaciones
- No modificar directamente $SPLUNK_HOME/etc/system/default/.
- Para personalizaciones locales, utilizar system/local o, preferentemente, la aplicación correspondiente.
- Mantener las configuraciones versionadas y documentadas.
- Revisar precedencia y contexto de aplicación antes de modificar parámetros.

## Archivos principales
- inputs.conf: fuentes de entrada.
- outputs.conf: destinos y envío.
- props.conf: propiedades de datos y reglas asociadas.
- transforms.conf: transformaciones y reglas de extracción/enrutamiento.
- indexes.conf: definición de índices y almacenamiento.
- savedsearches.conf: búsquedas guardadas y alertas.
- authentication.conf: configuración de autenticación.
- authorize.conf: roles y capacidades.

Validar sintaxis y comportamiento en un entorno de pruebas. La aplicabilidad de cada parámetro depende de la versión y del rol Splunk.
