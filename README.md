# ✍️ Auto Typer

¿Tu organización bloqueó la función de copiar/pegar en Teams? 🤦‍♂️ Este proyecto nació de esa frustración.

Una aplicación simple para escribir texto automáticamente en cualquier ventana. Especialmente útil cuando no puedes pegar texto en Teams, formularios web, o cualquier aplicación que bloquee el pegado.

## 🚀 Descarga Rápida

**Ejecutable listo para usar:** [`dist/AutoTyper.exe`](dist/AutoTyper.exe)

No necesitas instalar nada. Solo descarga, ejecuta y listo.

---

## ⚙️ Características

- 🎨 **Interfaz moderna** con tema oscuro
- 🚀 **3 velocidades**: Lento, Normal, Rápido
- ⏱️ **Delay ajustable**: Tiempo para cambiar de ventana (1-10 segundos)
- ⬛ **Botón Stop**: Cancela cuando quieras
- 🗑️ **Botón Limpiar**: Borra el texto rápidamente
- 🌍 **Caracteres especiales**: Tildes, ñ, símbolos, etc.
- � **100% local**: No envía nada a internet

---

## 💻 Cómo Usar

### Ejecutable
1. Descarga `AutoTyper.exe` de la carpeta [`dist/`](dist/)
2. Ejecútalo (no necesita instalación)

### Desde código
```bash
git clone https://github.com/DanieelMR/auto-typer.git
cd auto-typer
pip install -r requirements.txt
python auto_typer.py
```

---
 
## 📖 Guía de Uso

1. Abre la aplicación
2. Pega tu texto en el área
3. Selecciona la velocidad (🐢 Lento / ⚡ Normal / 🚀 Rápido)
4. Ajusta el delay (tiempo para cambiar de ventana)
5. Click en "▶ Iniciar"
6. Cambia rápido a la ventana destino (ej: Teams)
7. ¡El texto se escribirá solo!

### 💡 Casos de Uso

- 💬 **Teams/Slack**: Cuando tu organización bloquea copiar/pegar
- 📝 **Formularios web**: Llenar campos repetitivos
- 🎮 **Gaming**: Comandos o texto en juegos
- 🌐 **Sitios restrictivos**: Páginas que no permiten pegar

---

## ⚠️ Notas

- **Windows**: Ejecuta como administrador para mejor funcionamiento con tildes y ñ
- **Saltos de línea**: Usa Shift+Enter para no enviar mensajes en chats
- **Caracteres**: Soporta tildes (á, é, í, ó, ú), ñ, símbolos y más

---

## 🛠️ Desarrollo

**Dependencias:**
```
keyboard==0.13.5
pyautogui==0.9.54
```

**Compilar ejecutable:**
```bash
python -m PyInstaller auto_typer_optimized.spec --clean
```

---

## 🤝 Contribuir

¿Tienes ideas o mejoras? ¡Abre un issue o haz un PR!

## � Licencia

Código abierto. Úsalo, modifícalo y compártelo libremente.

---

**⭐ Si este proyecto te salvó de las restricciones de Teams, dale una estrella!**
