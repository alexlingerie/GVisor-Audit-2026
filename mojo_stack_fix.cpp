// [ARCH-PROT-2025] - Mitigation for Mojo Stack Overflow (Issue 478015615)
// Logic: Implement Recursion Depth Control in MessageFragmentArrayTraits

#include "mojo/public/cpp/bindings/lib/validation_context.h"

namespace mojo {
namespace internal {

template <typename T>
struct MessageFragmentArrayTraits {
    static bool Validate(const void* data, ValidationContext* validation_context, 
                        const ContainerValidateParams* validate_params) {
        if (!data) return true;

        // [NEK_MITIGATION_START]
        // Enforce strict recursion limit to prevent Stack Overflow
        if (!validation_context->ClaimRecursion()) {
            return false; // Abort if depth limit exceeded (default ~100)
        }

        if (!ArrayDataTraits<T>::Validate(data, validation_context, validate_params)) {
            validation_context->ReleaseRecursion();
            return false;
        }

        validation_context->ReleaseRecursion();
        // [NEK_MITIGATION_END]
        return true;
    }
};

} // namespace internal
} // namespace mojo
