#include <iostream>

// --- SIMULACIÓN DEL PARCHE DE NEK (ARCH-PROT-2025) ---
class ValidationContext {
private:
    int depth = 0;
    const int max_depth = 100; // El límite que recomendaste
public:
    bool ClaimRecursion() {
        if (depth >= max_depth) return false;
        depth++;
        return true;
    }
    void ReleaseRecursion() {
        if (depth > 0) depth--;
    }
};

struct FuzzUnion_Data {
    FuzzUnion_Data* nested;
};

// Función de validación con el parche aplicado
bool PatchedMojoValidate(FuzzUnion_Data* data, ValidationContext* ctx) {
    if (!data) return true;

    // IMPLEMENTACIÓN DE TU PARCHE
    if (!ctx->ClaimRecursion()) {
        std::cerr << "[!] SEGURIDAD: Límite de recursión alcanzado. Abortando validación profunda." << std::endl;
        return false; 
    }

    bool result = PatchedMojoValidate(data->nested, ctx);

    ctx->ReleaseRecursion();
    return result;
}

int main() {
    std::cout << "[*] Iniciando prueba con PARCHE IMPLEMENTADO..." << std::endl;
    
    // Crear la misma estructura de 1 millón de niveles que causó el crash
    FuzzUnion_Data* root = new FuzzUnion_Data();
    FuzzUnion_Data* current = root;
    for(int i = 0; i < 1000000; ++i) {
        current->nested = new FuzzUnion_Data();
        current = current->nested;
    }
    current->nested = nullptr;

    ValidationContext ctx;
    
    if (PatchedMojoValidate(root, &ctx)) {
        std::cout << "[+] Validación exitosa." << std::endl;
    } else {
        std::cout << "[-] Validación rechazada por política de seguridad (Deep Nesting)." << std::endl;
    }

    return 0;
}
