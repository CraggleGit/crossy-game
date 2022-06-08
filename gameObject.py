import pygame

# Create GameObject class to hold game objects that are being used more than once (images mostly)
class GameObject:
    # Pass x, y, width, height and image_path values
    def __init__(self, x, y, width, height, image_path):
        # Load an image from a path and scale it up
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))
        # Every game object will have these 4 properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height
