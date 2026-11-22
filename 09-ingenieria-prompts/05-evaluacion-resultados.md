# 05. Evaluación de resultados, errores y supervisión humana

## 1. ¿Por qué evaluar las respuestas?

Una respuesta fluida puede contener errores, omisiones, información desactualizada o afirmaciones sin evidencia. La ingeniería de prompts requiere un proceso de control de calidad, no solo redactar una instrucción y aceptar el primer resultado.

## 2. Errores frecuentes

| Tipo de error | Descripción |
|---|---|
| Alucinación | El modelo genera información que no está respaldada por los datos disponibles. |
| Omisión | No incluye información relevante de la entrada. |
| Interpretación incorrecta | Comprende mal la solicitud o el contexto. |
| Inconsistencia | Presenta conclusiones contradictorias. |
| Error de formato | No respeta la estructura solicitada. |
| Sesgo | Produce resultados sistemáticamente inclinados por datos o patrones aprendidos. |
| Información desactualizada | Responde con datos que ya no reflejan la situación actual. |
| Falsa certeza | Presenta una hipótesis como si fuera un hecho comprobado. |

## 3. Proceso de evaluación

1. **Definir criterios:** exactitud, relevancia, integridad, trazabilidad y seguridad.
2. **Preparar casos de prueba:** ejemplos normales, límites, ambiguos y adversariales.
3. **Ejecutar:** utilizar el mismo conjunto de datos y condiciones comparables.
4. **Verificar:** contrastar afirmaciones con fuentes originales.
5. **Registrar:** documentar errores, impacto y frecuencia.
6. **Mejorar:** ajustar prompt, contexto, modelo o flujo de trabajo.
7. **Reevaluar:** repetir las pruebas para comprobar que la mejora no introdujo nuevos errores.

## 4. Rúbrica de evaluación

Califica cada dimensión de 1 a 5:

| Dimensión | Pregunta de control |
|---|---|
| Exactitud | ¿Las afirmaciones coinciden con la fuente? |
| Relevancia | ¿Responde a la tarea solicitada? |
| Integridad | ¿Incluye los elementos necesarios? |
| Trazabilidad | ¿Permite identificar de dónde sale cada dato? |
| Claridad | ¿La respuesta es comprensible y está organizada? |
| Seguridad | ¿Respeta privacidad, permisos y límites de uso? |

Una puntuación alta no sustituye la verificación de hechos críticos.

## 5. Delegación equilibrada

La IA puede apoyar tareas repetitivas, clasificación inicial, síntesis y elaboración de borradores. La persona debe conservar la responsabilidad de:
- definir el objetivo y el alcance;
- verificar datos y conclusiones;
- interpretar el contexto organizacional;
- aprobar decisiones de impacto;
- controlar el acceso a sistemas y datos;
- autorizar acciones sensibles.

## 6. Ejemplo SOC

La IA resume una alerta de múltiples intentos fallidos de autenticación. El analista debe verificar:
- si los eventos existen en el SIEM;
- si las marcas de tiempo y zonas horarias son correctas;
- si las direcciones IP corresponden a los registros;
- si hay eventos exitosos posteriores;
- si la hipótesis de fuerza bruta está respaldada por evidencia.

La IA puede asistir el análisis, pero no debe declarar automáticamente un incidente confirmado sin criterios y evidencias suficientes.

## 7. Registro de pruebas

| ID | Prompt / caso | Resultado esperado | Resultado observado | Error | Acción correctiva |
|---|---|---|---|---|---|
| T-001 | Resumen de registros ficticios | Extraer eventos sin inventar campos | Completar durante la práctica | Por evaluar | Por definir |
