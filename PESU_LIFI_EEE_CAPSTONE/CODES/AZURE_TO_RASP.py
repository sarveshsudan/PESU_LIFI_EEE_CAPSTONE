import time
from azure.iot.device import IoTHubDeviceClient, Message

# Connection parameters for your IoT Hub
CONNECTION_STRING = "HostName=Rpiplugcoontroller.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=U3gToFlE6+x7lbSTow9qTSNZN7qk3AAGaAIoTEMi990="
DEVICE_ID = "rpipwm"

def send_message(device_client, payload):
    try:
        message = Message(payload)
        device_client.send_message(message)
        print(f"Message sent: {payload}")

    except Exception as e:
        print(f"Error sending message: {e}")

def receive_commands(device_client):
    try:
        while True:
            # Receive the message from Azure Digital Twins
            message = device_client.receive_message()

            if message:
                print(f"Received command: {message.data}")

                # Process the command as needed

    except Exception as e:
        print(f"Error receiving commands: {e}")

def main():
    try:
        # Create an instance of the device client
        device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING, device_id=DEVICE_ID)

        # Connect the device client
        device_client.connect()

        print("Connected to Azure IoT Hub")

        # Send some initial data to Azure IoT Hub
        initial_payload = "Initial data from Raspberry Pi"
        send_message(device_client, initial_payload)

        # Simulate receiving commands
        receive_commands(device_client)

    except Exception as e:
        print(f"Error in main: {e}")

    finally:
        # Clean up resources
        if device_client:
            device_client.disconnect()
            print("Disconnected from Azure IoT Hub")

if __name__ == "__main__":
    main()

4.6 Raspberry Pi receiver code from azure: 
from azure.iot.device import IoTHubDeviceClient, Message
import time


CONNECTION_STRING = "HostName=Rpiplugcoontroller.azure-devices.net;DeviceId=rpipwm;SharedAccessKey=QZmLZhGXk+B3Ch6ylKY2CDOVvVBPYCtgQAIoTHyZ26I="


def receiver_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def receive_message(message):
    try:
        print(f"Received message: {message.data}")

        # Add your logic to handle the received message
        # For demonstration, let's print the message on the Raspberry Pi's terminal

    except Exception as e:
        print(f"Error handling message: {e}")

def main():
    try:
        client = receiver_init()
        client.connect()

        # Set the message callback
        client.on_message_received = receive_message

        print("Waiting for messages...")

        # Keep the script running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Receiver program closed.")
    finally:
        client.disconnect()

if _name_ == '_main_':
    main()
