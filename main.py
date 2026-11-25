# Programa de saludo - Laboratorio Tema 1
# Experiencia: Gestionando proyectos colaborativos con Git y GitHub

def main():
    """Solicita el nombre del usuario y muestra un saludo."""
    nombre = input("Ingresa tu nombre: ").strip()

    if nombre:
        print(f"¡Hola, {nombre}! Bienvenido al laboratorio de Git y GitHub.")
    else:
        print("¡Hola! Bienvenido al laboratorio de Git y GitHub.")


if __name__ == "__main__":
    main()
