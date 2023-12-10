import bpy
  import socket
  import time

  RaspberryPi_IP = '10.20.200.196'  # Replace with your Raspberry Pi's IP
  RaspberryPi_Port = 12345  # Use the same port as in your Raspberry Pi script
  
  tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcpClient.connect((RaspberryPi_IP, RaspberryPi_Port))

  class OBJECT_OT_SendCursorPosToRaspberryPi(bpy.types.Operator):
      bl_idname = "object.send_cursor_pos_to_raspberry_pi"
      bl_label = "Send Cursor Pos to Raspberry Pi"
  
      def execute(self, context):
          cursor_pos = bpy.context.scene.cursor.location
          data_to_send = f"{cursor_pos.x},{cursor_pos.y},{cursor_pos.z}".encode()
          tcpClient.send(data_to_send)
          print(f"Sent data: {cursor_pos}")
  
          return {'FINISHED'}

  def register():
      bpy.utils.register_class(OBJECT_OT_SendCursorPosToRaspberryPi)
 
  def unregister():
      bpy.utils.unregister_class(OBJECT_OT_SendCursorPosToRaspberryPi)

  def send_cursor_pos(scene):
      bpy.ops.object.send_cursor_pos_to_raspberry_pi('EXEC_DEFAULT')
  
  if __name__ == "__main__":
      register()
      bpy.app.handlers.scene_update_post.append(send_cursor_pos)
  
  On Mon, Dec 4, 2023 at 10:21 AM Deng Veng <dengveng69@gmail.com> wrote:
  import bpy
  import socket
  
  RaspberryPi_IP = '10.20.201.165'
  RaspberryPi_Port = 12346
  
  tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcpClient.connect((RaspberryPi_IP, RaspberryPi_Port))
  
  class OBJECT_OT_SendCursorPosToRaspberryPi(bpy.types.Operator):
      bl_idname = "object.send_cursor_pos_to_raspberry_pi"
      bl_label = "Send Cursor Pos to Raspberry Pi"
  
      old_cursor_pos = None
  
      def execute(self, context):
          cursor_pos = bpy.context.scene.cursor.location
          if cursor_pos != self.old_cursor_pos:
              data_to_send = f"{cursor_pos.x},{cursor_pos.y},{cursor_pos.z}".encode()
              tcpClient.send(data_to_send)
              print(f"Sent data: {cursor_pos}")
              self.old_cursor_pos = cursor_pos
  
          return {'FINISHED'}
  
  def register():
      bpy.utils.register_class(OBJECT_OT_SendCursorPosToRaspberryPi)
  
  def unregister():
      bpy.utils.unregister_class(OBJECT_OT_SendCursorPosToRaspberryPi)
  
  if __name__ == "__main__":
      register()
      bpy.ops.object.send_cursor_pos_to_raspberry_pi('INVOKE_DEFAULT')
