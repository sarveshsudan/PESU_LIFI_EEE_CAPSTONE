import streamlit as st

device1_state = False
device2_state = False

st.title("Device Control")

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
    device1_button.label = f"Toggle Device 1 {device1_state}"
    device2_button.label = f"Toggle Device 2 {device2_state}"


device1_container = st.container()

device1_label = st.subheader("Device 1")

device1_button = st.button(
    label=f"Toggle Device 1 {device1_state}",
    on_click=toggle_device1_state  # Call the toggle function here
)

device2_container = st.container()

device2_label = st.subheader("Device 2")

device2_button = st.button(
    label=f"Toggle Device 2 {device2_state}",
    on_click=toggle_device2_state  # Call the toggle function here
)
