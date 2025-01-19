from Robot import param
from collections import deque
from controller import Robot
from Robot import Sensor
from Robot import setup


import math

class maze:

    def has_wall(x, y, direction):
        """Check if there's a wall in the given direction at position (x,y)"""
        if 0 <= x < len(param.maze[0]) and 0 <= y < len(param.maze):
            return bool(param.maze[y][x] & direction)
        return True  # Treat out of bounds as walls
    
    def find_path(target_x, target_y):
        """Find path to target coordinates using BFS"""
        if not (0 <= target_x < len(param.maze[0]) and 0 <= target_y < len(param.maze)):
            return None
        
        queue = deque([(param.current_x, param.current_y, [])])
        visited = set()
        
        while queue:
            x, y, path = queue.popleft()
            
            if (x, y) == (target_x, target_y):
                return path
            
            if (x, y) in visited:
                continue
                
            visited.add((x, y))
            
            # Check all four directions
            directions = [
                (x, y-1,param.NORTH, 'N'),  # North
                (x+1, y, param.EAST, 'E'),   # East
                (x, y+1, param.SOUTH, 'S'),  # South
                (x-1, y, param.WEST, 'W')    # West
            ]
            
            for next_x, next_y, wall_dir, move in directions:
                if (not maze.has_wall(x, y, wall_dir) and 
                    0 <= next_x < len(param.maze[0]) and 
                    0 <= next_y < len(param.maze)):
                    queue.append((next_x, next_y, path + [move]))
        
        return None
    
    def get_turn_direction(current_dir, target_dir):
        """Determine whether to turn left or right"""
        dirs = ['N', 'E', 'S', 'W']
        current_idx = dirs.index(current_dir)
        target_idx = dirs.index(target_dir)
        
        diff = (target_idx - current_idx) % 4
        if diff == 1:
            return 'right'
        elif diff == 3:
            return 'left'
        elif diff == 2:
            return 'around'
        return None
    
    def get_movement_commands(target_x, target_y):
        """Get list of movement commands to reach target"""
        path = maze.find_path(target_x, target_y)
        if not path:
            return []
        
        commands = []
        
        for move in path:
            if move != param.current_dir:
                turn = maze.get_turn_direction(param.current_dir, move)
                if turn == 'right':
                    commands.append('rotate_right')
                elif turn == 'left':
                    commands.append('rotate_left')
                elif turn == 'around':
                    commands.append('rotate_right')
                    commands.append('rotate_right')
                param.current_dir = move
            commands.append('move_forward')
        
        return commands
    
    def calculateTargetRotation(turning_angle):
        arc_lenngth = math.pi * param.wheelBase * turning_angle / 360
        target_rotation = arc_lenngth / param.wheelRadius
        return target_rotation
    
    def turn_left():
        setup.left_motor.setVelocity(-param.turning_SPEED)
        setup.right_motor.setVelocity(param.turning_SPEED)

        steps = int((1.2445 * 1000)/param.timestep)
        for _ in range(steps):
            param.robot.step(param.timestep)

        setup.left_motor.setVelocity(0)
        setup.right_motor.setVelocity(0)

    def turn_right():
        setup.left_motor.setVelocity(param.turning_SPEED)
        setup.right_motor.setVelocity(-param.turning_SPEED)

        steps = int((1.2445 * 1000)/param.timestep)
        for _ in range(steps):
            param.robot.step(param.timestep)

        setup.left_motor.setVelocity(0)
        setup.right_motor.setVelocity(0)

    def turnleft():

        param.robot.step(param.timestep)
        target_rotation = maze.calculateTargetRotation(98.174)
        
        initial_reading = Sensor.encoderValues()
        
        while param.robot.step(param.timestep) != -1:
            setup.left_motor.setVelocity(-param.turning_SPEED)
            setup.right_motor.setVelocity(param.turning_SPEED)
            current_reading = Sensor.encoderValues()

            #check if rotation is complete
            delta_left = abs(current_reading[0] - initial_reading[0])
            delta_right = abs(current_reading[1] - initial_reading[1])

            if delta_left >= target_rotation and delta_right >= target_rotation:
                #stop the motors
                setup.left_motor.setVelocity(0)
                setup.right_motor.setVelocity(0)
                break
            
        #update directions
        if param.direction == param.NORTH:
            param.direction=param.EAST

        elif param.direction == param.EAST:
            param.direction = param.SOUTH

        elif param.direction == param.SOUTH:
            param.direction = param.WEST

        else:
            param.direction = param.NORTH

                
    def turnright():
        param.robot.step(param.timestep)
        target_rotation = maze.calculateTargetRotation(98.174)
        
        initial_reading = Sensor.encoderValues()
        
        while param.robot.step(param.timestep) != -1:
            setup.left_motor.setVelocity(param.turning_SPEED)
            setup.right_motor.setVelocity(-param.turning_SPEED)
            current_reading = Sensor.encoderValues()

            #check if rotation is complete
            delta_left = abs(current_reading[0] - initial_reading[0])
            delta_right = abs(current_reading[1] - initial_reading[1])

            if delta_left >= target_rotation and delta_right >= target_rotation:
                #stop the motors
                setup.left_motor.setVelocity(0)
                setup.right_motor.setVelocity(0)
                break

        # Update direction
        if param.direction == param.NORTH:
            param.direction = param.WEST

        elif param.direction == param.WEST:
            param.direction = param.SOUTH

        elif param.direction == param.SOUTH:
            param.direction = param.EAST

        else:
            param.direction = param.NORTH

    def calculateTargetDistance(distance):
        wheel_circumference = 2 * math.pi * param.wheelRadius
        target_rotation = (distance / wheel_circumference) * 2 * math.pi  # Convert distance to radians\
        return target_rotation


    def moveforward():

        param.robot.step(param.timestep)
        target_rotation = maze.calculateTargetDistance(0.25)
        # Loop until the target distance is reached
        initial_reading = Sensor.encoderValues()
        
        while param.robot.step(param.timestep) != -1:
            
            setup.left_motor.setVelocity(param.forward_SPEED)
            setup.right_motor.setVelocity(param.forward_SPEED)

            # Get current encoder readings
            current_reading = Sensor.encoderValues()

            #check if rotation is complete
            delta_left = abs(current_reading[0] - initial_reading[0])
            delta_right = abs(current_reading[1] - initial_reading[1])

            if delta_left >= target_rotation and delta_right >= target_rotation:
                #stop the motors
                setup.left_motor.setVelocity(0)
                setup.right_motor.setVelocity(0)
                break
        # print(param.current_x,param.current_y,param.direction)
        # Update position based on direction
        if param.direction == param.NORTH and not maze.has_wall(param.current_x, param.current_y, param.NORTH):
            param.current_y -= 1
        elif param.direction == param.EAST and not maze.has_wall(param.current_x, param.current_y, param.EAST):
            param.current_x += 1
        elif param.direction == param.SOUTH and not maze.has_wall(param.current_x, param.current_y, param.SOUTH):
            param.current_y += 1
        elif param.direction == param.WEST and not maze.has_wall(param.current_x, param.current_y, param.WEST):
            param.current_x -= 1
        # print(param.current_x,param.current_y,param.direction)



    def stop():
        setup.left_motor.setVelocity(0)
        setup.right_motor.setVelocity(0)
    
    # def teleport_robot(x,y):
    #     param.robot_node.getField("translation").setSFVec3f([x,0,y])


    def execute_commands(target_x, target_y):

        setup.speaker.playSound(
            left=setup.speaker,
            right=setup.speaker,
            sound=param.music,
            volume=param.volume,
            pitch=param.pitch,
            balance=param.balance,
            loop=True
        )
        """Execute movement commands to reach target coordinates"""
        commands = maze.get_movement_commands(target_x, target_y)
        print(commands)
        if not commands:
            print(f"No path found to ({target_x}, {target_y})")
            return False

        print(f"Executing path to ({target_x}, {target_y})")

        
        

        for cmd in commands:
            print("Executing command:", cmd)  # Add this debug print
            if cmd == 'rotate_right':
                maze.turnright()
            elif cmd == 'rotate_left':
                maze.turnleft()
            elif cmd == 'move_forward':
                maze.moveforward()

        setup.speaker.stop()
        setup.speaker.playSound(
            left=setup.speaker,
            right=setup.speaker,
            sound=param.end,
            volume=param.volume,
            pitch=param.pitch,
            balance=param.balance,
            loop=False
        )
        # Verify final position
        if param.current_x == target_x and param.current_y == target_y:
            print("Target reached successfully!")
            return True
        else:
            print("Failed to reach target position")
            return False
        

    def set_robot_position(x, y, z):
        """Set the robot's position in the world."""
        if setup.trans_field:
            setup.trans_field.setSFVec3f([x, y, z])
            
    def set_robot_rotation(angle_degrees):
        """Set the robot's rotation around the Y axis."""
        # Convert angle to radians
        angle_rad = math.radians(angle_degrees)
        # In Webots, rotation is specified as [x y z angle]
        # For rotation around Y axis, we use [0 1 0 angle]
        if setup.rot_field:
            setup.rot_field.setSFRotation([0, 0, -1, angle_rad])
            
    def position_robot(x, y, z, angle_degrees):
        """Set both position and rotation of the robot."""
        maze.set_robot_position(x, y, z)
        maze.set_robot_rotation(angle_degrees)


    def final():
        setup.speaker.playSound(
            left=setup.speaker,
            right=setup.speaker,
            sound=param.music,
            volume=param.volume,
            pitch=param.pitch,
            balance=param.balance,
            loop=True
        )
        """Execute movement commands to reach target coordinates"""
        print(param.current_x,param.current_y)
        targetr_x = 7
        targetr_y = 3
        commands = maze.get_movement_commands(targetr_x, targetr_y)
        print(commands)
        if not commands:
            print(f"No path found to ({targetr_x}, {targetr_y})")
            return False

        print(f"Executing path to ({targetr_x}, {targetr_y})")

        for cmd in commands:
            print("Executing command:", cmd)  # Add this debug print
            if cmd == 'rotate_right':
                maze.turnright()
            elif cmd == 'rotate_left':
                maze.turnleft()
            elif cmd == 'move_forward':
                maze.moveforward()
        
        maze.position_robot(0.625,0.375, 0.0, -90)
        
        commands = []

        param.current_x = 7
        param.current_y = 3
        targety_x = 5
        targety_y = 9

        commands = maze.get_movement_commands(targety_x, targety_y)
        print(commands)
        if not commands:
            print(f"No path found to ({targety_x}, {targety_y})")
            return False

        print(f"Executing path to ({targety_x}, {targety_y})")

        for cmd in commands:
            print("Executing command:", cmd)  # Add this debug print
            if cmd == 'rotate_right':
                maze.turnright()
            elif cmd == 'rotate_left':
                maze.turnleft()
            elif cmd == 'move_forward':
                maze.moveforward()

        maze.position_robot(0.125,-1.125, 0.0, 90)
        commands = []

        param.current_x = 5
        param.current_y = 9
        targetp_x = 7
        targetp_y = 6

        commands = maze.get_movement_commands(targetp_x, targetp_y)
        print(commands)
        if not commands:
            print(f"No path found to ({targetp_x}, {targetp_y})")
            return False

        print(f"Executing path to ({targetp_x}, {targetp_y})")

        for cmd in commands:
            print("Executing command:", cmd)  # Add this debug print
            if cmd == 'rotate_right':
                maze.turnright()
            elif cmd == 'rotate_left':
                maze.turnleft()
            elif cmd == 'move_forward':
                maze.moveforward()

        maze.position_robot(0.625,-0.375, 0.0, 90)
        commands = []

        param.current_x = 7
        param.current_y = 6
        targetb_x = 8
        targetb_y = 6

        commands = maze.get_movement_commands(targetb_x, targetb_y)
        print(commands)
        if not commands:
            print(f"No path found to ({targetb_x}, {targetb_y})")
            return False

        print(f"Executing path to ({targetb_x}, {targetb_y})")

        for cmd in commands:
            print("Executing command:", cmd)  # Add this debug print
            if cmd == 'rotate_right':
                maze.turnright()
            elif cmd == 'rotate_left':
                maze.turnleft()
            elif cmd == 'move_forward':
                maze.moveforward()


        maze.position_robot(0.875,-0.375, 0.0, 0)
        commands = []

        param.current_x = 8
        param.current_y = 6
        targetrr_x = 7
        targetrr_y = 2

        commands = maze.get_movement_commands(targetrr_x, targetrr_y)
        print(commands)
        if not commands:
            print(f"No path found to ({targetrr_x}, {targetrr_y})")
            return False

        print(f"Executing path to ({targetrr_x}, {targetrr_y})")

        for cmd in commands:
            print("Executing command:", cmd)  # Add this debug print
            if cmd == 'rotate_right':
                maze.turnright()
            elif cmd == 'rotate_left':
                maze.turnleft()
            elif cmd == 'move_forward':
                maze.moveforward()
        
        maze.position_robot(0.625,0.625, 0.0, 95)
        commands = []

        param.current_x = 7
        param.current_y = 2
        targetg_x = 0
        targetg_y = 6

        commands = maze.get_movement_commands(targetg_x, targetg_y)
        print(commands)
        if not commands:
            print(f"No path found to ({targetg_x}, {targetg_y})")
            return False

        print(f"Executing path to ({targetg_x}, {targetg_y})")

        for cmd in commands:
            print("Executing command:", cmd)  # Add this debug print
            if cmd == 'rotate_right':
                maze.turnright()
            elif cmd == 'rotate_left':
                maze.turnleft()
            elif cmd == 'move_forward':
                maze.moveforward()
        
        setup.speaker.stop()
        setup.speaker.playSound(
            left=setup.speaker,
            right=setup.speaker,
            sound=param.end,
            volume=param.volume,
            pitch=param.pitch,
            balance=param.balance,
            loop=False
        )

        setup.speaker.stop()



        

    