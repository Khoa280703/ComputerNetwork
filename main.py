from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os 
from PIL import Image, ImageTk
import time

def send_pid_to_server(pid):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))  
    client_socket.send(pid.encode())
    client_socket.close()

def on_exit():
    pid = str(os.getpid())
    send_pid_to_server("exit")  # Send "exit" message to the server
    root.destroy()

root = Tk()
root.title("P2P File Sharing")
root.geometry("950x600+300+100")
root.configure(bg="#f4fdfe")
root.resizable(False,False)


id_list = []
host = socket.gethostname()
pid = os.getpid()
unique_id = f'{pid}'
id_list.append(unique_id)
id_text = Text(root, height=10, width=20, bg="#ffffff", bd=0, font=('Arial', 12))
id_text.place(x=800, y=100)
id_text.insert(END, "\n".join(id_list))

def select_file():
    global filename
    filename= filedialog.askopenfilename(initialdir=os.getcwd(),
                                         title ='Select Image File',
                                         filetype=(('file_type','*.txt'),('all file','*.*')))

def sender():
    s=socket.socket()
    host=socket.gethostname()
    port= 8080
    s.bind((host,port))
    s.listen(1)
    print(host)
    print('wating for any incoming connections...')
    conn,addr=s.accept()
    file=open(filename,'rb')
    file_data=file.read(1024)
    conn.send(file_data)
    print("Data has been transmitted successfully...")

def Send():
    window= Toplevel(root)
    window.title("Send")
    window.geometry("950x600+300+100")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    #icon
    image_icon1=PhotoImage(file="Image/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="Image/sendframe.png")
    Label(window, image= Sbackground).place(x=0, y=0)

    Label(window, text=f'ID: {unique_id}', bg='white', fg='black').place(x=420, y=100)

    Button(window, text ="+ select file", width =10, height =1, font ='arial 14 bold', bg="#fff", fg="#000", command = select_file).place(x=340, y = 290)
    Button(window, text="SEND", width=8, height =1, font='arial 14 bold', bg= "#000", fg="#fff", command = sender).place(x = 500,y=290)
    window.mainloop()

def Receive():
    main= Toplevel(root)
    main.title("Receive")
    main.geometry("950x600+300+100")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    #icon
    image_icon1=PhotoImage(file="Image/receive.png")
    main.iconphoto(False, image_icon1)

    Hbackground=PhotoImage(file="Image/sendframe.png")
    Label(main, image=Hbackground).place(x =0, y=0)
    
    Label(main, text ="Receive", font=('arial, 20'), bg ="#f4fdfe").place(x = 430, y = 90)

    Label(main, text="Input client id", font =('arial', 10, 'bold'), bg= "#f4fdfe").place(x = 300, y= 253)
    SenderID= Entry(main,width=20, fg= "black", border =2, bg='white', font =('arial', 15))
    SenderID.place(x =410, y = 250)
    SenderID.focus()

    Label(main, text="Input filename", font =('arial', 10, 'bold'), bg= "#f4fdfe").place(x = 300, y= 303)
    icoming_file= Entry(main,width=20, fg= "black", border =2, bg='white', font =('arial', 15))
    icoming_file.place(x =410, y = 300)

    rr=Button(main, text ="Download", compound=LEFT, width=13, bg ="#39c790", font="arial 14 bold")
    rr.place(x = 420, y= 350)

    main.mainloop()


#icon
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False, image_icon)

Label(root, text ="File Sharing", font =('Acumin Variable Concept', 20,'bold'), bg ="#f4fdfe").place(x=400,y =30)

Frame(root, width= 400, height =2, bg ="#f3f5f6").place(x=25,y=80)


send_original = Image.open("Image/send.png")
receive_original = Image.open("Image/receive.png")

# Resize the images to a smaller size (e.g., 100x100)
send_resized = send_original.resize((100, 100))
receive_resized = receive_original.resize((100, 100))

# Convert the resized images to PhotoImage objects
send_image = ImageTk.PhotoImage(send_resized)
receive_image = ImageTk.PhotoImage(receive_resized)

# Create the buttons
send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command= Send)
receive = Button(root, image=receive_image, bg="#f4fdfe", bd=0, command = Receive)

# Position the buttons using the grid layout manager
send.grid(row=0, column=0, padx=10)
receive.grid(row=0, column=1, padx=10)

# Center the buttons within the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

#label
Label(root, text ="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x= 205, y =230)
Label(root, text ="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x= 665, y =230)


background=PhotoImage(file="Image/background.png")
Label(root, image= background).place(x=-2, y= 400)

def on_start():
    pid = str(os.getpid())
    send_pid_to_server(pid)

def send_exit_signal():
    pid = str(os.getpid())
    send_pid_to_server("exit")  # Send "exit" signal when the window closes

root.protocol("WM_DELETE_WINDOW", send_exit_signal)  # Intercept the window close event
on_start()

root.mainloop()
