# Actividad 6. Herramientas y lenguajes de programación

**Estado:** En desarrollo  
**Objetivo:** reconocer cómo la programación y las consultas permiten automatizar tareas defensivas y analizar información.

## 1. Lenguajes y tecnologías

| Tecnología | Aplicación en ciberseguridad |
|---|---|
| Python | Automatizar análisis de archivos, logs y tareas repetitivas |
| Bash | Administrar Linux y encadenar utilidades de terminal |
| PowerShell | Automatizar administración y análisis en Windows |
| SQL | Consultar registros y detectar patrones en bases de datos |
| JavaScript | Comprender el comportamiento de aplicaciones web y validar código del lado cliente |
| HTML/CSS | Reconocer estructura y presentación de interfaces web |

## 2. Fundamentos que debe dominarse
- Variables y tipos de datos.
- Condicionales y bucles.
- Funciones y módulos.
- Lectura y escritura de archivos.
- Manejo de excepciones.
- Expresiones regulares.
- Estructuras de datos.
- Consultas y filtros.
- Registro de errores y validación de entradas.

## 3. Ejercicio Python: calcular hashes SHA-256
El siguiente programa calcula la huella SHA-256 de un archivo local para ayudar a verificar su integridad. No modifica el archivo.

```python
from pathlib import Path
import hashlib
import sys

def sha256_file(file_path: Path) -> str:
    digest = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            digest.update(chunk)

    return digest.hexdigest()

def main() -> None:
    if len(sys.argv) != 2:
        print("Uso: python hash_file.py <ruta_archivo>")
        raise SystemExit(1)

    file_path = Path(sys.argv[1])

    if not file_path.is_file():
        print("Error: la ruta no corresponde a un archivo.")
        raise SystemExit(1)

    print(f"Archivo: {file_path.name}")
    print(f"SHA-256: {sha256_file(file_path)}")

if __name__ == "__main__":
    main()
```

**Ejecución en laboratorio:**

```bash
python hash_file.py archivo_demo.txt
```

**Interpretación:** el hash permite comparar si el contenido de un archivo cambió. Una coincidencia no demuestra que el archivo sea seguro; solo indica que los contenidos producen el mismo resumen criptográfico con una probabilidad de colisión extremadamente baja.

## 4. Ejercicio SQL: filtrar eventos
Tabla ficticia `security_events` con campos `event_time`, `event_type`, `username` y `source_ip`.

```sql
SELECT
    username,
    source_ip,
    COUNT(*) AS failed_attempts
FROM security_events
WHERE event_type = 'AUTH_FAIL'
GROUP BY username, source_ip
ORDER BY failed_attempts DESC;
```

**Propósito:** agrupar intentos fallidos por usuario y dirección de origen. En un entorno real se deben definir ventanas de tiempo, normalizar eventos y correlacionar con otros registros antes de concluir que existe un ataque.

## 5. Ejercicio de terminal Linux
Sobre un archivo de registros ficticio:

```bash
grep "AUTH_FAIL" auth.log
grep "AUTH_FAIL" auth.log | wc -l
grep "AUTH_SUCCESS" auth.log
```

- El primer comando filtra eventos de autenticación fallida.
- El segundo cuenta las líneas coincidentes.
- El tercero localiza autenticaciones exitosas.

## 6. Buenas prácticas de programación segura
- Validar entradas y controlar errores.
- No incluir contraseñas, tokens ni claves en el código.
- Evitar ejecutar comandos construidos directamente con datos no confiables.
- Aplicar mínimo privilegio.
- Mantener dependencias actualizadas.
- Probar con datos ficticios y documentar las limitaciones.

## 7. Conclusión preliminar
La programación permite convertir tareas manuales en procedimientos repetibles. Todo script debe tener un objetivo claro, entradas validadas, resultados interpretables y pruebas en un entorno controlado.

## 8. Referencias
- Python Documentation. https://docs.python.org/3/
- PostgreSQL Documentation. https://www.postgresql.org/docs/
- OWASP. *Secure Coding Practices*. https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/

## 9. Pendiente para completar
- [ ] Ejecutar el script con un archivo de prueba propio.
- [ ] Guardar salida de consola y versión de Python utilizada.
- [ ] Probar la consulta SQL en una base de datos de práctica.
- [ ] Añadir un ejercicio breve de Bash o PowerShell.
