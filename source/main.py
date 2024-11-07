import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Importa ttk para usar Notebook

# Verificar si el módulo Tkinter se ha importado exitosamente
print(f'Modulo: {tk.__name__} fue importado exitosamente!')

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Markdown: Editor')
        self.geometry('800x400')
        self.resizable(False, False)
        
        # Crear el Notebook para manejar las pestañas
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)
        
        # Crear el frame para la pestaña "Editor"
        editor_tab = tk.Frame(notebook)
        notebook.add(editor_tab, text="Editor")  # Añadir la pestaña

        # Crear el frame para la pestaña "Visor"
        viewer_tab = tk.Frame(notebook)
        notebook.add(viewer_tab, text="Visor")  # Añadir otra pestaña

        # Crear la funcionalidad del editor dentro de la pestaña "Editor"
        self.theme_app = False
        theme_button = tk.Button(editor_tab, text='🌓', width=2, height=1, command=self._change_theme_callback)
        theme_button.place(x=10, y=10)

        self.text_widget = tk.Text(editor_tab, wrap='word', font=('Arial', 12))
        self.text_widget.place(x=50, y=0, width=700, height=360)

        # Crear un menú contextual para abrir y guardar archivos
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label='Guardar', command=self._guardar_markdown)
        self.menu.add_command(label='Abrir', command=self._abrir_archivo)
        self.menu.add_separator()
        self.menu.add_command(label='Cerrar', command=self.quit)
        
        # Vincular el menú contextual al clic derecho
        self.text_widget.bind('<Button-3>', self._mostrar_menu)

        # Agregar contenido de prueba a la pestaña "Visor"
        viewer_label = tk.Label(viewer_tab, text="Aquí se mostrará el contenido del archivo", font=('Arial', 12))
        viewer_label.pack(pady=20)
        
    def _change_theme_callback(self):
        """Callback para alternar el tema entre claro y oscuro."""
        self.theme_app = not self.theme_app
        
        if self.theme_app:
            self.config(bg='black')
            self.text_widget.config(bg='black', fg='white')
        else:
            self.config(bg='white')
            self.text_widget.config(bg='white', fg='black')
        
    def _guardar_markdown(self):
        text_md = self.text_widget.get("1.0", tk.END)
        md_filetype = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[('Archivos Markdown', '*.md')])
        
        if md_filetype:
            try:
                with open(md_filetype, 'w') as f:
                    f.write(text_md)
                print('Markdown Guardado')
            except Exception as e:
                print(f'Error al guardar: {e}')

    def _abrir_archivo(self):
        md_filetype = filedialog.askopenfilename(title="Seleccionar archivo Markdown", filetypes=[('Archivos Markdown', '*.md')])
        
        if md_filetype:
            try:
                with open(md_filetype, 'r') as file:
                    content = file.read()
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert(tk.END, content)
            except Exception as e:
                print(f'Error al abrir el archivo: {e}')

    def _mostrar_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

# Ejecutar la aplicación
if __name__ == '__main__':
    app = Editor()
    app.mainloop()
