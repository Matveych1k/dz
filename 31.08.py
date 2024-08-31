import customtkinter

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")

label = customtkinter.CTkLabel(app, text="Hello, World!")
label.pack()

app.mainloop()