import tkinter as tk
import subprocess

def run_server():
    subprocess.Popen(["python", "server.py"])

def run_client():
    subprocess.Popen(["python", "client.py"])

root = tk.Tk()
root.title("VPN - Tunnel")
root.geometry("400x200")
root.configure(bg='#8ecae6')  # Set the background color to red

button_server = tk.Button(root, text="Start Server", command=run_server)
button_server.pack(pady=10)

button_client = tk.Button(root, text="Start Client", command=run_client)
button_client.pack(pady=10)

# add a button with image

image = tk.PhotoImage(file="logo.png")  
button_image = tk.Button(root, image=image)
button_image.pack(pady=10)

root.mainloop()