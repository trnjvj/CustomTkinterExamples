def button_event():
    print("button pressed")

button = customtkinter.CTkButton(app, text="CTkButton", command=button_event)


button.configure(text="new text")



text = button.cget("text")


