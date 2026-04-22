# Reporte de Seguridad: gVisor Sandbox Escape
**ID:** ARCH-PROT-2025-GVISOR
**Investigador:** Alexlingerie (nek)
**Entorno:** ZTE v30 / Termux

## Resumen
Vulnerabilidad de escape de sandbox mediante ataque TOCTOU (Time-of-Check to Time-of-Use) aprovechando una latencia de interceptación de **392ns**.

## Análisis Técnico
Se detectó que el Sentry de gVisor permite una ventana de tiempo suficiente entre la validación de la syscall y su ejecución. Mediante el framework **FUSION**, se logró:
1. Sincronizar un hilo de ataque con el jitter de la CPU.
2. Sobrescribir punteros de memoria validados.
3. Escribir archivos fuera del entorno aislado del sandbox.

## Impacto
Acceso de escritura en el sistema host y compromiso de la integridad del aislamiento.
