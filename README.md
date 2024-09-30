Explicación del Código:
Interfaz Gráfica (Tkinter):
tk.Tk()cree la ventana principal de la aplicación.
Entry, Button y Listbox se utilizan para crear los elementos de la GUI:
El Entry es un campo de texto para que el usuario escriba las nuevas tareas.
Los Button son para las funciones de "Añadir Tarea", "Marcar como Completada" y "Eliminar Tarea".
El Listbox muestra las tareas agregadas.
Manejo de Eventos:
Cada botón tiene su función asociada, que se ejecuta cuando se hace clic en el botón.
Además, se asocia el evento de la tecla Enter para que el usuario pueda agregar una tarea presionando Enter, utilizando root.bind('<Return>', add_task).
Lógica de la aplicación:
Añadir Tarea: El texto del Entry se añade a la lista y se borra el campo de entrada.
Completar Tarea: Al hacer clic en "Marcar como Completada", la tarea seleccionada se actualiza visualmente agregando el texto "(Completada)".
Eliminar Tarea: Elimina la tarea seleccionada del Listbox.
En ambos casos (completar o eliminar), si no hay ninguna tarea seleccionada, se muestra un mensaje de advertencia con messagebox.showwarning.


