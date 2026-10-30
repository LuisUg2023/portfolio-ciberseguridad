# Actividad 4. Herramientas de ciberseguridad

**Estado:** En desarrollo  
**Objetivo:** reconocer herramientas comunes, su finalidad, sus límites y las precauciones necesarias para utilizarlas en un laboratorio autorizado.

## 1. Catálogo inicial

| Herramienta | Uso principal | Ejemplo de aplicación | Precaución |
|---|---|---|---|
| Wireshark | Análisis de tráfico de red | Inspeccionar protocolos en una captura propia | Las capturas pueden contener datos sensibles |
| tcpdump | Captura de paquetes desde terminal | Registrar tráfico de una interfaz autorizada | Definir interfaz, filtros y duración |
| Nmap | Descubrimiento y auditoría de servicios | Inventariar equipos de un laboratorio propio | Escanear solo rangos autorizados |
| OWASP ZAP | Pruebas de seguridad de aplicaciones web | Analizar una aplicación de laboratorio | No ejecutar pruebas activas contra terceros |
| OpenVAS / Greenbone | Evaluación de vulnerabilidades | Revisar activos autorizados | Validar falsos positivos y ventana de escaneo |
| Suricata | IDS/IPS y análisis de tráfico | Detectar patrones conocidos | Ajustar reglas y validar alertas |
| Wazuh | Monitoreo de endpoints y eventos | Centralizar registros de máquinas de laboratorio | Proteger la consola y los agentes |
| Linux (grep, awk, journalctl) | Análisis de registros | Buscar eventos y patrones | Preservar integridad y contexto de logs |

## 2. Criterios para seleccionar una herramienta
1. Objetivo: qué pregunta de seguridad debe responder.
2. Alcance: qué sistemas y datos analizará.
3. Compatibilidad: sistema operativo, versiones y dependencias.
4. Evidencia: qué resultados exporta y cómo se reproducen.
5. Riesgo operativo: carga, falsos positivos y posibilidad de interrupción.
6. Licencia y mantenimiento: soporte, actualizaciones y comunidad.

## 3. Flujo de laboratorio seguro
1. Crear una máquina virtual o entorno aislado.
2. Utilizar aplicaciones intencionalmente vulnerables diseñadas para formación.
3. Configurar red host-only o una red privada sin exposición pública.
4. Tomar una instantánea antes de cada práctica.
5. Ejecutar una sola actividad con alcance definido.
6. Guardar resultados sanitizados y documentar versiones.
7. Restaurar el entorno al finalizar.

## 4. Registro de ejecución
| Campo | Valor a completar |
|---|---|
| Herramienta y versión | Pendiente |
| Sistema operativo | Pendiente |
| Objetivo de laboratorio | Pendiente |
| Autorización y alcance | Laboratorio propio |
| Fecha y duración | Pendiente |
| Resultado observado | Pendiente de ejecución |
| Limitaciones/falsos positivos | Pendiente |

## 5. Ejercicio propuesto
**Objetivo:** identificar servicios de una máquina virtual propia.

- Preparar una VM de laboratorio y confirmar su dirección IP privada.
- Verificar conectividad.
- Ejecutar el inventario de servicios únicamente contra esa VM.
- Registrar comando, versión, fecha y resultado.
- Explicar qué servicios deberían estar expuestos y por qué.
- No escanear redes públicas ni dispositivos ajenos.

Los resultados deben añadirse después de ejecutar la práctica; este documento no afirma que el escaneo ya se haya realizado.

## 6. Conclusión preliminar
Una herramienta no reemplaza el criterio del analista. La selección depende del objetivo, el alcance autorizado, la calidad de los datos y la interpretación de resultados.

## 7. Referencias
- Wireshark Documentation. https://www.wireshark.org/docs/
- Nmap Reference Guide. https://nmap.org/book/man.html
- OWASP ZAP Documentation. https://www.zaproxy.org/docs/
- Greenbone Documentation. https://greenbone.github.io/docs/
- Suricata Documentation. https://docs.suricata.io/
- Wazuh Documentation. https://documentation.wazuh.com/

## 8. Pendiente para completar
- [ ] Registrar las versiones realmente instaladas.
- [ ] Adjuntar captura sanitizada del laboratorio.
- [ ] Documentar un ejercicio reproducible y sus resultados.
