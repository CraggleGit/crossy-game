# Import any external libraries or classes
from gameObject import GameObject

# Enemy class will be a sub-class of the GameObject class
class Enemy(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed
    
    # Use max_width here because the enemies move from left to right not up and down like the player
    def move(self, max_width):
        # Check if the enemy is at the far left of the screen
        if self.x <= 0:
            # Don't add or subract from speed, keep the value postive
            self.speed = abs(self.speed)
        elif self.x >= max_width - self.width:
            # Ensure that the enemy moves in the opposite direction if it hits a boundary
            self.speed = -self.speed

        self.x += self.speed
