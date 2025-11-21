# ✍️ Auto Typer

Aplicación con interfaz gráfica moderna para escribir texto automáticamente en cualquier ventana. Ideal para automatizar entrada de texto repetitivo en formularios, chats, documentos, etc.

## 🚀 Descarga Rápida

**¿Solo quieres usar la aplicación?** El ejecutable listo para usar está en la carpeta [`dist/AutoTyper.exe`](dist/AutoTyper.exe). No necesitas instalar Python ni dependencias. Solo descárgalo y ejecútalo.

---

## 📸 Capturas de Pantalla

### Interfaz Principal
Ventana amplia y moderna con tema oscuro profesional.

### Características en Acción
- **Selector de velocidad**: Lento, Normal o Rápido
- **Botón Stop**: Detén el proceso en cualquier momento
- **Botón Limpiar**: Limpia el contenido con un clic

---

## ⚙️ Características

### 🎨 Interfaz Moderna
- Ventana amplia (800x700 píxeles) con diseño profesional
- Tema oscuro elegante y cómodo a la vista
- Área de texto grande con 18 líneas de altura
- Controles intuitivos y bien organizados

### 🚀 Control de Velocidad
- **🐢 Lento**: 0.1s por carácter (ideal para aplicaciones lentas)
- **⚡ Normal**: 0.05s por carácter (velocidad balanceada)
- **🚀 Rápido**: 0.02s por carácter (rápido pero natural)

### 🎯 Funcionalidades
- ⏱️ **Delay configurable**: De 1 a 10 segundos para cambiar de ventana
- ⬛ **Botón Stop**: Cancela el proceso en cualquier momento
- 🗑️ **Botón Limpiar**: Borra el contenido del área de texto
- 🌍 **Soporte completo**: Tildes, ñ, símbolos y caracteres especiales
- 🔄 **Threading**: La interfaz nunca se bloquea
- ↩️ **Saltos de línea**: Usa Shift+Enter para no enviar mensajes

### 🔐 Seguridad y Privacidad
- Todo se ejecuta localmente en tu computadora
- No envía datos a internet
- No requiere permisos especiales (excepto para caracteres especiales en Windows)

---

## 💻 Uso de la Aplicación

### Opción 1: Ejecutable (Recomendado)

1. Descarga `AutoTyper.exe` desde la carpeta [`dist/`](dist/)
2. Ejecuta el archivo (no requiere instalación)
3. Sigue los pasos de uso descritos abajo

### Opción 2: Desde Código Fuente

#### Requisitos
- Python 3.7 o superior

#### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/TU_USUARIO/auto-typer.git
cd auto-typer
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
python auto_typer.py
```

---

## 📖 Guía de Uso

### Pasos Básicos

1. **Abre la aplicación** (ejecutable o script)
2. **Pega o escribe** el texto que deseas escribir automáticamente
3. **Selecciona la velocidad** de escritura:
   - 🐢 Lento: Para aplicaciones que tardan en responder
   - ⚡ Normal: Velocidad balanceada (recomendado)
   - 🚀 Rápido: Máxima velocidad humanizada
4. **Ajusta el delay** (1-10 segundos) - Tiempo para cambiar a la ventana destino
5. **Haz clic en "▶ Iniciar"**
6. **Cambia rápidamente** a la ventana donde quieres escribir
7. El texto se escribirá automáticamente

### Consejos Útiles

✅ **Coloca el cursor** en el campo de texto correcto antes de iniciar
✅ **Usa el delay** suficiente para tener tiempo de cambiar de ventana
✅ **Velocidad Lento** es ideal para aplicaciones web lentas o conexiones lentas
✅ **Botón Stop** te permite cancelar si algo sale mal
✅ **Botón Limpiar** te ayuda a empezar de nuevo rápidamente

### Casos de Uso

- 📝 **Formularios repetitivos**: Rellenar campos largos una y otra vez
- 💬 **Mensajes masivos**: Enviar el mismo texto en múltiples chats
- 📄 **Documentación**: Insertar texto en aplicaciones sin opción de pegar
- 🎮 **Gaming**: Escribir comandos o texto en juegos
- 🌐 **Aplicaciones web**: Sitios que bloquean copiar/pegar

---

## ⚠️ Notas Importantes

### Windows
- Para **mejor funcionamiento con caracteres especiales** (tildes, ñ, etc.), ejecuta como administrador
- Clic derecho en el ejecutable → "Ejecutar como administrador"

### Saltos de Línea
- El programa usa **Shift+Enter** para los saltos de línea
- Esto evita enviar mensajes accidentalmente en chats

### Caracteres Soportados
- ✅ Letras con tildes: á, é, í, ó, ú
- ✅ Caracteres especiales: ñ, ü, ¿, ¡
- ✅ Símbolos: @, #, $, %, &, etc.
- ✅ Emojis y Unicode (dependiendo del sistema)

---

## 🛠️ Desarrollo

### Estructura del Proyecto

```
auto-typer/
│
├── dist/                    # Ejecutable listo para usar
│   └── AutoTyper.exe
│
├── auto_typer.py           # Código fuente principal
├── requirements.txt        # Dependencias de Python
├── auto_typer_optimized.spec  # Configuración de PyInstaller
├── .gitignore             # Archivos ignorados por Git
└── README.md              # Este archivo
```

### Dependencias

```
keyboard==0.13.5
pyautogui==0.9.54
```

### Compilar el Ejecutable

Si quieres generar tu propio ejecutable:

```bash
python -m PyInstaller auto_typer_optimized.spec --clean
```

El ejecutable se generará en la carpeta `dist/`.

---

## 📝 Licencia

Este proyecto es de código abierto. Siéntete libre de usar, modificar y distribuir.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la aplicación:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

---

## 🐛 Reportar Problemas

¿Encontraste un bug o tienes una sugerencia? [Abre un issue](../../issues) en GitHub.

---

## ❓ Preguntas Frecuentes (FAQ)

### ¿Por qué necesito ejecutar como administrador en Windows?
Para que la librería `keyboard` funcione correctamente con caracteres especiales (tildes, ñ, etc.).

### ¿Funciona en todas las aplicaciones?
Sí, funciona en la mayoría de aplicaciones. Sin embargo, algunos juegos con anti-cheat o aplicaciones con seguridad elevada pueden bloquearlo.

### ¿Puedo usar esto para automatizar tareas?
Sí, es ideal para automatizar entrada de texto repetitivo. Pero úsalo de manera responsable y respeta los términos de servicio de las aplicaciones.

### ¿El ejecutable es seguro?
Sí, está compilado directamente desde el código fuente de este repositorio. Puedes compilarlo tú mismo si lo prefieres.

### ¿Por qué usa Shift+Enter en vez de Enter?
Para evitar enviar mensajes accidentalmente en aplicaciones de chat. Los saltos de línea se insertan sin activar el envío.

---

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue o contactarme.

---

**⭐ Si te gustó este proyecto, dale una estrella en GitHub!**
