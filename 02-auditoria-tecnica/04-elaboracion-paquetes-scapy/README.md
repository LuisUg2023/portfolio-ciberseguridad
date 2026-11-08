# Práctica: elaboración de paquetes con Scapy

**Ruta:** Módulo 2 – Auditoría técnica  
**Actividad:** 04 – Elaboración de paquetes con Scapy  
**Origen:** Cisco NetAcad, *Práctica de laboratorio – Elaboración de paquetes con Scapy*  
**Tipo:** laboratorio controlado de análisis y elaboración de paquetes  
**Estado de ejecución:** documentación preparada; evidencias reales pendientes de ejecutar en Kali Linux.

## 1. Objetivos

- Investigar las capacidades de Scapy.
- Capturar y examinar tráfico de red.
- Construir y enviar un paquete ICMP personalizado.
- Construir y enviar un paquete TCP SYN y analizar la respuesta del host.

## 2. Alcance y autorización

La guía original utiliza una máquina Kali Linux y un host de laboratorio con dirección **10.6.6.23**, conectado a la red virtual **10.6.6.0/24**. La interfaz indicada en el laboratorio es `br-internal`, asociada a **10.6.6.1**.

Ejecuta las pruebas únicamente en la red virtual del laboratorio, contra máquinas propias o con autorización expresa. Antes de enviar paquetes, verifica que la interfaz y el host de destino pertenecen a tu entorno autorizado. No sustituyas la IP por direcciones públicas ni utilices suplantación de origen, inundación de paquetes o técnicas de denegación de servicio.

> **Integridad de evidencias:** este repositorio no incluye capturas simuladas ni resultados atribuidos a una ejecución no realizada. Las capturas y conclusiones observadas se incorporarán después de ejecutar los pasos en Kali.

## 3. Entorno de laboratorio

| Elemento | Valor indicado por Cisco |
|---|---|
| Sistema de trabajo | Kali Linux personalizado para Ethical Hacker |
| Herramienta | Scapy (Python) |
| Red virtual | 10.6.6.0/24 |
| IP de la interfaz interna | 10.6.6.1 |
| Interfaz indicada | `br-internal` |
| Host objetivo del laboratorio | 10.6.6.23 |
| Puerto TCP evaluado | 445 |
| Analizador PCAP | Wireshark |

Los valores anteriores describen el escenario del material de Cisco; deben verificarse en la VM antes de ejecutar la práctica.

## 4. Preparación y verificación

Ejecuta en una terminal de Kali:

```bash
ip -br address
```
Muestra las interfaces y sus direcciones IP en formato breve; permite comprobar si existe `br-internal` y si tiene asignada la dirección esperada.

```bash
ip route
```
Muestra las rutas de red disponibles y ayuda a confirmar por dónde se alcanzaría el segmento de laboratorio.

```bash
ip route get 10.6.6.23
```
Consulta la ruta que el sistema utilizaría para llegar al host objetivo; revisa que corresponda a la red virtual autorizada.

```bash
ping -c 3 10.6.6.23
```
Envía tres solicitudes ICMP de prueba al host del laboratorio para comprobar conectividad básica; la ausencia de respuesta no demuestra por sí sola que el host esté apagado, porque ICMP puede estar filtrado.

Si la interfaz, la ruta o el objetivo no coinciden con el entorno, detente y corrige la configuración de la VM antes de continuar. No inventes ni sustituyas resultados.

## 5. Parte 1 – Investigar la herramienta Scapy

### 5.1 Documentación

Consulta la introducción oficial: [Scapy – Introduction](https://scapy.readthedocs.io/en/latest/introduction.html).

Scapy es una herramienta basada en Python para construir, enviar, capturar, diseccionar y manipular paquetes de red. Puede utilizarse de forma interactiva o desde scripts Python.

### 5.2 Iniciar Scapy

```bash
sudo -i
```
Abre una sesión de shell con privilegios administrativos, necesarios para varias operaciones de captura y transmisión de paquetes.

```bash
scapy
```
Inicia el intérprete interactivo de Scapy; los comandos siguientes se introducen en el indicador `>>>`.

```python
ls()
```
Enumera las capas y protocolos disponibles en la instalación. Para localizar los formatos TFTP, revisa la salida de la lista y cuenta los formatos mostrados bajo esa capa; registra el número observado en tu versión, no lo deduzcas de otra instalación.

### 5.3 Encabezado IPv4

El encabezado IPv4 contiene, entre otros, versión, longitud de encabezado, DSCP/ECN, longitud total, identificación, indicadores de fragmentación, TTL, protocolo, checksum, dirección de origen y dirección de destino. Los campos permiten que los equipos procesen y enruten el datagrama.

Valores comunes del campo protocolo IPv4:
- ICMP: 1
- TCP: 6
- UDP: 17

**Pregunta de la práctica:** ¿Qué campo se puede modificar para que un paquete parezca originarse en otra máquina?  
**Respuesta:** el campo de dirección IPv4 de origen (`src`). Esta capacidad debe estudiarse conceptualmente; no se utilizará para suplantar equipos en esta práctica.

## 6. Parte 2 – Usar Scapy para rastrear tráfico

### 6.1 Captura en la interfaz predeterminada

En el intérprete Scapy:

```python
sniff()
```
Inicia la captura en la interfaz predeterminada. Mientras captura, abre otra terminal y genera tráfico limitado:

```bash
ping -c 5 www.cisco.com
```
Envía cinco solicitudes ICMP al nombre indicado por Cisco. Regresa a Scapy y detén la captura con **Ctrl+C**.

```python
a = _
a.summary()
```
Guarda en `a` el resultado de la última operación y muestra un resumen de los paquetes capturados. El volumen y los protocolos dependerán del tráfico real presente en el equipo.

### 6.2 Captura en la interfaz interna

Verifica primero la interfaz con `ip -br address`. Si el laboratorio confirma que la interfaz es `br-internal`, ejecuta en Scapy:

```python
sniff(iface="br-internal")
```
Captura el tráfico que atraviesa la interfaz interna. Desde otra terminal, abre el servicio web del host de laboratorio:

```bash
curl -I --max-time 5 http://10.6.6.23/
```
Realiza una solicitud HTTP de cabeceras con tiempo límite; úsala como alternativa reproducible a abrir Firefox. Si el servicio está disponible, detén la captura con **Ctrl+C** y consulta:

```python
a = _
a.summary()
```
Muestra el resumen de los paquetes obtenidos.

### 6.3 Filtrar diez paquetes ICMP

En Scapy, ejecuta:

```python
sniff(iface="br-internal", filter="icmp", count=10)
```
Captura un máximo de diez paquetes ICMP en la interfaz interna. En otra terminal:

```bash
ping -c 5 10.6.6.23
```
Genera hasta cinco solicitudes de eco; si el host responde, se podrán observar solicitudes y respuestas. La captura finalizará al alcanzar diez paquetes o puede requerir detenerse manualmente si no se generan suficientes.

```python
a = _
a.nsummary()
```
Muestra los paquetes capturados numerados para facilitar su inspección.

**Pregunta: ¿Qué tráfico se muestra en el resultado de nsummary()?**  
**Respuesta esperada según el escenario de Cisco:** solicitudes de eco ICMP y respuestas de eco ICMP. El resultado real puede variar si el host no responde o si hay filtrado.

### 6.4 Inspeccionar un paquete

```python
a[2].show()
```
Muestra los campos del tercer paquete capturado (índice Python 2). Comprueba que el índice exista antes de consultarlo.

**Pregunta: ¿Por qué aparecen dos conjuntos de campos de origen y destino?**  
**Respuesta:** porque se muestran direcciones de distintas capas. La capa de enlace puede presentar direcciones MAC de origen y destino, mientras que la capa de red IPv4 presenta direcciones IP de origen y destino.

### 6.5 Guardar la captura en PCAP

```python
wrpcap("capture1.pcap", a)
```
Escribe los paquetes contenidos en `a` en un archivo PCAP que puede abrirse con Wireshark.

En otra terminal, verifica el archivo:

```bash
ls -lh capture1.pcap
```
Lista el archivo y muestra su tamaño. Ábrelo con Wireshark y revisa las columnas de protocolo, origen, destino e información.

## 7. Parte 3 – Crear y enviar un paquete ICMP

En una primera terminal Scapy, inicia la captura interna:

```python
sniff(iface="br-internal")
```
Mantén la captura activa. En una segunda terminal, abre Scapy con privilegios administrativos y envía el paquete definido por Cisco:

```bash
sudo -i
```
Abre una shell administrativa para ejecutar la transmisión.

```bash
scapy
```
Inicia una segunda instancia del intérprete Scapy.

```python
send(IP(dst="10.6.6.23")/ICMP()/"This is a test")
```
Construye un paquete IPv4 dirigido al host de laboratorio, agrega una cabecera ICMP y adjunta la carga útil de texto `This is a test`; después transmite un paquete.

Regresa a la primera terminal, detén la captura con **Ctrl+C** y examina:

```python
a = _
a.nsummary()
```
Guarda la captura y muestra un resumen numerado de los paquetes recibidos.

Consulta los índices que existan para comparar la solicitud y la respuesta:

```python
a[0].show()
```
Muestra los campos del primer paquete capturado; repite con el índice que corresponda al paquete que deseas analizar.

**Pregunta: ¿Qué tipos de paquetes aparecen en el resumen?**  
**Respuesta esperada:** pueden aparecer solicitud de eco, respuesta de eco y mensajes ARP asociados a la resolución de direcciones. La composición exacta depende de la captura.

**Pregunta: ¿Qué diferencia existe entre el intercambio ICMP original y el personalizado?**  
**Respuesta:** la carga útil del paquete personalizado contiene el texto `This is a test`, mientras que el ping convencional utiliza su propia carga de datos.

## 8. Parte 4 – Crear y enviar un paquete TCP SYN

Inicia la captura en la terminal Scapy que utiliza la interfaz interna:

```python
sniff(iface="br-internal")
```
Mantiene la captura activa mientras se envía el paquete desde una segunda terminal Scapy.

```python
send(IP(dst="10.6.6.23")/TCP(dport=445, flags="S"))
```
Construye un paquete IPv4 hacia el host de laboratorio con destino TCP 445 y el indicador SYN activado; transmite un paquete.

Detén la captura con **Ctrl+C** y examina el resumen:

```python
a = _
a.nsummary()
```
Almacena la captura y muestra los paquetes numerados.

Inspecciona el paquete de respuesta que corresponda al host objetivo:

```python
a[1].show()
```
El índice es un ejemplo; identifica primero en `a.nsummary()` cuál paquete proviene del objetivo y utiliza su índice real.

### Interpretación de respuestas TCP

| Respuesta observada | Interpretación habitual |
|---|---|
| SYN-ACK (`SA`) | El puerto está abierto y acepta el inicio de conexión. |
| RST o RST-ACK (`R` / `RA`) | El puerto está cerrado o rechaza la conexión. |
| Sin respuesta | Resultado inconcluso: puede existir filtrado, pérdida o falta de conectividad. |

**Pregunta: ¿Qué indica el indicador SA en el paquete devuelto desde 10.6.6.23?**  
**Respuesta:** SYN-ACK. En el escenario de la práctica, indica que el puerto TCP 445 está abierto y respondió al SYN inicial.

## 9. Preguntas de reflexión

### 9.1 ¿Cómo se pueden utilizar varios paquetes TCP SYN para realizar reconocimiento de puertos?

En una evaluación autorizada, se pueden enviar solicitudes SYN controladas a puertos específicos y analizar las respuestas. SYN-ACK suele indicar un puerto abierto; RST/RST-ACK suele indicar un puerto cerrado; la ausencia de respuesta no permite concluir por sí sola que esté cerrado. La técnica permite identificar servicios potencialmente disponibles sin completar necesariamente el establecimiento TCP.

### 9.2 ¿Cómo podría una solicitud ICMP con dirección de origen falsificada contribuir a una denegación de servicio?

Si se envían solicitudes ICMP con una dirección de origen falsificada que pertenece a la víctima, las respuestas pueden dirigirse a esa víctima. Cuando múltiples sistemas participan o se amplifica el volumen de tráfico, el resultado puede contribuir a una denegación de servicio distribuida. Esta explicación es conceptual: la práctica no ejecuta suplantación de origen ni ataques DoS/DDoS.

## 10. Evidencias que deben recopilarse

Guarda las capturas reales en la carpeta `evidencias/` con nombres descriptivos:

| Nombre sugerido | Evidencia |
|---|---|
| `01-entorno-interfaces.png` | Interfaces e IP de Kali |
| `02-scapy-inicio-ls.png` | Inicio de Scapy y salida de `ls()` |
| `03-sniff-interfaz-default.png` | Captura en interfaz predeterminada |
| `04-sniff-br-internal.png` | Captura de tráfico interno |
| `05-filtro-icmp-nsummary.png` | Diez paquetes ICMP numerados |
| `06-detalle-paquete-icmp.png` | Campos del paquete ICMP |
| `07-wireshark-pcap.png` | PCAP abierto en Wireshark |
| `08-icmp-personalizado.png` | Envío y captura de carga útil personalizada |
| `09-tcp-syn-445.png` | Envío del SYN y respuesta observada |

No incluyas direcciones públicas, datos personales, credenciales ni información ajena al laboratorio. No agregues capturas de ejemplo como si fueran resultados propios.

## 11. Criterios de validación

- [ ] Se identificó la interfaz y se verificó el segmento autorizado.
- [ ] Scapy inició correctamente y se revisaron sus protocolos.
- [ ] Se realizó una captura y se consultó su resumen.
- [ ] Se filtró tráfico ICMP y se inspeccionó un paquete.
- [ ] Se exportó y abrió un archivo PCAP.
- [ ] Se envió el paquete ICMP personalizado y se examinó la captura.
- [ ] Se envió el paquete TCP SYN al puerto 445 y se interpretó la respuesta real.
- [ ] Se guardaron las capturas de pantalla y se redactaron conclusiones basadas en observaciones.

## 12. Conclusión

Scapy permite construir, transmitir, capturar y analizar paquetes de distintos protocolos desde Python. La práctica relaciona la estructura de IPv4, el comportamiento de ICMP y el establecimiento inicial de TCP con tareas de reconocimiento técnico. La conclusión definitiva sobre conectividad, contenido de paquetes y estado del puerto debe redactarse después de ejecutar el laboratorio y revisar las evidencias obtenidas.

## 13. Referencias

- Cisco NetAcad. *Práctica de laboratorio – Elaboración de paquetes con Scapy*. Material proporcionado para esta actividad.
- [Documentación oficial de Scapy – Introduction](https://scapy.readthedocs.io/en/latest/introduction.html).
- [IANA – ICMP Parameters](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml).
