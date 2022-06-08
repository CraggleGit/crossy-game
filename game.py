# Import external libraries and classes
import pygame
from enemy import Enemy
from gameObject import GameObject
from player import Player

# Create a game class to initialise the main game loop
class Game:
    def __init__(self):

        # Create the display window for the game using height and width pixel values
        self.width = 960
        self.height = 960

        # Set the colour of the base game window using RGB values
        self.base_colour = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        # Set a clock to handle display updates per second (framerate)
        self.clock = pygame.time.Clock()

        # Load background image at x, y coordinate of 0, 0; scale to width and
        # height values and pass in the image_path
        self.background = GameObject(0, 0, self.width, self.height, 'assets/background.png')

        # Load a treasure chest at y, x coordinate of 450, 60; scale it and pass the image_path
        self.treasure = GameObject(450, 60, 60, 60, 'assets/treasure.png')

        # Create a difficulty/level variable
        self.level = 1.0

        # Set initial difficulty state on the map
        self.reset_map()

    # Reset the game to default difficulty on collision with enemy
    def reset_map(self): 
        # Load a player sprite at x, y coordinate of 450, 840; scale it and pass the image_path and speed value
        self.player = Player(450, 840, 60, 60, 'assets/player.png', 10)
        
        # Increase enemy speed for each level completion
        speed = 5 + (self.level * 5)

        if self.level >= 4.0:
            # Load enemy sprites from Enemy class at x, y coordinates, scale them, pass the image_path and speed values
            self.enemies = [
                Enemy(450, 770, 60, 60, 'assets/enemy.png', speed),
                Enemy(900, 610, 60, 60, 'assets/enemy.png', speed),
                Enemy(450, 450, 60, 60, 'assets/enemy.png', speed),
                Enemy(0, 290, 60, 60, 'assets/enemy.png', speed)
        ]
        elif self.level >=2.0:
            self.enemies = [
                Enemy(450, 450, 60, 60, 'assets/enemy.png', speed),
                Enemy(0, 290, 60, 60, 'assets/enemy.png', speed)
        ]
        else: 
            self.enemies = [
                Enemy(450, 450, 60, 60, 'assets/enemy.png', speed)
        ]

    # Draw objects such as background, treasure and player
    def draw_objects(self):
        self.game_window.fill(self.base_colour)
        self.game_window.blit(self.background.image, (self.background.x,self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        # Loop through list of enemies and draw each one at its given coordinates
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()


    # Function for player and enemy movements
    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            # Move current enemy loaded from the list
            enemy.move(self.width)


    # Function for collision detection between objects
    def collision_detection(self, object_1, object_2):
        # If no object is colliding return False (object_1 is BELOW object_2)
        if object_1.y > (object_2.y + object_2.height):
            return False
        # Check if object_1 is ABOVE object_2    
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        # Apply the same logic to x axis and use width instead of height (object_1 is further RIGHT that object_2)
        if object_1.x > (object_2.x + object_2.width):
            return False
        # Check is object_1 is further LEFT than object_2
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        # Will return True if any of the objects collide
        return True
    
    # Function to check if player has collided with an enemy or treasure
    def check_if_collided(self):
        for enemy in self.enemies:
            if self.collision_detection(self.player, enemy):
                # Set level back to 1.0 on collision
                self.level = 1.0
                return True
        if self.collision_detection(self.player, self.treasure):
            # Increase the level if player collides with treasure
            self.level += 0.5
            return True
        return False
        

    ### MAIN GAME LOOP ###
    def game_loop(self):
        player_direction = 0
        
        while True:
        # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                # Triggered if any key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # Move player up using the UP key
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    # Move player down using the DOWN key
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                # Triggered if user stops pressing the UP or DOWN key
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        # Stop the player moving
                        player_direction = 0

            # Execute logic for movement and player/enemy height
            self.move_objects(player_direction)
            
            # Update display
            self.draw_objects()

            # Detect collisions
            if self.check_if_collided():
                self.reset_map()

            # Update clock 60 times per second (60fps)
            self.clock.tick(60)
