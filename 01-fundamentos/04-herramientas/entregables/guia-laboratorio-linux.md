# Guía de laboratorio: reconocimiento local y revisión básica

**Entorno:** máquina propia o laboratorio aislado. No ejecutar contra redes ajenas.

## Objetivo
Practicar inventario local, revisión de servicios y lectura de registros sin explotar sistemas.

## Comandos

```bash
# Identidad y sistema
whoami
hostnamectl
uname -a

# Interfaces y rutas
ip address
ip route

# Servicios en escucha (solo observación local)
ss -tulpen

# Procesos
ps aux --sort=-%cpu | head

# Espacio y actualizaciones
 df -h
sudo apt update
apt list --upgradable

# Revisar autenticaciones en Debian/Ubuntu (si existe el archivo)
sudo tail -n 50 /var/log/auth.log
```

## Registro de resultados
| Comando | Hallazgo observado | Riesgo/interpretación | Acción propuesta |
|---|---|---|---|
| `ss -tulpen` | Pendiente | Identificar servicios expuestos localmente | Revisar necesidad y firewall |
| `apt list --upgradable` | Pendiente | Paquetes con actualizaciones | Aplicar proceso de parches |

## Evidencia
Guardar fecha, distribución, versión, comandos y salidas anonimizadas en `evidencias/`. No publicar IP públicas, usuarios, tokens ni datos personales.

**Estado:** guía preparada; ejecución y capturas pendientes.