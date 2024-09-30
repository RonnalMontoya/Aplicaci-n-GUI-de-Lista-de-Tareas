import tkinter as tk
from tkinter import messagebox


# Función para añadir tarea
def add_task(event=None):
    task = entry.get()  # Obtener texto del campo de entrada
    if task:  # Si hay algo en la entrada
        listbox_tasks.insert(tk.END, task)  # Añadir tarea al final de la lista
        entry.delete(0, tk.END)  # Limpiar campo de entrada
    else:
        messagebox.showwarning("Input Error", "Tienes que ingresar una tarea.")


# Función para marcar una tarea como completada
def complete_task():
    try:
        # Obtener la tarea seleccionada
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)

        # Actualizar la tarea agregando "(Completada)" al final del texto
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, task + " (Completada)")
    except IndexError:
        messagebox.showwarning("Selection Error", "Selecciona una tarea para marcar como completada.")


# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Selecciona una tarea para eliminar.")


# Crear ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Crear marco principal
frame = tk.Frame(root)
frame.pack(pady=10)

# Crear entrada de texto para nuevas tareas
entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=10)

# Crear botón para añadir tarea
button_add_task = tk.Button(frame, text="Añadir Tarea", command=add_task)
button_add_task.pack(side=tk.LEFT)

# Crear Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=45, height=10)
listbox_tasks.pack(pady=10)

# Crear botón para marcar como completada
button_complete_task = tk.Button(root, text="Marcar como Completada", command=complete_task)
button_complete_task.pack(pady=5)

# Crear botón para eliminar tarea
button_delete_task = tk.Button(root, text="Eliminar Tarea", command=delete_task)
button_delete_task.pack(pady=5)

# Manejar evento de la tecla Enter para añadir tarea
root.bind('<Return>', add_task)

# Ejecutar la aplicación
root.mainloop()
