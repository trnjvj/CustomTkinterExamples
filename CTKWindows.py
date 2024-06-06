app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")

app.mainloop()




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app
    def button_click(self):
        print("button click")


app = App()
app.mainloop()





app.configure(fg_color=new_fg_color)





fg_color = app.cget("fg_color")





