def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.set("option 2")


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox_var = customtkinter.StringVar(value="option 2")
combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"],
                                     command=combobox_callback, variable=combobox_var)
combobox_var.set("option 2")



state = combobox.cget("state")



