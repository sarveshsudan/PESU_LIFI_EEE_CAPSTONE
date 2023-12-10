import tkinter as t
device1_state = False
device2_state = False

def toggle_device1_state():
    global device1_state
    device1_state = not device1_state
    update_device_button_labels()

def toggle_device2_state():
    global device2_state
    device2_state = not device2_state
    update_device_button_labels()

def toggle_all_devices_on():
    global device1_state, device2_state
    device1_state = True
    device2_state = True
    update_device_button_labels()

def toggle_all_devices_off():
    global device1_state, device2_state
    device1_state = False
    device2_state = False
    update_device_button_labels()

def update_device_button_labels():
    if device1_state:
        device1_button.config(text="Device 1 ON")
    else:
        device1_button.config(text="Device 1 OFF")

    if device2_state:
        device2_button.config(text="Device 2 ON")
    else:
        device2_button.config(text="Device 2 OFF")

window = tk.Tk()
window.title("Device Control")

device1_frame = tk.Frame(window)
device1_frame.pack(side=tk.TOP)

device1_label = tk.Label(device1_frame, text="Device 1:")
device1_label.pack()

device1_button = tk.Button(device1_frame, text="Toggle Device 1", command=toggle_device1_state)
device1_button.pack()

device2_frame = tk.Frame(window)
device2_frame.pack(side=tk.TOP)

device2_label = tk.Label(device2_frame, text="Device 2:")
device2_label.pack()

device2_button = tk.Button(device2_frame, text="Toggle Device 2", command=toggle_device2_state)
device2_button.pack()

toggle_all_on_button = tk.Button(window, text="Toggle All On", command=toggle_all_devices_on)
toggle_all_on_button.pack()

toggle_all_off_button = tk.Button(window, text="Toggle All Off", command=toggle_all_devices_off)
toggle_all_off_button.pack()

window.mainloop()

