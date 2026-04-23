#include <iostream>

void recurse(int depth) {
    if (depth % 1000 == 0) {
        std::cout << "\r[+] Profundidad: " << depth;
        std::flush(std::cout);
    }
    
    // Sin límite artificial para ver dónde truena el sistema (Vector-X puro)
    char padding[16]; 
    recurse(depth + 1);
}

int main() {
    std::cout << "[*] Iniciando prueba de estrés de pila hasta el fallo..." << std::endl;
    recurse(0);
    return 0;
}
