from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import *
from pytube import YouTube
import validators

root = Tk()
root.title("Youtube-Video-Downloader")
root.geometry('500x500+300+100')
root.resizable(width=False, height=False)
root.iconbitmap('yt.ico')
root.config(bg='gray3')

#Function create...........................................................

direct = " "
def open_path():
        dn_msg.config(text="Please wait a minute, your download running", background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))

        dn_title.config(text=" ")

        dn_size.config(text=" ")

        dn_path.config(text=" ")
        global direct

        direct = filedialog.askdirectory()
        path_h.config(text=direct)

def download():
        url = entry_link.get()
        path = select_type.get()
        if len(url)<1:
            try:
                yt = YouTube(url)
                
                try:
                    if(path == option[0]):
                        typ = yt.streams.get_highest_resolution()
                    elif(path == option[1]):
                        typ = yt.streams.filter(progressive=True, file_extension="mp4").first()
                    elif(path == option[2]):
                        typ = yt.streams.filter(only_audio=True).first()

                    try:
                        typ.download(direct)
                        path_h.config(text="\t\t\t\t     ")
                        dn_msg.config(text="Downloaded", font=(12))

                        name = typ.title
                        size = typ.fileaize/1024000
                        size = round(size,1)


                        dn_title.config(text="Name : "+name)
                        
                        dn_size.config(text="size : "+str(size)+"MB")
                        
                        dn_path.config(text="path"+direct)
                    except:
                        dn_msg.config(text="Download successfully completed", font=(12))
                except:
                     dn_msg.config(text="Download Failed", font=(12))
                
            except:
                dn_msg.config(text="Download Failed", font=(12))

    



label = Label(root, text="YT--DOWNLOWDER", background='gray3', foreground='dark orange', font=('arial', 15, 'bold'))
label.pack(anchor='center', pady=15)

link_name = Label(root, text="URL", background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
link_name.pack(anchor='nw', padx=25)

var = StringVar()

entry_link = Entry(root, textvariable=var)
entry_link.place(x=60, y=55 ,width=400, height=30)



path_h = Label(root, text="Path", background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
path_h.pack(anchor='nw', padx=25, pady=40)



#-----------------------------------------------------------------------------------
'''
path_h = Label(root, text="\t\t\t", background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
path_h.place(x=32, y=130)
'''
#demo...........
error_msg = Label(root, background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
error_msg.place(x=360, y=150)

#add button.........................
style = ttk.Style()
style.configure("s.TButton", background='red', foreground='black', font=('sans', 10, 'bold'))

select_path = Button(root, text="SELECT PATH", style="s.TButton", command=open_path)
select_path.place(x=365, y=117, height=26)

download_type = Label(root, text="Download type", background='gray3', foreground='dark orange', font=('arial', 12, 'bold'))
download_type.place(x=20, y=180)

option = ["High Quality", "Low Quality", "Audio"]
select_type = ttk.Combobox(root, values=option, width=35)
select_type.current(0)
select_type.place(x=145, y=177 ,width=100, height=30)

#Download Button.........................
style = ttk.Style()
style.configure("d.TButton", background='purple', foreground='black', font=('sans', 12, 'bold'))
download_video = Button(root, text="Download Now", style="d.TButton", command=download)
download_video.place(x=120, y=250, height=40, width=250)

#downloading mesaage........
dn_msg = Label(root, background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
dn_msg.place(x=100, y=300)

#download result show......................-----------------------------------------
dn_title = Label(root, background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
dn_title.place(x=100, y=340)

dn_size = Label(root, background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
dn_size.place(x=100, y=380)

dn_path = Label(root, background='gray3', foreground='dark orange', font=('arial', 10, 'bold'))
dn_path.place(x=100, y=420)

#------------------------------------------------------------------------------------

root.mainloop()