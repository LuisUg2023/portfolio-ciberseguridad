# 07. Campos de Splunk (Fields)

**Duración:** 11 minutos.

## Objetivo
Comprender cómo los campos convierten eventos en información consultable.

## Conceptos
- Un campo es un nombre asociado a un valor: employee_name=J y employee_id=00124.
- Los campos filtran eventos y permiten obtener información específica.
- Son componentes básicos de búsquedas, informes y modelos de datos.
- Un campo puede tener múltiples valores.
- Los nombres de campo distinguen entre mayúsculas y minúsculas.

## Ejemplo de extracción
Evento sintético:

~~~text
GET / HTTP/1.1
User-Agent: Mozilla/5.0 Chrome/537.36
~~~

Regex:

~~~regex
537\.36
~~~

Si la extracción se guarda con el nombre test, la búsqueda puede consultar ese campo.

~~~spl
index=web test="537.36"
| table _time host source sourcetype test
~~~

## Métodos mencionados
1. Field Extractor desde Splunk Web.
2. Regex para eventos no estructurados.
3. Delimitadores para datos estructurados.
4. Configuración mediante props.conf y transforms.conf.

## Tipos
- Index-time: extracción o asignación durante la ingesta/indexación; puede afectar almacenamiento y requerir reindexación para modificar datos históricos.
- Search-time: extracción durante la búsqueda; permite cambiar reglas sin reindexar eventos.

Imagen de referencia: página 2 del documento fuente, infografía de extracción de campos.
