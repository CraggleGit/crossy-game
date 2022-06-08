# Import any external libraries or classes
from gameObject import GameObject

# Create a sub-class of GameObject to assign to a Player class
class Player(GameObject):

    # Pass x, y, width, height, image_path and speed values
    def __init__(self, x, y, width, height, image_path, speed):
        # Call upon GameObject to avoid repeating the same code
        super().__init__(x, y, width, height, image_path)
        # Set a speed parameter
        self.speed = speed

    # Create a function to move the player and use max_height to create a boundary so that player
    # cannot move outside the game window
    def move(self, direction, max_height):
        if (self.y >= max_height - self.height and direction > 0) or (self.y <= 0 and direction < 0):
            return

        self.y += (direction * self.speed)
