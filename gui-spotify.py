import customtkinter
import tkinter as tk
import spotifyMassDownload as sp
import threading
import time


window = customtkinter.CTk()
window.title("Spotify Playlist Downloader")
window.geometry("750x750") 

def progreso():
    progressbar.set(sp.porcentaje)
    numeroPorcentaje.set(str(sp.porcentaje*100))
    
    if sp.porcentaje == 1:
        progressbar.set(1)
        numeroPorcentaje.set(str(100))
    else:
        time.sleep(10)
        progreso()

    

def descarga():
    thread_descarga = threading.Thread(target=sp.download)
    thread_porcentaje = threading.Thread(target=progreso)

    thread_descarga.start()
    thread_porcentaje.start()

    thread_descarga.join()
    thread_porcentaje.join()


def pulsar_boton():
    global progressbar, numeroPorcentaje, numeroPorcentajeLabel
    sp.playlist_url = textbox.get(0.0, tk.END)
    textbox.grid_forget()
    button.grid_forget()
    progressbar = customtkinter.CTkProgressBar(
                                            frame, 
                                            orientation="horizontal",
                                            mode="determinate",
                                            progress_color="green",
                                            corner_radius=10,
                                            width=400,
                                            height=15)
    progressbar.grid(row=1, column=0, padx=10, pady=12)
    numeroPorcentaje = tk.StringVar(frame)
    numeroPorcentajeLabel = customtkinter.CTkLabel(
                                            frame, 
                                            textvariable=f'{numeroPorcentaje}%',
                                            fg_color="transparent",
                                            font=("Roboto", 18))
    
    
    progressbar.set(0)
    sp.get_playlist()
    descarga()


frame = customtkinter.CTkFrame(window, fg_color="transparent")

textbox = customtkinter.CTkTextbox(frame, activate_scrollbars=False)
textbox.grid(row=0, column=0, padx=10, pady=12, sticky="ew")
textbox.configure(state="normal", width=400, height=8, corner_radius=10)

button = customtkinter.CTkButton(frame)
button.grid(row=1, column=0, padx=10, pady=12)
button.configure(text="Descargar", fg_color="green", hover_color="darkgreen", command=pulsar_boton)

frame.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop()
