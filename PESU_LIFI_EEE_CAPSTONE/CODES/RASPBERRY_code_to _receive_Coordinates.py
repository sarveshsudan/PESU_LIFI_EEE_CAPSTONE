  import socket
  import RPi.GPIO as GPIO
  import time
  import threading
  GPIO.setwarnings(False)
  
  class Object:
      def __init__(self, vertices, duty_cycle):
          self.vertices = vertices
          self.duty_cycle = duty_cycle
  
  class DigitalTwin:
      def __init__(self):
          self.objects = []
  
      def add_object(self, obj):
          self.objects.append(obj)
  
      def find_object(self, point):
          for idx, obj in enumerate(self.objects):
              x, y, z = point
              x_values, y_values, z_values = zip(*obj.vertices)
  
              if min(x_values) <= x <= max(x_values) and \
                 min(y_values) <= y <= max(y_values) and \
                 min(z_values) <= z <= max(z_values):
                  return idx, obj.duty_cycle
  
          return "NO Device", None
  
      def receive_coordinates(self):
          server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          server_socket.bind(('10.20.201.165', 12346))  # Choose a suitable port
          server_socket.listen(1)
  
          print("Waiting for connection...")
          conn, addr = server_socket.accept()
          print(f"Connection from {addr}")
  
          try:
              while True:
                  data = conn.recv(1024)
                  if not data:
                      break  # Break the loop if no data is received
                  coordinates = data.decode()
                  print(f"Received coordinates: {coordinates}")
  
                  point = tuple(map(float, coordinates.split(',')))
  
                  obj_index, duty_cycle = self.find_object(point)
                  if obj_index is not None:
                      print(f"Point belongs to object {obj_index + 1}")
                      print(f"Applying PWM with duty cycle: {duty_cycle}")
  
                      pwm_thread = threading.Thread(target=self.start_pwm, args=(obj_index, duty_cycle))
                      pwm_thread.start()
  
          except Exception as e:
              print(f"Error: {e}")
  
          finally:
              conn.close()
              server_socket.close()
  
      def start_pwm(self, obj_index, duty_cycle):
          pwm_pin = 18  
          frequency = 250  
  
          GPIO.setmode(GPIO.BCM)
          GPIO.setup(pwm_pin, GPIO.OUT)
          pwm = GPIO.PWM(pwm_pin, frequency)
  
          pwm.start(duty_cycle)
          time.sleep(1000)  # Run PWM for a specific duration (10 seconds in this case)
          pwm.stop()
          GPIO.cleanup()
  
  if __name__ == "__main__":

      object1 = Object([(9.694780349731445,-14.018527030944824,7.888457298278809), (9.695409774780273,-14.010496139526367,8.959671020507812), (9.674747467041016,-15.895212173461914,9.035609245300293), (9.694960594177246,-15.879796028137207,7.8829569816589355)], duty_cycle=30)
      object2 = Object([(9.34733772277832,8.863290786743164,8.95805549621582), (9.347139358520508,8.886310577392578,7.760686874389648), (9.347257614135742,10.98607349395752,9.000123977661133), (9.368307113647461,10.981321334838867,7.877028465270996)], duty_cycle=70)
  

      digital_twin = DigitalTwin()
      digital_twin.add_object(object1)
      digital_twin.add_object(object2)
      digital_twin.receive_coordinates()

