# Actividad 3. Amenazas, riesgos y vulnerabilidades

**Estado:** En desarrollo  
**Escenario:** organización ficticia que utiliza correo corporativo y una aplicación web.

## 1. Objetivo
Distinguir activos, amenazas, vulnerabilidades y riesgos; construir escenarios de riesgo y priorizar acciones de tratamiento.

## 2. Definiciones
- **Activo:** recurso con valor para la organización (información, sistema, equipo, servicio o persona).
- **Amenaza:** circunstancia o actor capaz de causar un efecto adverso.
- **Vulnerabilidad:** debilidad que puede ser aprovechada por una amenaza.
- **Riesgo:** efecto de la incertidumbre sobre los objetivos; en este ejercicio se estima a partir de probabilidad e impacto.
- **Control:** medida que modifica la probabilidad o las consecuencias de un evento.

**Ejemplo:** el phishing es una amenaza; la ausencia de MFA puede aumentar la exposición; una cuenta comprometida es un escenario; el acceso no autorizado a datos es una consecuencia.

## 3. Inventario de activos de ejemplo

| ID | Activo | Información/función | Prioridad inicial |
|---|---|---|---|
| A-01 | Aplicación web | Servicio a clientes | Alta |
| A-02 | Base de datos | Registros de clientes | Alta |
| A-03 | Correo corporativo | Comunicación y recuperación de cuentas | Alta |
| A-04 | Estaciones de trabajo | Operación diaria | Media |
| A-05 | Copias de seguridad | Recuperación de información | Alta |

La prioridad es ilustrativa y debe validarse con el propietario del proceso.

## 4. Método cualitativo de valoración
Escala de probabilidad e impacto: 1 (bajo), 2 (medio), 3 (alto).  
Puntuación = probabilidad × impacto.

| Resultado | Nivel orientativo |
|---|---|
| 1–2 | Bajo |
| 3–4 | Medio |
| 6–9 | Alto |

Esta matriz es una herramienta académica simplificada, no una medición estadística.

## 5. Registro inicial de riesgos

| ID | Escenario | Prob. | Impacto | Nivel | Tratamiento propuesto |
|---|---|---:|---:|---|---|
| R-01 | Phishing compromete una cuenta de correo | 3 | 3 | Alto (9) | MFA, filtros, capacitación y alertas |
| R-02 | Aplicación sin parches contiene una falla explotable | 2 | 3 | Alto (6) | Inventario, gestión de parches y pruebas |
| R-03 | Pérdida de datos por respaldo no recuperable | 2 | 3 | Alto (6) | Copias 3-2-1 y pruebas de restauración |
| R-04 | Equipo extraviado expone información local | 2 | 2 | Medio (4) | Cifrado, bloqueo y borrado remoto autorizado |
| R-05 | Acceso excesivo de una cuenta interna | 2 | 3 | Alto (6) | RBAC, mínimo privilegio y revisión periódica |

## 6. Análisis de un escenario
**R-01: compromiso de correo por phishing**
- Activo: cuenta de correo corporativo.
- Amenaza: campaña de phishing.
- Debilidad: usuario entrega credenciales o reutiliza una contraseña.
- Evento: tercero obtiene acceso a la cuenta.
- Impacto posible: fraude, exposición de información y uso de la cuenta para nuevos ataques.
- Controles: MFA resistente al phishing cuando sea viable, protección de correo, capacitación, alertas de acceso y procedimiento de recuperación.
- Indicador: porcentaje de cuentas con MFA y tiempo de revocación de sesiones sospechosas.

## 7. Opciones de tratamiento
- **Mitigar:** implementar controles para reducir probabilidad o impacto.
- **Evitar:** dejar de realizar la actividad que origina el riesgo.
- **Transferir/compartir:** distribuir parte del impacto mediante acuerdos o seguros, sin eliminar la responsabilidad.
- **Aceptar:** asumir formalmente el riesgo residual dentro del apetito aprobado.

## 8. Conclusión preliminar
La identificación de amenazas no basta: es necesario vincular cada escenario con un activo, una vulnerabilidad o condición, una consecuencia y un tratamiento verificable. La valoración debe revisarse cuando cambien los sistemas o las amenazas.

## 9. Referencias
- NIST. *SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments*. https://csrc.nist.gov/pubs/sp/800/30/r1/final
- NIST. *Cybersecurity Framework 2.0*. https://www.nist.gov/cyberframework
- CISA. *Secure Our World*. https://www.cisa.gov/secure-our-world

## 10. Pendiente para completar
- [ ] Validar la escala de valoración con el material del curso.
- [ ] Añadir un diagrama de relación activo-amenaza-vulnerabilidad-riesgo.
- [ ] Documentar riesgos residuales y responsables.
