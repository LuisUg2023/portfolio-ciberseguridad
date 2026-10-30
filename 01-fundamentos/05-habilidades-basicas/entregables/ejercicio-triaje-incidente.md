# Ejercicio de triaje: actividad de autenticación sospechosa

## Escenario
Aplicación ficticia registra varios intentos fallidos y posteriormente un inicio de sesión correcto desde una dirección no habitual. Los datos son sintéticos.

## Datos de muestra
| Hora UTC | Usuario | IP de origen | Evento |
|---|---|---|---|
| 10:01 | mlopez | 198.51.100.24 | LOGIN_FAILED |
| 10:02 | mlopez | 198.51.100.24 | LOGIN_FAILED |
| 10:03 | mlopez | 198.51.100.24 | LOGIN_FAILED |
| 10:04 | mlopez | 198.51.100.24 | LOGIN_SUCCESS |
| 10:06 | admin | 203.0.113.8 | LOGIN_FAILED |

Las direcciones pertenecen a rangos reservados para documentación; no identifican equipos reales.

## Procedimiento de análisis
1. Validar zona horaria y sincronización de reloj.
2. Agrupar eventos por usuario, IP y ventana temporal.
3. Correlacionar con MFA, geolocalización corporativa autorizada, dispositivo y cambios de privilegios.
4. Determinar si el éxito posterior a fallos requiere investigación; no asumir compromiso solo por el patrón.
5. Preservar registros originales y documentar hash, origen y hora de adquisición.

## Clasificación inicial
- Severidad provisional: media, sujeta a contexto y criticidad de la cuenta.
- Hipótesis: fuerza bruta/credential stuffing o error legítimo del usuario.
- Acciones: validar con titular por canal alternativo, revisar MFA/sesiones, revocar sesiones si se confirma riesgo y escalar según procedimiento.

## Informe breve
- Qué ocurrió:
- Alcance confirmado:
- Evidencias:
- Impacto:
- Acciones realizadas:
- Recomendaciones:
- Estado: ejercicio de escritorio; no es un incidente real.