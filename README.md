# Laboratorio Tema 1: Control de versiones y estructuras fundamentales

**Curso:** Fundamentos de Programación  
**Experiencia:** Gestionando proyectos colaborativos con Git y GitHub

## Descripción
Este repositorio contiene el desarrollo de la experiencia de laboratorio sobre control de versiones con Git y GitHub. Se trabaja con un repositorio remoto, una rama de funcionalidad y una solicitud de incorporación (Pull Request).

## Estructura
- `README.md`: documentación y comandos del laboratorio.
- `main.py`: programa sencillo que solicita un nombre y muestra un saludo.

## Parte 1. Instalación y configuración local
Instalar Git desde https://git-scm.com y configurar la identidad en la terminal:

```bash
git config --global user.name "Tu Nombre y Apellidos"
git config --global user.email "tu-correo@example.com"
git --version
git config --list
```

Reemplazar los valores de ejemplo por el nombre y correo asociados a la cuenta de GitHub.

## Parte 2. Repositorio local y primer commit
La guía indica crear una carpeta, inicializar Git, crear un README, agregarlo y confirmar el primer commit:

```bash
mkdir Laboratorio-Tema1-Git-GitHub
cd Laboratorio-Tema1-Git-GitHub
git init
echo "# Mi Proyecto" > README.md
git add README.md
git commit -m "Primer commit"
git status
git log --oneline
```

## Parte 3. Repositorio remoto
Repositorio remoto utilizado en esta experiencia:

https://github.com/limayung98-ux/limayung98-ux-Laboratorio-Tema1-Git-GitHub

Para vincular una copia local del proyecto y sincronizarla:

```bash
git remote add origin https://github.com/limayung98-ux/limayung98-ux-Laboratorio-Tema1-Git-GitHub.git
git branch -M main
git push -u origin main
git pull origin main
```

> Este repositorio remoto fue creado con un README inicial. Si se clona el repositorio, no se debe volver a ejecutar `git init` ni crear un README duplicado.

## Parte 4. Ramas y colaboración
La rama `funcionalidad` contiene el archivo `main.py`. El archivo solicita el nombre y muestra un saludo.

Para reproducir el flujo desde una copia local:

```bash
git switch -c funcionalidad
git add main.py
git commit -m "Agregar saludo"
git push -u origin funcionalidad
```

Luego, en GitHub, abrir un Pull Request desde `funcionalidad` hacia `main`, revisar los cambios y confirmar el merge.

## Ejecución del programa
Requiere Python 3:

```bash
python main.py
```

## Comandos útiles de verificación
```bash
git status
git branch
git log --oneline --graph --all
git remote -v
```
