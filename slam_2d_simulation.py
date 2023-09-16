import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Landmark:
    """Class for landmarks."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    """Class for robot."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


def move_robot(robot, dx, dy):
    """Move the robot by dx and dy."""
    robot.x += dx
    robot.y += dy


def update(frame, robot, landmarks, scat):
    """Update function for animation."""
    move_robot(robot, 0.1, 0.1)
    scat.set_offsets([[robot.x, robot.y]] + [[lm.x, lm.y] for lm in landmarks])
    return scat,


def visualize_slam(robot, landmarks):
    """Visualize SLAM with animation."""
    fig, ax = plt.subplots()
    scat = ax.scatter([robot.x] + [lm.x for lm in landmarks], [robot.y] + [lm.y for lm in landmarks])
    
    ani = animation.FuncAnimation(fig, update, frames=range(100), fargs=(robot, landmarks, scat))
    plt.show()


if __name__ == "__main__":
    robot = Robot(0, 0)
    landmarks = [Landmark(np.random.randint(1, 10), np.random.randint(1, 10)) for _ in range(5)]
    visualize_slam(robot, landmarks)

