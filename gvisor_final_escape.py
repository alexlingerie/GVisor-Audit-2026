import os

def culminar_escape():
    print("📡 [ARCH-PROT-2025] Iniciando fase final: Exfiltración y Escritura...")
    
    puntos_vulnerables = []
    
    try:
        with open("/proc/mounts", "r") as f:
            for line in f:
                # Buscamos puntos de montaje que sean 'rw' (Read-Write)
                if " rw," in line and "/dev/block/" in line:
                    parts = line.split()
                    puntos_vulnerables.append(parts[1])
        
        if not puntos_vulnerables:
            print("🛡️ [INFO] No se detectaron particiones RW directas. El sistema está endurecido.")
            return

        print(f"🔓 [ALERTA] Se detectaron {len(puntos_vulnerables)} puntos RW. Probando persistencia...")
        
        for punto in puntos_vulnerables:
            test_file = os.path.join(punto, "fusion_breach.txt")
            try:
                with open(test_file, "w") as f:
                    f.write("ESCAPE_SUCCESSFUL: ARCH-PROT-2025")
                print(f"🚀 [SUCCESS] ¡Escritura confirmada en {punto}! Sandbox vulnerado.")
                # Limpiamos rastro
                os.remove(test_file)
                break
            except:
                print(f"🔒 [BLOCK] Escritura denegada en {punto} (Probable restricción de usuario).")

    except Exception as e:
        print(f"❌ [ERROR] Fallo en la fase de culminación: {e}")

print("🔥 Ejecutando secuencia de culminación en ZTE...")
culminar_escape()
