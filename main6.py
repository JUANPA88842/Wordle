from tkinter import *
import words
from tkinter import messagebox
import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")  

#1.0 Variables principales

#Variables del marcador
victorias = 0
derrotas = 0

#Funciones del marcador
def Victorias():
    messagebox.showinfo("Felicidades bro!",f"Tienes {victorias} victorias")

def Derrotas():
    messagebox.showinfo("Que pasa ps bro",f"Tienes {derrotas} derrotas")

#Palabras aleatorias a adivinar
word4 = words.get_word4().lower()
word5 = words.get_word5().lower()
word6 = words.get_word6().lower()
word7 = words.get_word7().lower()
word8 = words.get_word8().lower()

#Colores de las palabras
GREEN = "#16A120"
YELLOW = "#F5E900"
BLACK = "#000000"
WHITE = "#FFFFFF"

#Variables que sirve como contador de intentos
intentos = 0


#2.0 Función que ejecuta juego con 4 letras

def abrirjuego4():
    """Juego de 4 letras, función de cerrar ventana, reiniciar y adivinar palabra
    """
    def CerrarVentana():
        root.destroy()
        ventana.deiconify()

    #Comenzar el juego
    root = customtkinter.CTk()
    root.title("Wordle")
    root.geometry("800x600")
    ventana.iconify()
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Wordle") 
    label_1.grid(row=0, column=0, pady=12, padx=10)

    def reiniciar():
        global intentos
        intentos = 0
        root.destroy()
        ventana.deiconify()
    root.protocol("WM_DELETE_WINDOW", reiniciar)

    def getGuess4():
        global word4
        global victorias
        global derrotas
        global intentos
        intentos += 1
        repetidas = set()
        guess = wordInput.get().lower()
        if intentos != 6:
            if len(guess) == 4:
                if word4 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word4}") 
                    intentos = 0 
                    word4 = words.get_word4()  
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
                else:                   #Incorrecto
                    diccionario = {}
                    for i, letter in enumerate(guess):
                        diccionario[i] = letter
                    for j in diccionario:
                        label = customtkinter.CTkLabel(master=frame_1, text=diccionario[j].upper(), width=30, height=35, corner_radius=6)
                        label.grid(row=intentos, column=(j+1) ,pady=12, padx=10)
                        if diccionario[j] == word4[j]:  #Si hay una letra correcta
                            label.configure(fg_color="green", text_color='white')
                            repetidas.add(diccionario[j])  
                        if diccionario[j] in word4 and not diccionario[j] == word4[j]:  #Cuando la letra esta en la palabra pero no en el lugar específico
                            if diccionario[j] in repetidas:
                                label.configure(fg_color="black", text_color='white')
                                continue
                            else:
                                repetidas.add(diccionario[j])
                                label.configure(fg_color="yellow", text_color='black')
                        if diccionario[j] not in word4:
                            label.configure(fg_color="black", text_color='white')
            else:
                messagebox.showerror("ooops!", "Usar 4 caracteres")
                intentos -= 1
        elif intentos == 6:
            if word4 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word4}")
                    intentos = 0 
                    word4 = words.get_word4()  
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
            else:
                messagebox.showerror("Perdiste", f"la palabra era: {word4}")
                intentos = 0
                diccionario = {}
                word4 = words.get_word4()
                repetidas = set()
                derrotas += 1
                CerrarVentana()
                ventana.deiconify()

    #Ventana con tamaños
    wordInput = customtkinter.CTkEntry(master=frame_1, placeholder_text="Pon una palabra")
    wordInput.grid(row=6, column=0, pady=10, padx=20, sticky="w")

    #Boton de adivinar
    wordGuessButton = customtkinter.CTkButton(master=frame_1, command=getGuess4, text="Adivina")
    wordGuessButton.grid(row=12, column=0, pady=12, padx=10)

    #Corre el programa
    root.mainloop()

#3.0 Función que ejecuta juego con 5 letras

def abrirjuego5():
    """Juego de 5 letras, función de cerrar ventana, reiniciar y adivinar palabra
    """
    def CerrarVentana():
        root.destroy()
        ventana.deiconify()
    
    #Comenzar el juego
    root = customtkinter.CTk()
    root.title("Wordle")
    root.geometry("800x600")
    ventana.iconify()
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Wordle") 
    label_1.grid(row=0, column=0, pady=12, padx=10)

    def reiniciar():
        global intentos
        intentos = 0
        root.destroy()
        ventana.deiconify()

    root.protocol("WM_DELETE_WINDOW",reiniciar)

    def getGuess5():
        global word5
        global victorias
        global derrotas
        global intentos
        intentos += 1
        repetidas = set()
        guess = wordInput.get().lower()
        if intentos != 6:
            if len(guess) == 5:
                if word5 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word5}")
                    intentos = 0
                    word5 = words.get_word5() 
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
                else:                   #Incorrecto
                    diccionario = {}
                    for i, letter in enumerate(guess):
                        diccionario[i] = letter
                    repetidas = set()
                    for j in diccionario:
                        label = customtkinter.CTkLabel(master=frame_1, text=diccionario[j].upper(), width=30, height=35, corner_radius=6)
                        label.grid(row=intentos, column=(j+1) ,pady=12, padx=10)
                        if diccionario[j] == word5[j]:  #Si hay una letra correcta
                            label.configure(fg_color="green", text_color='white')
                            repetidas.add(diccionario[j])
                        if diccionario[j] in word5 and not diccionario[j] == word5[j]:  #Cuando la letra esta en la palabra pero no en el lugar específico
                            if diccionario[j] in repetidas:
                                label.configure(fg_color="black", text_color='white')
                                continue
                            else:
                                repetidas.add(diccionario[j])
                                label.configure(fg_color="yellow", text_color='black')
                        if diccionario[j] not in word5:
                            label.configure(fg_color="black", text_color='white')
            else:
                messagebox.showerror("oopps!", "usar 5 caracteres")
                intentos -= 1
        elif intentos == 6:
            if word5 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word5}")
                    intentos = 0
                    word5 = words.get_word5()
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
            else:
                messagebox.showerror("Perdiste", f"la palabra era: {word5}")     
                intentos = 0
                word5 = words.get_word5()
                repetidas = set()
                derrotas += 1
                CerrarVentana()
                ventana.deiconify()
     
    #Ventana con tamaños
    wordInput = customtkinter.CTkEntry(master=frame_1, placeholder_text="Pon una palabra")
    wordInput.grid(row=6, column=0, pady=10, padx=20, sticky="w")

    #Boton de adivinar
    wordGuessButton = customtkinter.CTkButton(master=frame_1, command=getGuess5, text="Adivina")
    wordGuessButton.grid(row=12, column=0, pady=12, padx=10)

    #Corre el programa
    root.mainloop()

#4.0 Función que ejecuta juego con 6 letras

def abrirjuego6():
    """Juego de 6 letras, función de cerrar ventana, reiniciar y adivinar palabra
    """
    def CerrarVentana():
        root.destroy()
        ventana.deiconify()
    
    #Comenzar el juego
    root = customtkinter.CTk()
    root.title("Wordle")
    root.geometry("800x600")
    ventana.iconify()
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Wordle") 
    label_1.grid(row=0, column=0, pady=12, padx=10)

    def reiniciar():
        global intentos
        intentos = 0
        root.destroy()
        ventana.deiconify()

    root.protocol("WM_DELETE_WINDOW",reiniciar)

    def getGuess6():
        global word6
        global victorias
        global derrotas
        global intentos
        intentos += 1
        repetidas = set()
        guess = wordInput.get().lower()
        if intentos != 6:
            if len(guess) == 6:
                if word6 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word6}")
                    intentos = 0
                    word6 = words.get_word6()
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
                else:                   #Incorrecto
                    diccionario = {}
                    for i, letter in enumerate(guess):
                        diccionario[i] = letter
                    repetidas = set()
                    for j in diccionario:
                        label = customtkinter.CTkLabel(master=frame_1, text=diccionario[j].upper(), width=30, height=35, corner_radius=6)
                        label.grid(row=intentos, column=(j+1) ,pady=12, padx=10)
                        if diccionario[j] == word6[j]:  #Si hay una letra correcta
                            label.configure(fg_color="green", text_color='white')
                            repetidas.add(diccionario[j])
                        if diccionario[j] in word6 and not diccionario[j] == word6[j]:  #Cuando la letra esta en la palabra pero no en el lugar específico
                            if diccionario[j] in repetidas:
                                label.configure(fg_color="black", text_color='white')
                                continue
                            else:
                                repetidas.add(diccionario[j])
                                label.configure(fg_color="yellow", text_color='black')
                        if diccionario[j] not in word6:
                            label.configure(fg_color="black", text_color='white')
            else:
                messagebox.showerror("oopps!", "usar 6 caracteres")
                intentos -= 1 
        elif intentos == 6:
            if word6 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word6}")
                    intentos = 0
                    word6 = words.get_word6()
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
            else:
                messagebox.showerror("Perdiste", f"la palabra era: {word6}")
                intentos = 0
                word6 = words.get_word6()
                repetidas = set()
                derrotas += 1
                CerrarVentana()
                ventana.deiconify()

    #Ventana con tamaños
    wordInput = customtkinter.CTkEntry(master=frame_1, placeholder_text="Pon una palabra")
    wordInput.grid(row=6, column=0, pady=10, padx=20, sticky="w")

    #Boton de adivinar
    wordGuessButton = customtkinter.CTkButton(master=frame_1, command=getGuess6, text="Adivina")
    wordGuessButton.grid(row=12, column=0, pady=12, padx=10)

    #Corre el programa
    root.mainloop()
    
#5.0 Función que ejecuta juego con 7 letras
def abrirjuego7():
    """Juego de 7 letras, función de cerrar ventana, reiniciar y adivinar palabra
    """
    def CerrarVentana():
        root.destroy()
        ventana.deiconify()
    
    #Comenzar el juego
    root = customtkinter.CTk()
    root.title("Wordle")
    root.geometry("800x600")
    ventana.iconify()
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Wordle") 
    label_1.grid(row=0, column=0,pady=12, padx=10)

    def reiniciar():
        global intentos
        intentos = 0
        root.destroy()
        ventana.deiconify()

    root.protocol("WM_DELETE_WINDOW",reiniciar)

    def getGuess7():
        global word7
        global victorias
        global derrotas
        global intentos
        intentos += 1
        repetidas = set()
        guess = wordInput.get().lower()
        if intentos != 6:
            if len(guess) == 7:
                if word7 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word7}")
                    intentos = 0
                    word7 = words.get_word7()
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
                else:                   #Incorrecto
                    diccionario = {}
                    for i, letter in enumerate(guess):
                        diccionario[i] = letter
                    repetidas = set()
                    for j in diccionario:
                        label = customtkinter.CTkLabel(master=frame_1, text=diccionario[j].upper(), width=30, height=35, corner_radius=6)
                        label.grid(row=intentos, column=(j+1) ,pady=12, padx=10)
                        if diccionario[j] == word7[j]:  #Si hay una letra correcta
                            label.configure(fg_color="green", text_color='white')
                            repetidas.add(diccionario[j])
                        if diccionario[j] in word7 and not diccionario[j] == word7[j]:  #Cuando la letra esta en la palabra pero no en el lugar específico
                            if diccionario[j] in repetidas:
                                label.configure(fg_color="black", text_color='white')
                                continue
                            else:
                                repetidas.add(diccionario[j])
                                label.configure(fg_color="yellow", text_color='black')
                        if diccionario[j] not in word7:
                            label.configure(fg_color="black", text_color='white')
            else:
                messagebox.showerror("ooppss!", "usar 7 caracteres")
                intentos -= 1
        elif intentos == 6:
            if word7 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word7}")
                    intentos = 0
                    word7 = words.get_word7()
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
            else:
                messagebox.showerror("Perdiste", f"la palabra era: {word7}") 
                intentos = 0
                word7 = words.get_word7()
                repetidas = set()
                derrotas += 1
                CerrarVentana()
                ventana.deiconify()

    #Ventana con tamaños
    wordInput = customtkinter.CTkEntry(master=frame_1, placeholder_text="Pon una palabra")
    wordInput.grid(row=6, column=0, pady=10, padx=20, sticky="w")

    #Boton de adivinar
    wordGuessButton = customtkinter.CTkButton(master=frame_1, command=getGuess7, text="Adivina")
    wordGuessButton.grid(row=12, column=0,pady=12, padx=10)

    #Corre el programa
    root.mainloop()

#6.0 Función que ejecuta juego con 8 letras

def abrirjuego8():
    """Juego de 8 letras, función de cerrar ventana, reiniciar y adivinar palabra
    """
    def CerrarVentana():
        root.destroy()
        ventana.deiconify()
    
    #Comenzar el juego
    root = customtkinter.CTk()
    root.title("Wordle")
    root.geometry("800x600")
    ventana.iconify()
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Wordle") 
    label_1.grid(row=0, column=0,pady=12, padx=10)

    def reiniciar():
        global intentos
        intentos = 0
        root.destroy()
        ventana.deiconify()

    root.protocol("WM_DELETE_WINDOW",reiniciar)

    def getGuess8():
        global word8
        global victorias
        global derrotas
        global intentos
        intentos += 1
        repetidas = set()
        guess = wordInput.get().lower()
        
        if intentos != 6:
            if len(guess) == 8:
                if word8 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word8}")
                    intentos = 0
                    word8 = words.get_word8()
                    repetidas = set()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
                else:                   #Incorrecto
                    diccionario = {}
                    for i, letter in enumerate(guess):
                        diccionario[i] = letter
                    repetidas = set()
                    for j in diccionario:
                        label = customtkinter.CTkLabel(master=frame_1, text=diccionario[j].upper(), width=30, height=35, corner_radius=6)
                        label.grid(row=intentos, column=(j+1) ,pady=12, padx=10)
                        if diccionario[j] == word8[j]:  #Si hay una letra correcta
                            label.configure(fg_color="green", text_color='white')
                            repetidas.add(diccionario[j])
                        if diccionario[j] in word8 and not diccionario[j] == word8[j]:  #Cuando la letra esta en la palabra pero no en el lugar específico
                            if diccionario[j] in repetidas:
                                label.configure(fg_color="black", text_color='white')
                                continue
                            else:
                                repetidas.add(diccionario[j])
                                label.configure(fg_color="yellow", text_color='black')
                        if diccionario[j] not in word8:
                            label.configure(fg_color="black", text_color='white')
            else:
                messagebox.showerror("oopps!", "usar 8 caracteres")
                intentos -= 1
        elif intentos == 6:
            if word8 == guess:       #Correcto
                    messagebox.showinfo("Correcto", f"La palabra es: {word8}")
                    intentos = 0
                    word8 = words.get_word8()
                    victorias += 1
                    CerrarVentana()
                    ventana.deiconify()
            else:
                messagebox.showerror("Perdiste", f"la palabra era: {word8}")     
                intentos = 0
                word8 = words.get_word8()
                repetidas = set()
                derrotas += 1
                CerrarVentana()
                ventana.deiconify()

    #Ventana con tamaños
    wordInput = customtkinter.CTkEntry(master=frame_1, placeholder_text="Pon una palabra")
    wordInput.grid(row=6, column=0, pady=10, padx=20, sticky="w")

    #Boton de adivinar
    wordGuessButton = customtkinter.CTkButton(master=frame_1, command=getGuess8, text="Adivina")
    wordGuessButton.grid(row=12, column=0, pady=12, padx=10)

    #Corre el programa
    root.mainloop()

ventana = customtkinter.CTk()
ventana.geometry("800x600")
ventana.title("CustomTkinter simple_example.py")

def button_callback():
    """Opciones del menú principal
    """
    if optionmenu_1.get() == "4 Letras":
        abrirjuego4()
    if optionmenu_1.get() == "5 Letras":
        abrirjuego5()
    if optionmenu_1.get() == "6 Letras":
        abrirjuego6()
    if optionmenu_1.get() == "7 Letras":
        abrirjuego7()
    if optionmenu_1.get() == "8 Letras":
        abrirjuego8()
        
#7.0 Botones del menú principal

frame_1 = customtkinter.CTkFrame(master=ventana)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Wordle") 
label_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Play")
button_1.pack(pady=12, padx=10)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Escoge una dificultad") 
label_1.pack(pady=12, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["4 Letras", "5 Letras", "6 Letras", "7 Letras", "8 Letras"])
optionmenu_1.pack(pady=50, padx=10)
optionmenu_1.set("Dificultad")

button_2 = customtkinter.CTkButton(master=frame_1, command=Victorias, text="Victorias")
button_2.pack(pady=10, padx=80)

button_3 = customtkinter.CTkButton(master=frame_1, command=Derrotas, text="Derrotas")
button_3.pack(pady=0, padx=0)

ventana.mainloop()
