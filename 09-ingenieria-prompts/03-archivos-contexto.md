# 03. Archivos adjuntos, contexto y flujo de información

## 1. ¿Qué es un archivo adjunto?

Un **file attachment** es un archivo que el usuario incorpora a la conversación para que el chatbot lo consulte o procese. Según las capacidades de la plataforma, puede ser un PDF, DOCX, TXT, CSV, XLSX, imagen, código u otro formato admitido.

El archivo no es necesariamente una instrucción: normalmente es una fuente de datos para la tarea indicada en el prompt.

## 2. Diferencia entre prompt y archivo

| User prompt | Archivo adjunto |
|---|---|
| Explica qué tarea realizar. | Contiene datos o material de referencia. |
| Define el objetivo, alcance y formato. | Aporta evidencia o contexto documental. |
| Puede indicar qué partes analizar. | Puede contener texto, tablas, imágenes o código. |
| Debe especificar cómo tratar la información. | Debe revisarse según su integridad y confiabilidad. |

**Ejemplo:** el prompt solicita “resume los hallazgos del informe”; el PDF adjunto es el informe que debe analizarse.

## 3. Formas de introducir información

- **Texto directo:** pegar instrucciones o datos en el mensaje.
- **Archivo adjunto:** cargar documentos o evidencias.
- **Imagen:** aportar capturas, diagramas o fotografías para su interpretación.
- **Historial conversacional:** aprovechar mensajes previos que sigan disponibles en el contexto.
- **Contexto recuperado:** consultar documentos o bases de conocimiento mediante mecanismos de recuperación, cuando la aplicación los incorpora.
- **Herramientas o conectores:** obtener datos desde sistemas externos autorizados.

## 4. Formas de extraer información

- Resumen y extracción de puntos clave.
- Identificación de entidades, fechas, indicadores y campos.
- Conversión a tablas o formatos estructurados.
- Comparación entre documentos.
- Clasificación y etiquetado.
- Generación de preguntas, informes o borradores basados en las fuentes.

## 5. Flujo recomendado para trabajar con documentos

1. Identificar el propósito del análisis.
2. Verificar que el formato sea compatible.
3. Adjuntar el archivo correcto.
4. Indicar en el prompt qué secciones, páginas o campos interesan.
5. Solicitar que se señalen vacíos, ambigüedades y limitaciones.
6. Contrastar los resultados con el documento original.
7. Evitar divulgar información sensible.

## 6. Riesgos específicos

- **Prompt injection en archivos:** un documento puede contener texto que intente dar instrucciones al chatbot. Debe tratarse como contenido no confiable, no como una instrucción con autoridad.
- **Extracción incompleta:** tablas, escaneos o imágenes pueden no interpretarse correctamente.
- **Pérdida de contexto:** archivos extensos pueden procesarse por fragmentos o mediante recuperación selectiva.
- **Datos desactualizados:** un documento puede no representar el estado actual.
- **Exposición de información:** adjuntar documentos puede transmitir su contenido al proveedor del servicio, de acuerdo con la configuración y políticas de la plataforma.

## 7. Ejercicio de laboratorio

Utiliza un documento público o un archivo ficticio de registros de seguridad.

**Prompt:** “Analiza el archivo adjunto. Extrae fecha, evento, origen y resultado. Presenta una tabla. Cita la página o sección de origen cuando sea posible. No completes campos ausentes mediante suposiciones”.

**Validación:** compara una muestra de filas con el documento original y registra omisiones o errores.
