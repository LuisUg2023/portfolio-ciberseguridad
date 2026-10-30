# Actividad 1. Marcos y controles de ciberseguridad

**Estado:** En desarrollo  
**Tipo de evidencia:** análisis documental y diseño de controles  
**Escenario:** organización ficticia de servicios con aplicación web, cuentas de usuario y datos de clientes.

## 1. Objetivo
Reconocer la función de los marcos de ciberseguridad y seleccionar controles que permitan gestionar riesgos de confidencialidad, integridad y disponibilidad (CIA).

## 2. Conceptos fundamentales
- **Marco de ciberseguridad:** estructura de resultados, prácticas y recomendaciones para organizar la gestión de seguridad.
- **Control de seguridad:** salvaguarda administrativa, técnica o física que modifica la probabilidad o el impacto de un riesgo.
- **Política:** establece directrices y responsabilidades.
- **Procedimiento:** describe cómo ejecutar una actividad.
- **Evidencia:** registro verificable que permite demostrar que una actividad o control se ejecutó.

## 3. Marcos de referencia

| Marco | Enfoque | Uso en el escenario |
|---|---|---|
| NIST Cybersecurity Framework 2.0 | Gobernar, identificar, proteger, detectar, responder y recuperar | Organizar el programa de ciberseguridad y sus resultados |
| ISO/IEC 27001:2022 | Sistema de gestión de seguridad de la información | Definir contexto, riesgos, tratamiento y mejora continua |
| ISO/IEC 27002:2022 | Catálogo de controles de seguridad | Orientar la selección de controles |
| CIS Critical Security Controls v8.1 | Salvaguardas priorizadas | Establecer una línea base técnica y operativa |
| OWASP Top 10 (2021) | Riesgos frecuentes de aplicaciones web | Orientar revisiones de desarrollo y seguridad web |

Los marcos no son intercambiables: NIST CSF organiza resultados; ISO/IEC 27001 establece requisitos para un sistema de gestión; ISO/IEC 27002 aporta orientación sobre controles; CIS prioriza salvaguardas; OWASP se enfoca en riesgos de aplicaciones.

## 4. Selección inicial de controles

| Riesgo o necesidad | Control propuesto | Naturaleza | Evidencia esperada |
|---|---|---|---|
| Acceso indebido a cuentas | MFA y mínimo privilegio | Preventivo | Configuración y revisión de accesos |
| Pérdida de información | Copias de seguridad y prueba de restauración | Preventivo/correctivo | Registro de respaldo y restauración |
| Explotación de vulnerabilidades | Gestión de parches | Preventivo | Inventario y reporte de actualizaciones |
| Actividad sospechosa no detectada | Centralización y revisión de registros | Detectivo | Alertas y bitácora de análisis |
| Exposición de aplicación web | Validación de entradas y pruebas de seguridad | Preventivo/detectivo | Casos de prueba y resultados |
| Error humano o phishing | Capacitación y procedimiento de reporte | Preventivo | Material y registro de capacitación |

## 5. Método de selección
1. Identificar el activo y su propietario.
2. Describir la amenaza y la debilidad que podría aprovechar.
3. Estimar probabilidad e impacto.
4. Seleccionar controles proporcionales al riesgo.
5. Definir responsable, frecuencia y evidencia.
6. Verificar si el control funciona y registrar excepciones.

## 6. Ejercicio aplicado
**Situación:** la aplicación web permite iniciar sesión con contraseña, pero no dispone de MFA.

- Activo: cuentas de usuarios.
- Amenaza: robo o reutilización de credenciales.
- Vulnerabilidad/condición: autenticación de un solo factor.
- Consecuencia: acceso no autorizado y exposición de información.
- Control recomendado: MFA, limitación de intentos, alertas de inicio de sesión y política de contraseñas.
- Evidencia por recopilar: configuración de autenticación, pruebas autorizadas y registros de eventos.

## 7. Conclusión preliminar
La selección de controles debe derivarse del riesgo y del contexto del activo. Adoptar un marco no garantiza por sí solo la seguridad: se requiere asignar responsables, medir la operación de los controles y mantener evidencia verificable.

## 8. Referencias
- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*. https://www.nist.gov/cyberframework
- ISO. *ISO/IEC 27001:2022 — Information security management systems*. https://www.iso.org/standard/27001
- ISO. *ISO/IEC 27002:2022 — Information security controls*. https://www.iso.org/standard/75652.html
- CIS. *CIS Critical Security Controls*. https://www.cisecurity.org/controls
- OWASP. *OWASP Top 10:2021*. https://owasp.org/Top10/

## 9. Pendiente para completar
- [ ] Confirmar qué marcos fueron abordados en las lecciones del curso.
- [ ] Añadir notas propias y ejemplos desarrollados durante el estudio.
- [ ] Incorporar una matriz descargable de controles y responsables.
- [ ] Adjuntar evidencias académicas propias, sin información sensible.
