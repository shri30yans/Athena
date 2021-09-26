import tkinter as tk
import encoding

root=tk.Tk()
root.geometry("800x600")
root.title("Encrypter")
root.iconbitmap("images/icon.ico")
# Setting icon o master window

menu = tk.Menu(root)
# Defining the menu of our Tkinter window
root.config(menu = menu)

class Frame:
    # Creating a Frame with a Label and Text box for Encryption 
    def __init__(self,colour,LabelText,ButtonText, ButtonCommand):
        #root.configure(background=colour)
        self.Frame = tk.Frame(root,width = 800,height = 600,bg = colour)
        self.Label = tk.Label(self.Frame,text = LabelText,height = 3,bg = colour)
        self.TextBox = tk.Text(self.Frame,width = 50,height = 5)
        # creating a button using the widget
        self.Button = tk.Button(self.Frame,text = ButtonText,command = ButtonCommand)
        
        self.OutputTextBox = tk.Text(self.Frame,width = 50, height = 5)
        self.OutputTextBox.insert(tk.END,"Output will come here.")
        self.OutputTextBox.config(state = 'disabled')
    
    def SetFrame(self):
        self.hide_all_frames()
        self.Frame.grid(row = 0,column = 0)
        self.Label.grid(row = 0,column = 0)
        self.TextBox.grid(row = 0,column = 1)
        self.Button.grid(row = 1,column = 1)
        self.OutputTextBox.grid(row = 2,column = 1)

    def hide_all_frames(self):
        DecryptFrameObj.Frame.grid_forget()
        EncryptFrameObj.Frame.grid_forget()
    
    def ChangeOutput(self,text):
        self.OutputTextBox.config(state = 'normal')
        self.OutputTextBox.delete('1.0', tk.END)
        self.OutputTextBox.insert(tk.END,text)
        self.OutputTextBox.config(state = 'disabled')

def encryption_button_click():
    #"1.0" means that the input should be read from the first character and line zero
    #end-1c means End of text and then remove 1 character from the end ("\n")
    text = EncryptFrameObj.TextBox.get("1.0",'end-1c')
    encMessage = Encoding.encrypt(text)
    EncryptFrameObj.ChangeOutput(encMessage)


def decryption_button_click():
    #"1.0" means that the input should be read from the first character and line zero
    #end-1c means End of text and then remove 1 character from the end ("\n")
    text = DecryptFrameObj.TextBox.get("1.0",'end-1c')
    bytestext = bytes(text, 'utf-8')
    decMessage = Encoding.decrypt(bytestext)
    DecryptFrameObj.ChangeOutput(decMessage)



EncryptFrameObj = Frame(colour = "green",LabelText="Text to encrypt:",ButtonText="Encrypt",ButtonCommand=encryption_button_click)
DecryptFrameObj = Frame(colour = "red",LabelText="Text to decrypt:",ButtonText="Decrypt",ButtonCommand=decryption_button_click)


# Create a menu item
file_menu = tk.Menu(menu)
# Creating a sub menu by associating it with our parent menu
menu.add_cascade(label="Encoding",menu = file_menu)
file_menu.add_command(label = "Encrypt",command = EncryptFrameObj.SetFrame)
file_menu.add_command(label = "Decrypt",command = DecryptFrameObj.SetFrame)





root.mainloop()