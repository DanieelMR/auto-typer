import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard
import time
import threading

class AutoTyperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typer")
        self.root.geometry("800x700")
        self.root.resizable(False, False)
        
        # Variable de control para detener
        self.stop_flag = False
        
        # Configurar colores y estilo moderno
        self.bg_color = "#1e1e2e"
        self.fg_color = "#cdd6f4"
        self.accent_color = "#89b4fa"
        self.button_color = "#313244"
        self.button_hover = "#45475a"
        
        self.root.configure(bg=self.bg_color)
        
        # Título
        title_label = tk.Label(
            root,
            text="✍️ Auto Typer",
            font=("Segoe UI", 20, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack(pady=(20, 10))
        
        # Subtítulo
        subtitle_label = tk.Label(
            root,
            text="Pega tu texto y se escribirá automáticamente",
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg=self.fg_color
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Frame contenedor para el área de texto y botón limpiar
        text_container = tk.Frame(root, bg=self.bg_color)
        text_container.pack(padx=50, pady=(0, 15), fill="both", expand=False)
        
        # Frame superior con botón limpiar
        top_frame = tk.Frame(text_container, bg=self.bg_color)
        top_frame.pack(fill="x", pady=(0, 5))
        
        # Botón limpiar (discreto, alineado a la derecha)
        clear_button = tk.Button(
            top_frame,
            text="🗑️ Limpiar",
            command=self.clear_text,
            font=("Segoe UI", 9),
            bg=self.button_color,
            fg=self.fg_color,
            activebackground=self.button_hover,
            activeforeground=self.fg_color,
            relief="flat",
            padx=12,
            pady=4,
            cursor="hand2",
            borderwidth=0
        )
        clear_button.pack(side="right")
        
        # Efecto hover en botón limpiar
        clear_button.bind("<Enter>", lambda e: clear_button.config(bg=self.button_hover))
        clear_button.bind("<Leave>", lambda e: clear_button.config(bg=self.button_color))
        
        # Frame para el área de texto
        text_frame = tk.Frame(text_container, bg=self.bg_color)
        text_frame.pack(fill="both", expand=False)
        
        # Área de texto
        self.text_area = tk.Text(
            text_frame,
            font=("Consolas", 10),
            bg="#11111b",
            fg=self.fg_color,
            insertbackground=self.accent_color,
            relief="flat",
            padx=10,
            pady=10,
            wrap="word",
            borderwidth=2,
            highlightthickness=2,
            highlightbackground=self.button_color,
            highlightcolor=self.accent_color,
            height=18
        )
        self.text_area.pack(side="left", fill="both", expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        # Frame para velocidad
        speed_frame = tk.Frame(root, bg=self.bg_color)
        speed_frame.pack(pady=(0, 15))
        
        # Label de velocidad
        speed_label = tk.Label(
            speed_frame,
            text="Velocidad de escritura:",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg=self.fg_color
        )
        speed_label.pack(pady=(0, 8))
        
        # Variable para velocidad
        self.speed_var = tk.StringVar(value="normal")
        
        # Frame para radio buttons de velocidad
        speed_options_frame = tk.Frame(speed_frame, bg=self.bg_color)
        speed_options_frame.pack()
        
        # Radio buttons para velocidad
        speeds = [("🐢 Lento", "lento"), ("⚡ Normal", "normal"), ("🚀 Rápido", "rapido")]
        for text, value in speeds:
            radio = tk.Radiobutton(
                speed_options_frame,
                text=text,
                variable=self.speed_var,
                value=value,
                font=("Segoe UI", 10),
                bg=self.bg_color,
                fg=self.fg_color,
                selectcolor="#11111b",
                activebackground=self.bg_color,
                activeforeground=self.accent_color,
                cursor="hand2",
                borderwidth=0,
                highlightthickness=0
            )
            radio.pack(side="left", padx=12)
        
        # Frame para controles (delay y botón)
        controls_frame = tk.Frame(root, bg=self.bg_color)
        controls_frame.pack(pady=(0, 20))
        
        # Label de delay
        delay_label = tk.Label(
            controls_frame,
            text="Delay (segundos):",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg=self.fg_color
        )
        delay_label.pack(side="left", padx=(0, 10))
        
        # Spinbox para delay
        self.delay_var = tk.StringVar(value="3")
        delay_spinbox = tk.Spinbox(
            controls_frame,
            from_=1,
            to=10,
            textvariable=self.delay_var,
            width=5,
            font=("Segoe UI", 10),
            bg="#11111b",
            fg=self.fg_color,
            buttonbackground=self.button_color,
            relief="flat",
            borderwidth=2,
            highlightthickness=1,
            highlightbackground=self.button_color
        )
        delay_spinbox.pack(side="left", padx=(0, 20))
        
        # Botón de inicio
        self.start_button = tk.Button(
            controls_frame,
            text="▶ Iniciar",
            command=self.start_typing,
            font=("Segoe UI", 11, "bold"),
            bg=self.accent_color,
            fg="#1e1e2e",
            activebackground="#74c7ec",
            activeforeground="#1e1e2e",
            relief="flat",
            padx=25,
            pady=8,
            cursor="hand2",
            borderwidth=0
        )
        self.start_button.pack(side="left", padx=5)
        
        # Botón de stop (inicialmente oculto)
        self.stop_button = tk.Button(
            controls_frame,
            text="⬛ Detener",
            command=self.stop_typing,
            font=("Segoe UI", 11, "bold"),
            bg="#f38ba8",
            fg="#1e1e2e",
            activebackground="#eba0ac",
            activeforeground="#1e1e2e",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            borderwidth=0,
            state="disabled"
        )
        self.stop_button.pack(side="left", padx=5)
        
        # Label de estado
        self.status_label = tk.Label(
            root,
            text="Listo para escribir",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg=self.fg_color
        )
        self.status_label.pack(pady=(0, 15))
        
        # Efectos hover en botones
        self.start_button.bind("<Enter>", lambda e: self.start_button.config(bg="#74c7ec") if self.start_button['state'] == 'normal' else None)
        self.start_button.bind("<Leave>", lambda e: self.start_button.config(bg=self.accent_color) if self.start_button['state'] == 'normal' else None)
        self.stop_button.bind("<Enter>", lambda e: self.stop_button.config(bg="#eba0ac") if self.stop_button['state'] == 'normal' else None)
        self.stop_button.bind("<Leave>", lambda e: self.stop_button.config(bg="#f38ba8") if self.stop_button['state'] == 'normal' else None)
    
    def clear_text(self):
        """Limpiar el contenido del área de texto"""
        self.text_area.delete("1.0", "end")
        self.status_label.config(text="Texto limpiado", fg=self.fg_color)
    
    def start_typing(self):
        text = self.text_area.get("1.0", "end-1c")
        
        if not text.strip():
            self.status_label.config(text="⚠️ No hay texto para escribir", fg="#f38ba8")
            return
        
        delay = int(self.delay_var.get())
        
        # Reset flag de stop
        self.stop_flag = False
        
        # Deshabilitar botón de inicio y habilitar stop
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        # Iniciar thread para no bloquear la UI
        thread = threading.Thread(target=self.type_text, args=(text, delay))
        thread.daemon = True
        thread.start()
    
    def stop_typing(self):
        """Detener el proceso de escritura"""
        self.stop_flag = True
        self.status_label.config(text="⏹️ Detenido por el usuario", fg="#f38ba8")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
    
    def type_text(self, text, delay):
        # Countdown
        for i in range(delay, 0, -1):
            if self.stop_flag:
                self.start_button.config(state="normal")
                self.stop_button.config(state="disabled")
                return
            
            self.status_label.config(
                text=f"⏱️ Cambia a la ventana destino... {i}s",
                fg="#fab387"
            )
            time.sleep(1)
        
        self.status_label.config(text="✍️ Escribiendo...", fg="#a6e3a1")
        
        # Escribir el texto carácter por carácter
        for char in text:
            # Verificar si se debe detener
            if self.stop_flag:
                self.start_button.config(state="normal")
                self.stop_button.config(state="disabled")
                return
            
            if char == '\n':
                # Presionar Shift+Enter para salto de línea SIN enviar
                keyboard.press_and_release('shift+enter')
            elif char == '\r':
                # Ignorar retorno de carro
                continue
            else:
                # Escribir caracteres normales (incluye espacios y caracteres especiales)
                keyboard.write(char)
            
            # Aplicar velocidad según selección
            speed = self.speed_var.get()
            if speed == "lento":
                time.sleep(0.1)  # Más lento
            elif speed == "normal":
                time.sleep(0.05)  # Velocidad normal
            else:  # rapido
                time.sleep(0.02)  # Más rápido pero humanizado
        
        # Restaurar estado
        self.status_label.config(text="✅ Texto escrito correctamente", fg="#a6e3a1")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        
        # Volver a estado normal después de 3 segundos
        time.sleep(3)
        if not self.stop_flag:
            self.status_label.config(text="Listo para escribir", fg=self.fg_color)


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTyperApp(root)
    root.mainloop()
