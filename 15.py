# Analog Clock

import tkinter as tk
import time
import math

def update_clock(canvas, radius, center_x, center_y):
    canvas.delete("all")
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius)
    
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    if hour >= 12:
        hour -= 12
    
    hour_angle = (hour % 12 + minute / 60) * 30 - 90
    minute_angle = (minute + second / 60) * 6 - 90
    second_angle = second * 6 - 90
    
    hour_x = center_x + radius * 0.5 * math.cos(math.radians(hour_angle))
    hour_y = center_y + radius * 0.5 * math.sin(math.radians(hour_angle))
    minute_x = center_x + radius * 0.7 * math.cos(math.radians(minute_angle))
    minute_y = center_y + radius * 0.7 * math.sin(math.radians(minute_angle))
    second_x = center_x + radius * 0.9 * math.cos(math.radians(second_angle))
    second_y = center_y + radius * 0.9 * math.sin(math.radians(second_angle))
    
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill="black")
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="blue")
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red")
    
    canvas.after(1000, update_clock, canvas, radius, center_x, center_y)

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

radius = 150
center_x = 200
center_y = 200

update_clock(canvas, radius, center_x, center_y)
root.mainloop()