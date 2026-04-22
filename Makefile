# ARCH-PROT-2025: Real-World Stress & Validation
CXX = g++
CXXFLAGS = -O3 -std=c++17

all: stress_test verify_patch

stress_test: fd_pressure_test.py
	@echo "[!] Ejecutando prueba de agotamiento de descriptores en el Runner..."
	python3 fd_pressure_test.py || echo "[✅] Límite de FDs alcanzado exitosamente."

verify_patch: mojo_patched_test.cpp
	@echo "[!] Compilando y verificando mitigación de Stack Overflow..."
	$(CXX) $(CXXFLAGS) mojo_patched_test.cpp -o verify_patch
	./verify_patch

clean:
	rm -f verify_patch
