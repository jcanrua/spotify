import customtkinter

window = customtkinter.CTk()
window.title("Spotify Playlist Downloader")
window.geometry("750x750")

frame = customtkinter.CTkFrame(window, fg_color="transparent")

textbox = customtkinter.CTkTextbox(frame)
textbox.grid(row=0, column=0, padx=10, pady=12, sticky="ew")
textbox.configure(state="normal", width=400, height=8, corner_radius=10, activate_scrollbar=false) 

button = customtkinter.CTkButton(frame)
button.grid(row=1, column=0, padx=10, pady=12)
button.configure(text="Descargar", fg_color="green", hover_color="darkgreen", command=pulsar_boton)

frame.place(relx=0.5, rely=0.5, anchor='center')


def pulsar_boton():




window.mainloop()