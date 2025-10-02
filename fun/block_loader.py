import pygame
import os

properties = {
    "id": "dirt",
    "name": "Dirt Block",
    "solid": True
}

# Load the image (adjust path if needed)
image_path = os.path.join("assets", "images", "dirt.png")
texture = pygame.image.load(image_path).convert_alpha()
