#!/usr/bin/env python3
"""Resume eventos de autenticación de un CSV sintético.

Uso: python3 analizar_auth_logs.py auth_logs.csv
No procesa telemetría real ni bloquea direcciones IP.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

REQUIRED = {"timestamp", "username", "source_ip", "event"}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python3 analizar_auth_logs.py <archivo.csv>")
    path = Path(sys.argv[1])
    if not path.is_file():
        raise SystemExit(f"No se encuentra el archivo: {path}")

    by_event = Counter()
    failed_by_ip = Counter()
    failed_by_user = Counter()
    total = 0
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED.issubset(reader.fieldnames):
            raise SystemExit(f"El CSV debe incluir estas columnas: {', '.join(sorted(REQUIRED))}")
        for row in reader:
            total += 1
            event = (row.get("event") or "UNKNOWN").strip().upper()
            ip = (row.get("source_ip") or "UNKNOWN").strip()
            user = (row.get("username") or "UNKNOWN").strip()
            by_event[event] += 1
            if event == "LOGIN_FAILED":
                failed_by_ip[ip] += 1
                failed_by_user[user] += 1

    print(f"Eventos analizados: {total}")
    print("Eventos por tipo:")
    for event, count in by_event.most_common():
        print(f"  {event}: {count}")
    print("Fallos por IP:")
    for ip, count in failed_by_ip.most_common():
        print(f"  {ip}: {count}")
    print("Fallos por usuario:")
    for user, count in failed_by_user.most_common():
        print(f"  {user}: {count}")
    print("\nNota: los conteos son indicadores para revisión, no prueba concluyente de ataque.")


if __name__ == "__main__":
    main()
