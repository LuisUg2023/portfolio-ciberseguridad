# Actividad 2. Ética y uso responsable de la ciberseguridad

**Estado:** En desarrollo  
**Escenario:** laboratorio académico y organización ficticia.

## 1. Objetivo
Establecer límites éticos y operativos para realizar actividades de ciberseguridad respetando la autorización, la privacidad, la integridad de los sistemas y la confidencialidad de la información.

## 2. Principios de actuación
1. **Autorización previa:** no escanear, acceder, modificar ni probar sistemas sin permiso explícito del propietario.
2. **Alcance definido:** documentar sistemas, direcciones, fechas, técnicas permitidas y exclusiones.
3. **Minimización:** acceder únicamente a la información necesaria para el objetivo autorizado.
4. **No causar daño:** evitar interrupciones, borrado de datos, degradación del servicio o cambios no aprobados.
5. **Confidencialidad:** proteger datos y evidencias durante todo su ciclo de vida.
6. **Transparencia:** registrar métodos, limitaciones, errores y resultados sin exagerarlos.
7. **Divulgación responsable:** comunicar hallazgos al responsable designado y acordar un proceso seguro de corrección.

## 3. Actividades permitidas y límites

| Actividad | Condición |
|---|---|
| Analizar archivos propios o de laboratorio | Permitido dentro del entorno controlado |
| Revisar configuraciones de un equipo propio | Permitido |
| Escanear una red institucional | Requiere autorización escrita y alcance |
| Probar contraseñas de terceros | No realizar sin autorización explícita y procedimiento aprobado |
| Descargar bases de datos reales | No hacerlo salvo necesidad autorizada y controles de privacidad |
| Publicar capturas de incidentes | Sanitizar datos, direcciones, nombres y secretos antes de publicar |

## 4. Lista de verificación previa
- [ ] Identifiqué al propietario del sistema.
- [ ] Tengo autorización documentada.
- [ ] El alcance técnico está delimitado.
- [ ] Conozco las actividades prohibidas.
- [ ] Existe contacto para detener la prueba ante un incidente.
- [ ] Definí cómo proteger y eliminar las evidencias.
- [ ] No utilizaré datos reales si puedo usar datos sintéticos.

## 5. Caso práctico
**Situación:** un estudiante detecta un panel administrativo expuesto durante una práctica.

**Respuesta adecuada:**
1. No intentar iniciar sesión ni evadir controles.
2. Registrar únicamente la información mínima necesaria para describir la exposición.
3. No divulgar públicamente la dirección ni capturas con datos sensibles.
4. Informar al docente o responsable del laboratorio por el canal establecido.
5. Esperar autorización antes de realizar validaciones adicionales.

## 6. Manejo de evidencias
Antes de publicar un archivo, revisar que no contenga:
- Contraseñas, tokens, cookies o claves privadas.
- Nombres, correos, teléfonos o identificadores personales.
- Direcciones IP públicas o nombres internos que deban permanecer reservados.
- Datos de clientes, empleados o instituciones.
- Metadatos que permitan identificar a terceros.

Usar datos ficticios y reemplazar valores sensibles por marcadores como `[REDACTADO]`.

## 7. Conclusión preliminar
La competencia técnica debe estar acompañada de autorización, proporcionalidad y responsabilidad. Una vulnerabilidad no constituye permiso para acceder al sistema ni para demostrar su explotación.

## 8. Referencias
- NIST. *Computer Security Resource Center — Glossary*. https://csrc.nist.gov/glossary
- OWASP. *Web Security Testing Guide*. https://owasp.org/www-project-web-security-testing-guide/
- Electronic Frontier Foundation. *Surveillance Self-Defense*. https://ssd.eff.org/

## 9. Pendiente para completar
- [ ] Incorporar el código de conducta indicado por el curso, si aplica.
- [ ] Añadir reflexión personal sobre un dilema ético.
- [ ] Revisar la lista de evidencias antes de publicar capturas.
