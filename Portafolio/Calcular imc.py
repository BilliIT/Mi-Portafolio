from tkinter import *
from tkinter import messagebox

#Ventana
ventana = Tk()
ventana.geometry("550x550")
ventana.title("IMC")
ventana.minsize(width = 500, height = 250)

def imc():
        label_peso = e_peso.get()
        label_altura = e_altura.get()
        IMC = float(label_peso) / (float(label_altura)**2)

        if label_peso == "" or label_altura == "":
            messagebox.showerror("Error", "Faltan Valores para calcular tu IMC!")
        elif IMC <= 0:
            IMC = float(label_peso) / (float(label_altura)**2)
            messagebox.showinfo("IMC",IMC)
        elif IMC <= 16:
            messagebox.showinfo(IMC,"Desnutriciòn severa")
        elif IMC >= 16.1 and IMC <= 18.4:
              messagebox.showinfo(IMC, "Desnutriciòn moderada")
        elif IMC >= 18.5 and IMC <= 22:
              messagebox.showinfo(IMC, "Bajo peso")   
        elif IMC >= 22.1 and IMC <= 24.9:
              messagebox.showinfo(IMC, "Peso normal")  
        elif IMC >= 25 and IMC <= 29.9:
              messagebox.showinfo(IMC, "Sobre peso")   
        elif IMC >= 30 and IMC <= 34.9:
              messagebox.showinfo(IMC, "Obesidad tipo 1") 
        elif IMC >= 35 and IMC <= 39.9:
              messagebox.showinfo(IMC, "Obesidad tipo 2") 
        elif IMC >= 40:
              messagebox.showinfo(IMC, "Obesidad tipo 3")                                    



#Ajuste automatico ventana
ventana.columnconfigure(0, weight = 1)
ventana.columnconfigure(1, weight = 1)
ventana.rowconfigure(0, weight = 1)
ventana.rowconfigure(1, weight = 1)
ventana.rowconfigure(2, weight = 1)
ventana.rowconfigure(3, weight = 1)



label_titulo = Label(ventana, text = "Calcula tu IMC", font = "arial 20")
label_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 8)

label_peso = Label(ventana, text = "Peso", font = "arial 15")
label_peso.grid(row = 2, column = 0, pady = 8)

label_altura = Label(ventana, text = "Altura", font = "arial 15")
label_altura.grid(row = 1, column = 0, pady = 8)

e_peso = Entry(ventana, font = "arial 15")
e_peso.grid(row = 2, column = 1, pady = 8)

e_altura = Entry(ventana, font = "arial 15")
e_altura.grid(row = 1, column = 1, pady = 8)

calcular = Button(ventana, text = "Calcular", bg = "black", fg = "white", font = "arial 20", command = imc)
calcular.grid(row = 3, column = 0, columnspan = 2, pady = 8)

ventana.mainloop()