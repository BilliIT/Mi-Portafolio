from tkinter import*
from tkinter.ttk import*
from time import strftime

def actualizar_reloj():
    etiqueta_hm.config(text = strftime ("%H:%M"))
    etiqueta_s.config(text = strftime ("%S"))
    etiqueta_fecha.config(text = strftime ("%A, %d/%m/%Y"))
    etiqueta_s.after(1000, actualizar_reloj)

#Ventana
ventana = Tk()
ventana.title("Reloj digital")

frame_hora = Frame()
frame_hora.pack()
etiqueta_hm = Label(frame_hora, font = ("Digitalk", 100), text = "H:M")
etiqueta_hm.grid(row = 0, column = 0)

etiqueta_s = Label(frame_hora, font = ("Digitalk", 50), text = "s")
etiqueta_s.grid(row = 0, column = 1, sticky = "n")

etiqueta_fecha = Label(font = ("Digitalk", 50), text = "dia d/m/aaaa")
etiqueta_fecha.pack(anchor = "center")

actualizar_reloj()

ventana.mainloop()