button = customtkinter.CTkButton(app, font=("<family name>", <size in px>, "<optional keywords>"))


button = customtkinter.CTkButton(app, font=customtkinter.CTkFont(family="<family name>", size=<size in px>, <optional keyword arguments>))

button.cget("font").configure(size=new_size)  # configure font afterwards



my_font = customtkinter.CTkFont(family="<family name>", size=<size in px>, <optional keyword arguments>)

button_1 = customtkinter.CTkButton(app, font=my_font)
button_2 = customtkinter.CTkButton(app, font=my_font)

my_font.configure(family="new name")  # changes apply to button_1 and button_2




