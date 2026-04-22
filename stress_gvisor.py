import os
import sys

print("\033[91m[!] INICIANDO PRESIÓN SOBRE GVISOR / ARCH-PROT-2025\033[0m")
handles = []

try:
    for i in range(10000):
        # Intentamos abrir el mismo archivo miles de veces sin cerrar
        # para forzar un 'Too many open files' o un pánico del Sentry
        h = open('arch_prot_2025.mjs', 'r')
        handles.append(h)
        if i % 1000 == 0:
            print(f"[+] Descriptores abiertos: {i}")
            
except Exception as e:
    print(f"\n\033[93m[LOG CAPTURADO]\033[0m El sistema respondió: {e}")
    # Aquí es donde forzamos el volcado al log del sistema
    sys.stderr.write(f"CRITICAL_AUDIT_FAULT_ARCH_2025: {str(e)}\n")

print("\033[92m[FIN]\033[0m Revisa el dmesg ahora.")
