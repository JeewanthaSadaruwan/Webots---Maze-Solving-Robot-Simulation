# from Robot import param
# from collections import deque
# from controller import Robot
# from Robot import calibration
# from Robot import Sensor
# from Robot import setup
# from Robot import Control

# import math

# class MazeNavigator:

#     def has_wall(x, y, direction):
#         """Check if there's a wall in the given direction at position (x,y)"""
#         print(x,y,direction,len(param.maze))
#         if 0 <= x < len(param.maze[0]) and 0 <= y < len(param.maze):
#             print(param.maze[y][x],bool(param.maze[y][x] & direction))
#             return bool(param.maze[y][x] & direction)
#         return True  # Treat out of bounds as walls
    
#     def find_path(target_x, target_y):
#         """Find path to target coordinates using BFS"""
#         if not (0 <= target_x < len(param.maze[0]) and 0 <= target_y < len(param.maze)):
#             return None
        
#         queue = deque([(param.current_x, param.current_y, [])])
#         visited = set()
        
#         while queue:
#             x, y, path = queue.popleft()
            
#             if (x, y) == (target_x, target_y):
#                 return path
            
#             if (x, y) in visited:
#                 continue
                
#             visited.add((x, y))
            
#             # Check all four directions
#             directions = [
#                 (x, y-1,param.NORTH, 'N'),  # North
#                 (x+1, y, param.EAST, 'E'),   # East
#                 (x, y+1, param.SOUTH, 'S'),  # South
#                 (x-1, y, param.WEST, 'W')    # West
#             ]
            
#             for next_x, next_y, wall_dir, move in directions:
#                 if (not MazeNavigator.has_wall(x, y, wall_dir) and 
#                     0 <= next_x < len(param.maze[0]) and 
#                     0 <= next_y < len(param.maze)):
#                     queue.append((next_x, next_y, path + [move]))
        
#         return None
    
#     def get_turn_direction(current_dir, target_dir):
#         """Determine whether to turn left or right"""
#         dirs = ['N', 'E', 'S', 'W']
#         current_idx = dirs.index(current_dir)
#         target_idx = dirs.index(target_dir)
        
#         diff = (target_idx - current_idx) % 4
#         if diff == 1:
#             return 'right'
#         elif diff == 3:
#             return 'left'
#         elif diff == 2:
#             return 'around'
#         return None
    
#     def get_movement_commands(target_x, target_y):
#         """Get list of movement commands to reach target"""
#         path = MazeNavigator.find_path(target_x, target_y)
#         if not path:
#             return []
        
#         commands = []
#         param.current_dir = 'N'  # Assuming starting direction is North
        
#         for move in path:
#             if move != current_dir:
#                 turn = MazeNavigator.get_turn_direction(current_dir, move)
#                 if turn == 'right':
#                     commands.append('rotate_right')
#                 elif turn == 'left':
#                     commands.append('rotate_left')
#                 elif turn == 'around':
#                     commands.append('rotate_right')
#                     commands.append('rotate_right')
#                 current_dir = move
#             commands.append('move_forward')
        
#         return commands
    
#     def calculateTargetRotation(turning_angle):
#         arc_lenngth = math.pi * param.wheelBase * turning_angle / 360
#         target_rotation = arc_lenngth / param.wheelRadius
#         return target_rotation
    
#     def turnleft():

#         param.robot.step(param.timestep)
#         target_rotation = MazeNavigator.calculateTargetRotation(100)
        
#         initial_reading = Sensor.encoderValues()
        
#         while param.robot.step(param.timestep) != -1:
#             setup.left_motor.setVelocity(-param.SPEED)
#             setup.right_motor.setVelocity(param.SPEED)
#             current_reading = Sensor.encoderValues()

#             #check if rotation is complete
#             delta_left = abs(current_reading[0] - initial_reading[0])
#             delta_right = abs(current_reading[1] - initial_reading[1])

#             if delta_left >= target_rotation and delta_right >= target_rotation:
#                 #stop the motors
#                 setup.left_motor.setVelocity(0)
#                 setup.right_motor.setVelocity(0)
#                 break
            
#         #update directions
#         if param.direction == param.NORTH:
#             param.direction=param.EAST

#         elif param.direction == param.EAST:
#             param.direction = param.SOUTH

#         elif param.direction == param.SOUTH:
#             param.direction = param.WEST

#         else:
#             param.direction = param.NORTH

                
#     def turnright():
#         param.robot.step(param.timestep)
#         target_rotation = MazeNavigator.calculateTargetRotation(100)
        
#         initial_reading = Sensor.encoderValues()
        
#         while param.robot.step(param.timestep) != -1:
#             setup.left_motor.setVelocity(param.SPEED)
#             setup.right_motor.setVelocity(-param.SPEED)
#             current_reading = Sensor.encoderValues()

#             #check if rotation is complete
#             delta_left = abs(current_reading[0] - initial_reading[0])
#             delta_right = abs(current_reading[1] - initial_reading[1])

#             if delta_left >= target_rotation and delta_right >= target_rotation:
#                 #stop the motors
#                 setup.left_motor.setVelocity(0)
#                 setup.right_motor.setVelocity(0)
#                 break

#         # Update direction
#         if param.direction == param.NORTH:
#             param.direction = param.WEST

#         elif param.direction == param.WEST:
#             param.direction = param.SOUTH

#         elif param.direction == param.SOUTH:
#             param.direction = param.EAST

#         else:
#             param.direction = param.NORTH

#     def calculateTargetDistance(distance):
#         wheel_circumference = 2 * math.pi * param.wheelRadius
#         target_rotation = (distance / wheel_circumference) * 2 * math.pi  # Convert distance to radians\
#         return target_rotation


#     def movedistance(distance):

#         param.robot.step(param.timestep)
#         target_rotation = MazeNavigator.calculateTargetDistance(distance)
#         # Loop until the target distance is reached
#         initial_reading = Sensor.encoderValues()
        
#         while param.robot.step(param.timestep) != -1:
            
#             setup.left_motor.setVelocity(param.SPEED)
#             setup.right_motor.setVelocity(param.SPEED)

#             # Get current encoder readings
#             current_reading = Sensor.encoderValues()

#             #check if rotation is complete
#             delta_left = abs(current_reading[0] - initial_reading[0])
#             delta_right = abs(current_reading[1] - initial_reading[1])

#             if delta_left >= target_rotation and delta_right >= target_rotation:
#                 #stop the motors
#                 setup.left_motor.setVelocity(0)
#                 setup.right_motor.setVelocity(0)
#                 break
#         print(param.current_x,param.current_y,param.direction)
#         # Update position based on direction
#         if param.direction == param.NORTH and not MazeNavigator.has_wall(param.current_x, param.current_y, param.NORTH):
#             param.current_y -= 1
#         elif param.direction == param.EAST and not MazeNavigator.has_wall(param.current_x, param.current_y, param.EAST):
#             param.current_x += 1
#         elif param.direction == param.SOUTH and not MazeNavigator.has_wall(param.current_x, param.current_y, param.SOUTH):
#             param.current_y += 1
#         elif param.direction == param.WEST and not MazeNavigator.has_wall(param.current_x, param.current_y, param.WEST):
#             param.current_x -= 1
#         print(param.current_x,param.current_y,param.direction)



#     def stop():
#         setup.left_motor.setVelocity(0)
#         setup.right_motor.setVelocity(0)
    


#     def execute_commands(target_x, target_y):
#         """Execute movement commands to reach target coordinates"""
#         commands = MazeNavigator.get_movement_commands(target_x, target_y)

#         if not commands:
#             print(f"No path found to ({target_x}, {target_y})")
#             return False

#         print(f"Executing path to ({target_x}, {target_y})")
#         for cmd in commands:
#             if cmd == 'rotate_right':
#                 MazeNavigator.rotate_right()
#             elif cmd == 'rotate_left':
#                 MazeNavigator.rotate_left()
#             elif cmd == 'move_forward':
#                 MazeNavigator.move_forward()
        
#         param.robot.step(param.timestep)

#         # Verify final position
#         if param.current_x == target_x and param.current_y == target_y:
#             print("Target reached successfully!")
#             return True
#         else:
#             print("Failed to reach target position")
#             return False
        
    