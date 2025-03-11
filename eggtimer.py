import tkinter as tk
from tkinter import messagebox, PhotoImage
import time

# Global variable to track active timer
timer_running = False

def start_timer():
    global timer_running
    timer_running = True
    start_button.config(text="Reset Timer", command=reset_timer)
    label.config(text="Timer: 3:00")
    countdown(180)  # 3 minutes

def reset_timer():
    global timer_running
    timer_running = False  # Stop current timer
    start_button.config(text="Start Timer", command=start_timer)
    label.config(text="Press Start to begin", fg="black")
    image_label.config(image=egg_image)  # Reset to original image

def countdown(seconds):
    global timer_running
    if not timer_running:
        return  # Stop the countdown if reset is pressed
    
    if seconds > 0:
        minutes, secs = divmod(seconds, 60)
        time_format = f"Timer: {minutes}:{secs:02d}"
        label.config(text=time_format)
        root.after(1000, countdown, seconds - 1)
    else:
        label.config(text="Egg is ready!", fg="green")
        messagebox.showinfo("Egg Timer", "The egg is finished cooking!")
        start_button.config(text="Start Timer", command=start_timer)
        cycle_images()

def cycle_images():
    global current_image
    current_image = egg_image2 if current_image == egg_image3 else egg_image3
    image_label.config(image=current_image)
    root.after(1000, cycle_images)

# Create main window
root = tk.Tk()
root.title("Egg Timer")
root.geometry("400x400")
root.configure(bg="lightyellow")

# Load and resize images
try:
    egg_image = PhotoImage(file="egg.png").zoom(5, 5)  # Image size
    egg_image2 = PhotoImage(file="egg2.png").zoom(5, 5)
    egg_image3 = PhotoImage(file="egg3.png").zoom(5, 5)
    current_image = egg_image
    image_label = tk.Label(root, image=egg_image, bg="lightyellow")
    image_label.pack(pady=10)
except Exception as e:
    print("Images not found. Proceeding without them.")
    egg_image = None
    egg_image2 = None
    egg_image3 = None
    current_image = None
    image_label = tk.Label(root, bg="lightyellow")
    image_label.pack(pady=10)

# Load pixel font
pixel_font = ("Arial Rounded MT Bold", 14)

# Label to display time
label = tk.Label(root, text="Press Start to begin", font=pixel_font, bg="lightyellow", fg="black")
label.pack(pady=20)

# Start button
start_button = tk.Button(root, text="Start Timer", font=("Arial Rounded MT Bold", 12), command=start_timer, bg="orange", fg="white")
start_button.pack()

# Run the application
root.mainloop()