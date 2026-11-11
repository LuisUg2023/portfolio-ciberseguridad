# Evaluación: fundamentos de búsqueda en Splunk Enterprise

**Módulo:** `03-splunk-enterprise`  
**Tema:** Search & Reporting, SPL, trabajos de búsqueda y objetos de conocimiento  
**Tipo:** Evaluación de selección múltiple  
**Preguntas:** 15

## Instrucciones

Lee cada pregunta y selecciona la opción u opciones que correspondan. Cuando la pregunta indique selección única, marca solo una respuesta. En las preguntas ambiguas se incluye una observación en la clave de respuestas para evitar memorizar una formulación incorrecta.

---

## Cuestionario

### 1. ¿Cuál búsqueda permite encontrar eventos que contengan los términos *error*, *contraseña* o la frase exacta *contraseña incorrecta*?

A. `incorrecta OR contraseña OR "contraseña incorrecta"`  
B. `incorrecta OR contraseña`  
C. `error*`  
D. `contraseña incorrecta OR "contraseña incorrecta"`

### 2. ¿Qué comando permite filtrar aún más los resultados de una búsqueda?

A. `filter`  
B. `search`  
C. `subsearch`  
D. `subset`

### 3. En una búsqueda ad hoc que finaliza, ¿cuál es el tiempo de vida predeterminado del trabajo de búsqueda?

A. 10 minutos  
B. 30 minutos  
C. 7 días  
D. 30 días

### 4. ¿Cuáles de los siguientes operadores booleanos se pueden utilizar en búsquedas de Splunk? *(Selección múltiple)*

A. `NOT`  
B. `OR`  
C. `AND`  
D. `ALSO`

### 5. ¿Qué determina la zona horaria en la que se muestran las marcas de tiempo de los eventos?

A. Siempre se muestran en la hora del meridiano de Greenwich (GMT).  
B. Siempre se muestran en tiempo Unix.  
C. La zona horaria donde se originó el evento.  
D. La zona horaria definida en las preferencias del usuario de Splunk.

### 6. ¿Qué carácter se utiliza antes de un comando para continuar el procesamiento de una búsqueda?

A. Virgulilla (`~`)  
B. Barra vertical (`|`)  
C. Acento grave (`)`  
D. Comilla (`"`)

### 7. ¿Qué búsqueda encuentra términos que comienzan por `error`, como `error` y `errores`?

A. `*error`  
B. `error*`  
C. `error`  
D. `error+`

### 8. De manera predeterminada, ¿en qué orden se muestran los eventos de una búsqueda?

A. Orden alfanumérico inverso  
B. Orden alfanumérico  
C. Orden cronológico  
D. Orden cronológico inverso

### 9. ¿Qué componente de Search & Reporting permite limitar el período de los resultados?

A. Selector de rango de tiempo  
B. Selector de hora  
C. Selector de tiempo  
D. Selector de intervalo de tiempo

### 10. ¿Cuál de estas aplicaciones se proporciona de manera predeterminada con Splunk Enterprise?

A. Splunk Machine Learning Toolkit  
B. Splunk Enterprise Security  
C. Search & Reporting  
D. Dashboard Examples

### 11. ¿Cuál es una forma eficaz de reducir el volumen de resultados que debe analizar una búsqueda?

A. Filtrar por `host`  
B. Filtrar por origen  
C. Restringir el índice  
D. Limitar el rango de tiempo

### 12. ¿Qué modo de búsqueda ajusta su comportamiento según el tipo de búsqueda que se ejecuta?

A. Inteligente  
B. Variable  
C. Rápido  
D. Detallado

### 13. ¿Qué roles predeterminados pueden compartir objetos de conocimiento? *(Revisar la terminología de la traducción del curso)*

A. Administrador  
B. Usuario  
C. Experto  
D. Gerente

### 14. De manera predeterminada, ¿quién puede ver un informe guardado con permisos privados?

A. Cualquier usuario con rol de experto o administrador  
B. Cualquier usuario que pueda ver informes  
C. Cualquier usuario de la organización  
D. El usuario que lo creó

### 15. En la búsqueda `| stats count by product_name`, ¿qué elemento representa el campo usado como argumento de agrupación?

A. `stats`  
B. `count`  
C. `by`  
D. `product_name`

---

## Clave de respuestas y explicación

| N.º | Respuesta | Explicación |
|---:|---|---|
| 1 | **Ninguna opción está completa.** | La consulta que expresa exactamente los tres criterios es `error OR contraseña OR "contraseña incorrecta"`. La opción A omite el término independiente `error`; por tanto, la pregunta original tiene una inconsistencia. |
| 2 | **B. `search`** | El comando `search` aplica condiciones adicionales para filtrar eventos. Una subbúsqueda es una búsqueda anidada cuyos resultados se usan dentro de otra búsqueda; no es el nombre del comando de filtrado general. |
| 3 | **A. 10 minutos** | Es el tiempo predeterminado para un trabajo de búsqueda ad hoc que finaliza. Los trabajos programados pueden tener otra duración. |
| 4 | **A, B y C.** | `NOT`, `OR` y `AND` son operadores booleanos admitidos. `ALSO` no lo es. |
| 5 | **D.** | Splunk presenta las marcas de tiempo de acuerdo con la zona horaria configurada para el usuario. |
| 6 | **B. Barra vertical (`|`).** | El pipe pasa los resultados de la búsqueda al comando siguiente. |
| 7 | **B. `error*`** | El comodín `*` permite coincidencias con cero o más caracteres después de `error`. Esto encuentra `error` y términos como `errores`, pero no `incorrecta`. |
| 8 | **D. Orden cronológico inverso.** | De forma predeterminada, los eventos más recientes aparecen primero. |
| 9 | **A. Selector de rango de tiempo.** | Permite definir el período que se consultará, por ejemplo, los últimos 15 minutos o las últimas 24 horas. |
| 10 | **C. Search & Reporting.** | Es la aplicación principal proporcionada de manera predeterminada con Splunk Enterprise. |
| 11 | **D. Limitar el rango de tiempo.** | Acotar el período reduce el conjunto de eventos que se examina. También pueden aplicarse filtros por índice, host y origen. |
| 12 | **A. Inteligente (Smart).** | Smart Mode adapta el comportamiento de búsqueda según el tipo de búsqueda. |
| 13 | **A y posiblemente C, según la traducción.** | En los roles estándar de Splunk, `admin` puede compartir objetos globalmente y `power` puede compartirlos dentro de una aplicación. Si “Experto” traduce `Power User`, marca Administrador y Experto. El nombre “Gerente” no es un rol estándar equivalente. |
| 14 | **D. El usuario que lo creó.** | Un informe guardado con permisos privados solo es visible para su propietario; debe compartirse para que otros usuarios puedan verlo. |
| 15 | **D. `product_name`.** | Es el campo por el que se agrupan los eventos. `stats` es el comando, `count` la función de agregación y `by` introduce la agrupación. |

## Correcciones importantes respecto a la formulación original

- **Pregunta 1:** ninguna opción reproduce los tres criterios solicitados. La consulta corregida es:
  ```spl
  error OR contraseña OR "contraseña incorrecta"
  ```
- **Pregunta 2:** el comando general para filtrar resultados es `search`. Una subbúsqueda (*subsearch*) es un mecanismo distinto.
- **Pregunta 4:** si la plataforma permite seleccionar varias respuestas, deben marcarse `NOT`, `OR` y `AND`. Si obliga a elegir solo una, la pregunta está mal configurada.
- **Pregunta 7:** `error*` no encuentra el término independiente `incorrecta`. Para ambos criterios se podría usar `error* OR incorrecta`.
- **Pregunta 13:** la opción “Experto” depende de si la traducción del curso corresponde al rol estándar `power` (*Power User*). En Splunk, los permisos de compartir varían según el ámbito: aplicación o global.

## Referencias oficiales

- [Splunk — Extending job lifetimes](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.4/manage-jobs/extending-job-lifetimes)
- [Splunk — Search and Reporting app](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/meet-splunk-apps/search-and-reporting-app)
- [Splunk — About jobs and job management](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.6/manage-jobs/about-jobs-and-job-management)

> **Criterio de rigor:** esta evaluación reúne las preguntas realizadas durante el repaso y conserva sus opciones. Las observaciones identifican las preguntas cuya traducción o alternativas son ambiguas. No se presentan como resultados de una ejecución en Splunk.
