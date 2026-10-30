# Actividad 1. Marcos y controles de ciberseguridad

**Estado:** En desarrollo  
**Tipo de evidencia:** análisis documental, diseño de controles y matriz de tratamiento  
**Escenario:** organización ficticia de servicios con aplicación web, correo corporativo, estaciones de trabajo y base de datos.

> Este ejercicio es académico. El escenario y los datos son ficticios. No se han ejecutado auditorías ni pruebas sobre una organización real.

## 1. Objetivos de aprendizaje
Al terminar la actividad se espera poder:
- Explicar para qué sirven los marcos y estándares de ciberseguridad.
- Diferenciar un marco, un estándar, una política, un procedimiento y un control.
- Relacionar riesgos con controles preventivos, detectivos y correctivos.
- Definir responsables, evidencias e indicadores para verificar controles.
- Justificar la selección de controles según el contexto y el riesgo.

## 2. Conceptos fundamentales
- **Marco de ciberseguridad:** estructura de resultados y prácticas que ayuda a organizar un programa de seguridad.
- **Estándar:** conjunto formal de requisitos o especificaciones. Puede utilizarse como referencia para evaluar conformidad.
- **Control de seguridad:** salvaguarda administrativa, técnica o física que modifica la probabilidad o el impacto de un riesgo.
- **Política:** establece directrices, compromisos y responsabilidades.
- **Procedimiento:** describe los pasos para ejecutar una actividad.
- **Evidencia:** registro verificable que demuestra qué actividad se realizó, cuándo, por quién y con qué resultado.
- **Riesgo residual:** riesgo que permanece después de aplicar controles.

## 3. Marcos y referencias

| Referencia | Naturaleza y enfoque | Aplicación en el escenario |
|---|---|---|
| NIST Cybersecurity Framework 2.0 | Marco de resultados: Govern, Identify, Protect, Detect, Respond, Recover | Organizar y comunicar el programa de ciberseguridad |
| ISO/IEC 27001:2022 | Requisitos para un sistema de gestión de seguridad de la información (SGSI) | Gestionar contexto, riesgos, tratamiento, auditoría y mejora |
| ISO/IEC 27002:2022 | Guía de controles de seguridad | Orientar la selección e implementación de controles |
| CIS Critical Security Controls v8.1 | Conjunto priorizado de salvaguardas | Establecer una línea base técnica y operativa |
| OWASP Top 10:2021 | Documento de concienciación sobre riesgos de aplicaciones web | Orientar el análisis de riesgos de la aplicación |

Estas referencias no son intercambiables. NIST CSF organiza resultados; ISO/IEC 27001 establece requisitos de gestión; ISO/IEC 27002 orienta sobre controles; CIS prioriza salvaguardas; OWASP se enfoca en riesgos de aplicaciones.

## 4. Caso práctico y alcance
La organización ficticia procesa solicitudes de clientes mediante una aplicación web. Mantiene cuentas de usuario, correo corporativo, estaciones de trabajo y una base de datos.

**Incluido:** diseño conceptual de controles de acceso, protección de datos, seguridad de aplicaciones, registros, copias de seguridad y capacitación.

**Excluido:** pruebas de intrusión, escaneo de redes, acceso a sistemas de terceros, uso de datos reales y afirmaciones de cumplimiento normativo.

### Inventario resumido

| ID | Activo | Información o función | Necesidad principal |
|---|---|---|---|
| A-01 | Aplicación web | Servicio a clientes | Disponibilidad e integridad |
| A-02 | Base de datos | Registros de clientes | Confidencialidad e integridad |
| A-03 | Correo corporativo | Comunicación y recuperación de cuentas | Confidencialidad |
| A-04 | Estaciones de trabajo | Operación diaria | Integridad y disponibilidad |
| A-05 | Copias de seguridad | Recuperación de información | Disponibilidad e integridad |

## 5. Riesgos y controles seleccionados

| ID | Escenario de riesgo | Control propuesto | Tipo |
|---|---|---|---|
| R-01 | Compromiso de una cuenta por robo de credenciales | MFA, mínimo privilegio y revisión de accesos | Preventivo |
| R-02 | Explotación de una aplicación desactualizada | Gestión de vulnerabilidades y parches | Preventivo |
| R-03 | Pérdida de información por respaldo no recuperable | Copias de seguridad y pruebas de restauración | Preventivo/correctivo |
| R-04 | Actividad anómala no identificada | Registro centralizado, alertas y revisión | Detectivo |
| R-05 | Exposición de datos por permisos excesivos | RBAC, segregación de funciones y revisiones | Preventivo |
| R-06 | Inyección o validación incorrecta en la aplicación | Validación del lado servidor, consultas parametrizadas y pruebas | Preventivo/detectivo |
| R-07 | Phishing y error humano | Capacitación, filtros y mecanismo de reporte | Preventivo/detectivo |

La matriz detallada se encuentra en [entregables/matriz-controles.csv](./entregables/matriz-controles.csv).

## 6. Método de selección
1. Identificar el activo, su propietario y la información que procesa.
2. Describir el escenario de amenaza y la debilidad que podría aprovechar.
3. Estimar probabilidad e impacto usando criterios definidos.
4. Seleccionar controles proporcionales al riesgo.
5. Asignar responsable, frecuencia, evidencia e indicador.
6. Verificar el funcionamiento del control y registrar excepciones.
7. Reevaluar el riesgo residual y aprobar su tratamiento.

### Clasificación de controles
- **Preventivo:** reduce la probabilidad de que ocurra un evento.
- **Detectivo:** permite identificar un evento o una desviación.
- **Correctivo/recuperación:** limita consecuencias y permite restaurar la operación.

Un mismo control puede contribuir a más de una función.

## 7. Desarrollo del escenario R-01: compromiso de cuenta
**Situación:** la aplicación permite iniciar sesión con contraseña y no dispone de autenticación multifactor.

- Activo: cuentas de usuarios.
- Amenaza: robo, phishing o reutilización de credenciales.
- Condición vulnerable: autenticación de un solo factor.
- Evento: un tercero utiliza credenciales comprometidas.
- Consecuencias posibles: acceso no autorizado, exposición o modificación de información.
- Controles recomendados: MFA, limitación de intentos, alertas de inicio de sesión, revisión de privilegios y procedimiento de recuperación.
- Evidencia esperada: política de autenticación, configuración, registro de pruebas autorizadas y bitácora de revisión.

**Criterio de verificación:** comprobar que MFA esté habilitado para las cuentas definidas en el alcance y que el proceso de recuperación no permita eludirlo fácilmente. No se debe probar contra cuentas reales sin autorización.

## 8. Indicadores para seguimiento

| Indicador | Fórmula orientativa | Frecuencia |
|---|---|---|
| Cobertura MFA | Cuentas con MFA / cuentas dentro del alcance × 100 | Mensual |
| Parches dentro del plazo | Activos parcheados en plazo / activos que requerían parche × 100 | Mensual |
| Éxito de restauración | Pruebas de restauración exitosas / pruebas ejecutadas × 100 | Trimestral |
| Revisión de accesos | Cuentas revisadas / cuentas programadas para revisión × 100 | Trimestral |
| Alertas atendidas | Alertas triadas / alertas recibidas × 100 | Mensual |

Los indicadores requieren definir alcance, fuente de datos, responsable y umbral objetivo antes de utilizarlos.

## 9. Conclusión
La selección de controles debe derivarse del riesgo y del contexto de los activos. Adoptar un marco no garantiza por sí solo la seguridad: se requiere asignar responsables, verificar la operación de los controles, conservar evidencias y revisar el riesgo residual. La matriz propuesta es una línea base académica y no una declaración de cumplimiento.

## 10. Referencias
- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*. https://www.nist.gov/cyberframework
- NIST. *CSF 2.0 Resource & Reference Tool*. https://www.nist.gov/cyberframework/resources
- ISO. *ISO/IEC 27001:2022 — Information security management systems*. https://www.iso.org/standard/27001
- ISO. *ISO/IEC 27002:2022 — Information security controls*. https://www.iso.org/standard/75652.html
- CIS. *CIS Critical Security Controls*. https://www.cisecurity.org/controls
- OWASP. *OWASP Top 10:2021*. https://owasp.org/Top10/

## 11. Pendiente para completar con el curso
- [ ] Contrastar los conceptos con las lecciones y lecturas exactas de Coursera.
- [ ] Incorporar notas personales y ejemplos trabajados en las actividades del curso.
- [ ] Completar la columna de evidencia con resultados obtenidos en el laboratorio.
- [ ] Revisar la valoración de riesgos con criterios acordados.
- [ ] Añadir capturas sanitizadas y archivos de soporte.
- [ ] Registrar fecha, versiones de herramientas y responsable de cada práctica.

## 12. Historial de cambios
- Primera versión ampliada: caso ficticio, comparación de referencias, riesgos, controles e indicadores.
