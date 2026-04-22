#include <iostream>
#include <vector>

// Simulación de la estructura vulnerable de Mojo
struct FuzzUnion_Data {
    FuzzUnion_Data* nested;
};

// Función de validación recursiva (Simulando MessageFragmentArrayTraits::Validate)
bool SimulateMojoValidate(FuzzUnion_Data* data, int depth) {
    // Sin la mitigación ClaimRecursion(), esto seguirá hasta colapsar la pila
    if (!data) return true;
    
    // Log de profundidad para ver el avance en el ZTE v30
    if (depth % 1000 == 0) {
        std::cout << "[*] Validating depth: " << depth << std::endl;
    }

    return SimulateMojoValidate(data->nested, depth + 1);
}

int main() {
    std::cout << "[!] Starting Mojo Stack Overflow PoC (Issue 478015615)" << std::endl;
    
    // Creamos una estructura profundamente anidada
    FuzzUnion_Data* root = new FuzzUnion_Data();
    FuzzUnion_Data* current = root;
    
    for(int i = 0; i < 1000000; ++i) { // 100k niveles de profundidad
        current->nested = new FuzzUnion_Data();
        current = current->nested;
    }
    current->nested = nullptr;

    std::cout << "[+] Deep structure created. Triggering validation..." << std::endl;
    
    // Esto causará el Segmentation Fault (Stack Overflow)
    SimulateMojoValidate(root, 0);

    return 0;
}
