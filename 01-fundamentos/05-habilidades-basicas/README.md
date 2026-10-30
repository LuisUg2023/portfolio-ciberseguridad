# Actividad 5. Conocimientos y habilidades básicas

**Estado:** En desarrollo

## 1. Objetivo
Identificar las competencias esenciales de un analista de ciberseguridad y relacionarlas con tareas prácticas de observación, análisis, documentación y comunicación.

## 2. Competencias técnicas

| Competencia | Aplicación | Evidencia que se puede construir |
|---|---|---|
| Redes | Comprender IP, DNS, puertos, TCP/UDP y HTTP/HTTPS | Diagrama de red y análisis de una captura |
| Sistemas operativos | Administrar permisos, procesos y servicios | Registro de comandos y configuración de laboratorio |
| Linux | Navegar directorios, filtrar texto y revisar logs | Ejercicios de terminal |
| Windows | Revisar eventos, usuarios y servicios | Análisis de eventos de laboratorio |
| SQL | Consultar y relacionar registros | Consultas sobre base de datos de práctica |
| Python | Automatizar tareas repetitivas | Script documentado |
| Seguridad web | Reconocer autenticación, sesiones y validación de entradas | Lista de verificación de aplicación |
| Análisis | Separar observaciones, hipótesis y conclusiones | Informe técnico |
| Comunicación | Explicar impacto y mitigación | Resumen ejecutivo para responsables |

## 3. Flujo básico de análisis
1. **Preparar:** definir objetivo, autorización y alcance.
2. **Observar:** recopilar registros y datos relevantes.
3. **Normalizar:** ordenar fechas, campos, direcciones y eventos.
4. **Analizar:** buscar patrones, anomalías y relaciones.
5. **Validar:** comprobar hipótesis con fuentes independientes.
6. **Priorizar:** considerar impacto, probabilidad y criticidad del activo.
7. **Comunicar:** redactar hallazgos claros y accionables.
8. **Cerrar:** conservar evidencia necesaria y proteger o eliminar datos según el procedimiento.

## 4. Ejemplo de lectura de un registro
Registro ficticio:

```text
2026-10-01T10:15:32Z AUTH_FAIL user=usuario_demo src=192.0.2.25
2026-10-01T10:15:48Z AUTH_FAIL user=usuario_demo src=192.0.2.25
2026-10-01T10:16:02Z AUTH_SUCCESS user=usuario_demo src=192.0.2.25
```

**Observación:** se registran dos fallos de autenticación seguidos de un acceso exitoso desde la misma dirección de documentación.

**Hipótesis:** podría tratarse de un error de digitación o de un intento de acceso no autorizado.

**Validación necesaria:** correlacionar con MFA, dispositivo, geolocalización confiable, horario habitual y eventos posteriores. El fragmento por sí solo no demuestra un incidente.

## 5. Habilidades no técnicas
- Pensamiento crítico y atención al detalle.
- Comunicación escrita y oral.
- Gestión del tiempo y priorización.
- Trabajo colaborativo y escalamiento oportuno.
- Respeto a la confidencialidad y a los procedimientos.

## 6. Autoevaluación
Califica cada competencia de 1 a 5: 1 = necesito formación inicial; 5 = puedo demostrarla de forma autónoma.

| Competencia | Nivel (1–5) | Próxima acción |
|---|---:|---|
| Redes y protocolos | Por completar | Realizar práctica de captura |
| Linux y línea de comandos | Por completar | Analizar logs |
| Windows y eventos | Por completar | Revisar Event Viewer |
| SQL | Por completar | Practicar consultas |
| Python | Por completar | Crear script básico |
| Redacción de informes | Por completar | Documentar un caso |

No se asignan puntuaciones sin autoevaluación del estudiante.

## 7. Conclusión preliminar
El trabajo de un analista requiere combinar fundamentos técnicos con capacidad de validar hipótesis y comunicar hallazgos. La documentación reproducible es parte de la evidencia, no un complemento opcional.

## 8. Referencias
- NICE Framework. https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center
- NIST Cybersecurity Framework 2.0. https://www.nist.gov/cyberframework

## 9. Pendiente para completar
- [ ] Completar la autoevaluación con ejemplos reales de aprendizaje.
- [ ] Añadir una práctica de análisis de registros.
- [ ] Incorporar una reflexión sobre las competencias por fortalecer.
