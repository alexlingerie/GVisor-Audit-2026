import time
import os

def measure_syscall_latency():
    print("📡 [SIDE-CHANNEL] Midiendo latencia de syscalls (getpid)...")
    samples = []
    for _ in range(1000):
        start = time.perf_counter_ns()
        os.getpid() # Syscall ligera
        end = time.perf_counter_ns()
        samples.append(end - start)
    
    avg_latency = sum(samples) / len(samples)
    print(f"📊 Latencia Promedio: {avg_latency:.2f} ns")
    
    # En gVisor, la latencia es significativamente mayor que en Linux nativo
    # debido a la intercepción del Sentry.
    if avg_latency > 500: 
        print("🚨 [ANALYSIS] Latencia alta detectada: Posible intercepción por Sentry.")
    else:
        print("✅ [ANALYSIS] Latencia baja: Ejecución cercana al kernel nativo.")

measure_syscall_latency()
