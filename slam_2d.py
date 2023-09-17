import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Create a 500x500 pixel map
original_map = np.zeros((500, 500))

# Add 50 random 30x30 objects to the map
for _ in range(50):
    x = np.random.randint(0, 500 - 30)
    y = np.random.randint(0, 500 - 30)
    original_map[x:x+30, y:y+30] = 1

# Initialize the robot with a position and a sight radius of 20 pixels
global robot_x  # Mark robot_x as a global variable
global robot_y  # Mark robot_y as a global variable
robot_x = np.random.randint(20, 480)
robot_y = np.random.randint(20, 480)
robot_radius = 20

# Create a figure with two subplots: original map on the left, learned map on the right
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Create an initially empty learned map
learned_map = np.zeros_like(original_map)

def update_robot_sight(original_data, learned_data, robot_x, robot_y, robot_radius):
    for x in range(500):
        for y in range(500):
            if np.sqrt((x - robot_x)**2 + (y - robot_y)**2) <= robot_radius:
                if original_data[x, y] == 1:
                    learned_data[x, y] = 2  # Object detected
                else:
                    learned_data[x, y] = 3  # Free space

def animate(i):
    global robot_x  # Use the global robot_x
    global robot_y  # Use the global robot_y
    
    ax1.clear()
    ax2.clear()
    
    # Simulate the robot's movement
    robot_x += np.random.randint(-5, 6)
    robot_y += np.random.randint(-5, 6)
    # Ensure the robot stays within the map boundaries
    robot_x = np.clip(robot_x, 0, 499)
    robot_y = np.clip(robot_y, 0, 499)
    
    # Update the robot's sight on both maps
    update_robot_sight(original_map, learned_map, robot_x, robot_y, robot_radius)
    
    # Display the original map on the left
    ax1.imshow(original_map, cmap='cool', origin='lower')
    ax1.set_title('Original Map')
    
    # Display the learned map on the right
    ax2.imshow(learned_map, cmap='cool', origin='lower', alpha=0.2)  # Make the sight radius very transparent
    ax2.add_patch(Circle((robot_x, robot_y), robot_radius, color='red', alpha=0.5))  # Draw the transparent red circle
    ax2.scatter(robot_x, robot_y, color='red', s=100, marker='o')  # Mark the robot's position in red
    ax2.set_title('Learned Map')

if __name__ == "__main__":
    # Create an animation with 100 frames
    ani = FuncAnimation(fig, animate, frames=100, repeat=False)

    # Show the animation
    plt.show()
