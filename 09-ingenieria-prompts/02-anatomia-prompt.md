# 02. Anatomía de un prompt

## 1. Definición

Un **prompt** es la instrucción o entrada que se proporciona a un modelo de IA para orientar la tarea que debe realizar. La ingeniería de prompts consiste en diseñar y mejorar esas entradas para obtener resultados útiles, verificables y adecuados al contexto.

## 2. Elementos de un prompt eficaz

| Elemento | Qué especifica | Ejemplo |
|---|---|---|
| Rol o perspectiva | Enfoque desde el que debe responder | “Actúa como analista SOC de nivel 1”. |
| Objetivo | Qué debe conseguir | “Analiza los eventos de autenticación”. |
| Contexto | Información necesaria para interpretar la tarea | “Los registros pertenecen a un laboratorio Windows”. |
| Datos de entrada | Material que debe procesar | “Utiliza el extracto de auth.log adjunto”. |
| Tarea e instrucciones | Acciones concretas que debe realizar | “Agrupa por IP y detecta intentos repetidos”. |
| Restricciones | Qué debe evitar o respetar | “No inventes eventos ni atribuyas identidades”. |
| Formato de salida | Cómo presentar el resultado | “Entrega una tabla y un resumen ejecutivo”. |
| Criterios de calidad | Cómo comprobar que la respuesta sirve | “Incluye evidencia, incertidumbres y limitaciones”. |

## 3. Plantilla reutilizable

```text
ROL:
Actúa como [rol o especialidad].

OBJETIVO:
Necesito [resultado concreto].

CONTEXTO:
[Antecedentes, entorno, alcance y supuestos].

DATOS DE ENTRADA:
[Texto, archivo o información que debe analizarse].

INSTRUCCIONES:
1. [Primera acción].
2. [Segunda acción].
3. [Tercera acción].

RESTRICCIONES:
- No inventes información.
- Diferencia hechos, inferencias y recomendaciones.
- Señala los datos faltantes.
- Respeta los límites de seguridad y autorización.

FORMATO DE SALIDA:
[Tabla, lista, informe, código, JSON, etc.].

CRITERIOS DE VALIDACIÓN:
[Cómo evaluar exactitud, integridad y utilidad].
```

## 4. Ejemplo aplicado a ciberseguridad

**Prompt:**

“Actúa como analista SOC de nivel 1. Examina los eventos incluidos en el archivo adjunto. Identifica intentos fallidos de autenticación, agrúpalos por dirección IP y ventana temporal, y señala patrones que merezcan investigación. Presenta una tabla con hora, IP, cantidad de intentos y evidencia. Distingue observaciones de hipótesis. No atribuyas actividad a una persona ni declares un incidente confirmado sin evidencia suficiente. Si faltan campos, indícalo”.

## 5. Iteración del prompt

1. Definir el resultado esperado.
2. Ejecutar el prompt con datos de prueba autorizados.
3. Revisar la respuesta frente a los datos originales.
4. Identificar ambigüedades, omisiones o errores.
5. Ajustar contexto, instrucciones, restricciones o formato.
6. Repetir la evaluación con casos distintos.

Un prompt más largo no es necesariamente mejor. La calidad depende de la claridad, pertinencia y verificabilidad de sus instrucciones.
