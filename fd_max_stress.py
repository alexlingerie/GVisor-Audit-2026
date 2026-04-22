import os

def max_stress():
    print(f"🚀 [ATTACK] Apuntando al límite de {os.popen('ulimit -n').read().strip()} FDs...")
    fds = []
    try:
        # Intentamos abrir 33,000 para superar el límite de 32,768
        for i in range(1, 33001):
            fds.append(os.open("/dev/null", os.O_RDONLY))
            if i % 5000 == 0:
                print(f"   [+] Descriptores alcanzados: {i}")
    except OSError as e:
        print(f"\n🛡️ [BLOQUEO] Sistema saturado en {len(fds)} FDs.")
        print(f"🎯 Resultado: {e}")
    finally:
        for fd in fds:
            os.close(fd)

max_stress()
