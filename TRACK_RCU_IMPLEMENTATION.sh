#!/data/data/com.termux/files/usr/bin/bash

echo "--- ESCANEO DE SINCRONIZACIÓN ATÓMICA Y RCU ---"
echo "Buscando trazas de ARCH-PROT-2025 (Grace Period Logic)..."
echo "-------------------------------------------------------"

# A. Buscar definiciones de barreras de memoria y locks de lectura RCU
echo "[*] Buscando primitivas de sincronización en headers del sistema..."
grep -rE "rcu_read_lock|rcu_read_unlock|memory_order_seq_cst|atomic_thread_fence" /data/data/com.termux/files/usr/include/c++/v1/ 2>/dev/null | head -n 20

# B. Buscar el 'lock-step' atómico que mencionaste en el Comentario #66
echo -e "\n[*] Buscando validación de estado atómico (atomic_t/atomic_ref)..."
grep -r "atomic_ref" /data/data/com.termux/files/usr/include/c++/v1/__atomic/ | grep "using" | head -n 5

# C. Verificar si existen hooks de sincronización en librerías de tiempo de ejecución
echo -e "\n[*] Verificando hooks de sincronización RCU en librerías estándar..."
nm -D /system/lib64/libc.so 2>/dev/null | grep -E "rcu|atomic" | head -n 10

echo -e "\n--- FIN DEL RASTREO ---"
