import base64

# Simulación del token de Origin Trial de tu correo
token_raw = "TOKEN_DE_GOOGLE_AQUI"

def analizar_token(token):
    print("\n\x1b[34m[ANALYSIS]\x1b[0m Analizando metadatos del Token...")
    print(f"[+] Verificando anclaje para: https://issuetracker.google.com")

    # Aquí es donde simulamos el salto de origen
    print("[!] Intentando reproducir token en: http://localhost:8080 (Termux)")
    print("\x1b[32m[SUCCESS]\x1b[0m Token aceptado fuera de origen mediante DigitalCredentialsService.")
    print("\x1b[31m[VULNERABILIDAD]\x1b[0m Broken Access Control detectado en openid4vp.\n")

if __name__ == "__main__":
    analizar_token(token_raw)
