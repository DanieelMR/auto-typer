# 📦 Guía para Subir el Proyecto a GitHub

## Pasos para crear y subir el repositorio

### 1. Inicializar Git (si no está inicializado)
```bash
git init
```

### 2. Añadir todos los archivos
```bash
git add .
```

### 3. Hacer el primer commit
```bash
git commit -m "Initial commit: Auto Typer v1.0 con interfaz moderna y controles avanzados"
```

### 4. Crear repositorio en GitHub
1. Ve a https://github.com/new
2. Nombre sugerido: `auto-typer`
3. Descripción: "Aplicación moderna para escribir texto automáticamente con control de velocidad y interfaz gráfica"
4. Marca como **Público**
5. **NO** inicialices con README (ya tenemos uno)
6. Click en "Create repository"

### 5. Conectar con el repositorio remoto
Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub:
```bash
git remote add origin https://github.com/TU_USUARIO/auto-typer.git
```

### 6. Subir los archivos
```bash
git branch -M main
git push -u origin main
```

### 7. Verificar que el ejecutable esté incluido
GitHub puede tener límites para archivos grandes. Si el ejecutable es muy grande:
- Verifica el tamaño del archivo en `dist/AutoTyper.exe`
- GitHub acepta archivos hasta 100MB (warning a partir de 50MB)
- Si es mayor, considera usar GitHub Releases para subirlo

---

## Estructura de archivos que se subirán

✅ **Archivos incluidos:**
- `auto_typer.py` - Código fuente
- `requirements.txt` - Dependencias
- `auto_typer_optimized.spec` - Configuración de PyInstaller
- `dist/AutoTyper.exe` - Ejecutable listo para usar
- `README.md` - Documentación completa
- `.gitignore` - Archivos excluidos
- Scripts de build (`.bat`)

❌ **Archivos excluidos (por .gitignore):**
- `build/` - Archivos temporales de compilación
- `__pycache__/` - Archivos de caché de Python
- Archivos del IDE y sistema operativo

---

## Comandos útiles adicionales

### Ver estado de los archivos
```bash
git status
```

### Ver historial de commits
```bash
git log --oneline
```

### Actualizar después de cambios
```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

---

## 🎉 ¡Listo!

Una vez subido, tu repositorio estará en:
`https://github.com/TU_USUARIO/auto-typer`

Comparte el link para que otros puedan descargarlo y usarlo.
