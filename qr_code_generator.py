import os
import tkinter.messagebox
from PIL import ImageTk, Image
import qrcode
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


class Main(tkinter.Tk):
    def __init__(self):
        # initialize window
        super().__init__()
        # window config
        self.title("QR Code Generator")
        self.geometry("800x600")
        # instance variables
        self.top_rect = tkinter.Frame(self.master, background="red", width=800, height=75)
        self.left_rect = tkinter.Frame(self.master, background="gray", width=400, height=525)
        self.right_rect = tkinter.Frame(self.master, background="black", width=400, height=525)
        self.text_var = tkinter.StringVar()  # for text entry in text_data
        self.link_var = tkinter.StringVar()  # for text entry in link_data
        self.fallback_image = Image.open(r"./qr_code_example.png")
        self.qr_code = None
        self.file_content = None
        self.display_image = None
        # member function calls
        self.set_content_layout()
        self.make_gui()

    # creates the layout for window content
    def set_content_layout(self) -> None:
        # contains a title for the window
        self.top_rect.grid(column=0, row=0, columnspan=2, rowspan=1, padx=0, pady=0)
        # handles data entry, retrieval, and QR code generation
        self.left_rect.grid(column=0, row=1, columnspan=1, rowspan=1, padx=0, pady=0)
        # displays the generated QR code and allows the user to save it
        self.right_rect.grid(column=1, row=1, columnspan=1, rowspan=1, padx=0, pady=0)
        return None
    
    # member function to retrieve return value from filedialog.askopenfile() and read the content
    def read_text_file(self) -> None:
        self.text_file_path = askopenfilename()
        # make sure the file exists
        while not os.path.isfile(self.text_file_path):
            messagebox.showerror("Invalid File", "Invalid file selected. Please try again.")
            self.text_file_path = askopenfilename()
        # make sure its a text file
        while os.path.splitext(self.text_file_path)[1] != ".txt":
            messagebox.showerror("Invalid File Type", "Invalid file type provided. Please select a text (.txt) file.")
            self.text_file_path = askopenfilename()
        # show resulting path
        text_path_confirmation  = tkinter.Label(self.left_rect, text=self.text_file_path, font=("Helvetica bold", 8))
        text_path_confirmation.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        # read text file
        self.file_content = ""
        with open(self.text_file_path, "r") as f:
            self.file_content += f.read()
            f.close()
        return

    # creates GUI elements in the window
    def make_gui(self) -> None:
        # top_rect elements
        title = tkinter.Label(self.top_rect, text="Python QR Code Generator", font=("Helvetica bold", 26, "bold"))
        title.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # left_rect elements
        # header
        left_header = tkinter.Label(self.left_rect, text="Options", font=("Helvetica bold", 13))
        left_header.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        # text data
        text_data = tkinter.Entry(self.left_rect, textvariable=self.text_var, width=50)
        text_data.place(relx=0.55, rely=0.2, anchor=tkinter.CENTER)
        text_label = tkinter.Label(self.left_rect, text="Text:", font=("Helvetica bold", 13, "bold"), bg="black", fg="white")
        text_label.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
        # allow for text file upload in lieu of typing
        get_text_path = tkinter.Button(self.left_rect, text="Load Text File", command=self.read_text_file)
        get_text_path.place(relx=0.5, rely= 0.4, anchor=tkinter.CENTER)
        # generate qr code button
        generate_button = tkinter.Button(self.left_rect, text="Generate QR Code", command=self.generate_qr_code)
        generate_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        # right_rect elements
        save_button = tkinter.Button(self.right_rect, text="Save QR Code", command=lambda: print("save button pressed"))
        save_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        return None

    def generate_qr_code(self) -> None:
        # get text data and make the qr code
        if self.text_var.get():
            self.qr_code = qrcode.make(self.text_var.get())
            self.display_image = ImageTk.PhotoImage(self.qr_code.get_image())
            label = tkinter.Label(self.right_rect, image=self.display_image, width=250, height=300)
            label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
            print(self.qr_code.get_image())
        # text file data
        elif self.file_content:
            self.qr_code = qrcode.make(self.file_content)
            self.display_image = ImageTk.PhotoImage(self.qr_code.get_image())
            label = tkinter.Label(self.right_rect, image=self.display_image, width=250, height=300)
            label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
            print(self.qr_code.get_image())
        return None


if __name__ == "__main__":
    window = Main()
    window.mainloop()

'''
# Encode the data using make()
img = qrcode.make(data)

# Save as a PNG file
img.save("qr_code.png")
'''
