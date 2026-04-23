import os
import sys
import time

def demonstrate_fd_exhaustion():
    fds = []
    # En Android/Termux el límite suele ser 1024 o 32768 según el kernel
    limit = 40000  
    print("--- [ARCH-PROT-2025] Iniciando Stress Test de Descriptores ---")
    
    try:
        for i in range(limit):
            fd = os.open('/dev/null', os.O_RDONLY)
            fds.append(fd)
            if i % 1000 == 0:
                print(f"Descriptores consumidos: {i}")
    except OSError as e:
        print(f"\n[!] COLAPSO DE SISTEMA DETECTADO: {e}")
        print(f"Límite alcanzado en: {len(fds)}")
        print("[ALERTA] El validador de Mojo/IAP ha quedado CIEGO.")
        # Mantenemos el estado de ceguera por 10 segundos para la captura
        time.sleep(10)
        sys.exit(1)

if __name__ == "__main__":
    demonstrate_fd_exhaustion()
