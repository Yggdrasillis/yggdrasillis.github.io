#!/usr/bin/env python3
"""Generate a pixel art style plesiosaur background image"""

from PIL import Image, ImageDraw
import random

# Image dimensions
width, height = 1920, 600

# Create image with white background
img = Image.new('RGB', (width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Pixel size for pixel art effect
pixel_size = 6

# Function to draw pixelated rectangle
def draw_pixel_rect(x, y, w, h, color):
    px = (x // pixel_size) * pixel_size
    py = (y // pixel_size) * pixel_size
    pw = ((w + pixel_size - 1) // pixel_size) * pixel_size
    ph = ((h + pixel_size - 1) // pixel_size) * pixel_size
    draw.rectangle([px, py, px + pw, py + ph], fill=color)

# Function to draw pixelated ellipse (for rounded shapes)
def draw_pixel_ellipse(x, y, w, h, color):
    px = (x // pixel_size) * pixel_size
    py = (y // pixel_size) * pixel_size
    pw = ((w + pixel_size - 1) // pixel_size) * pixel_size
    ph = ((h + pixel_size - 1) // pixel_size) * pixel_size
    draw.ellipse([px, py, px + pw, py + ph], fill=color)

# Function to draw outline
def draw_pixel_outline(x, y, w, h, color, thickness=pixel_size):
    # Top
    draw_pixel_rect(x, y, w, thickness, color)
    # Bottom
    draw_pixel_rect(x, y + h - thickness, w, thickness, color)
    # Left
    draw_pixel_rect(x, y, thickness, h, color)
    # Right
    draw_pixel_rect(x + w - thickness, y, thickness, h, color)

# Plesiosaur colors - more vibrant and defined
body_color = (70, 150, 200)  # Blue
belly_color = (150, 200, 230)  # Light blue
outline_color = (30, 60, 100)  # Dark blue outline
eye_color = (255, 255, 255)  # White
pupil_color = (0, 0, 0)  # Black
highlight_color = (180, 220, 250)  # Light highlight

# Plesiosaur position (moved left, wider and flatter)
base_x = width // 2 - 550
base_y = height // 2 + 20

# Draw body (main torso) with outline - wider and flatter, more streamlined
body_x, body_y = base_x + 250, base_y + 30
body_w, body_h = 480, 130
# Outline
draw_pixel_ellipse(body_x - pixel_size, body_y - pixel_size, body_w + pixel_size*2, body_h + pixel_size*2, outline_color)
# Body
draw_pixel_ellipse(body_x, body_y, body_w, body_h, body_color)

# Draw belly with highlight - more realistic shape
belly_w, belly_h = 340, 85
draw_pixel_ellipse(body_x + 70, body_y + 23, belly_w, belly_h, belly_color)
# Belly highlight
draw_pixel_ellipse(body_x + 110, body_y + 28, 250, 50, highlight_color)

# Draw neck (long curved neck) - more elegant S-curve like real plesiosaur
neck_segments = [
    (base_x + 200, base_y + 60, 68, 58),
    (base_x + 168, base_y + 42, 66, 56),
    (base_x + 140, base_y + 25, 64, 54),
    (base_x + 116, base_y + 8, 62, 52),
    (base_x + 96, base_y - 8, 60, 50),
    (base_x + 80, base_y - 22, 58, 48),
    (base_x + 68, base_y - 35, 56, 46),
    (base_x + 60, base_y - 47, 54, 44),
    (base_x + 56, base_y - 58, 52, 42),
]

# Draw neck outline first
for seg in neck_segments:
    draw_pixel_ellipse(seg[0] - pixel_size, seg[1] - pixel_size, seg[2] + pixel_size*2, seg[3] + pixel_size*2, outline_color)

# Draw neck body
for seg in neck_segments:
    draw_pixel_ellipse(seg[0], seg[1], seg[2], seg[3], body_color)

# Draw head with more detail - more elongated like real plesiosaur
head_x, head_y = base_x + 50, base_y - 78
head_w, head_h = 80, 50
# Head outline
draw_pixel_ellipse(head_x - pixel_size, head_y - pixel_size, head_w + pixel_size*2, head_h + pixel_size*2, outline_color)
# Head
draw_pixel_ellipse(head_x, head_y, head_w, head_h, body_color)

# Draw snout/mouth area - longer snout
snout_x, snout_y = base_x + 28, base_y - 72
draw_pixel_ellipse(snout_x - pixel_size, snout_y - pixel_size, 60 + pixel_size*2, 28 + pixel_size*2, outline_color)
draw_pixel_ellipse(snout_x, snout_y, 60, 28, body_color)

# Draw mouth line - curved smile
mouth_y = base_y - 62
draw_pixel_rect(base_x + 35, mouth_y, 50, pixel_size, outline_color)
# Add slight curve to mouth
draw_pixel_rect(base_x + 40, mouth_y + pixel_size, 40, pixel_size, outline_color)

# Draw eye with more detail - larger, more expressive
eye_x, eye_y = head_x + 48, head_y + 16
# Eye white - larger
draw_pixel_rect(eye_x, eye_y, 20, 20, eye_color)
# Eye outline
draw_pixel_outline(eye_x, eye_y, 20, 20, outline_color, pixel_size)
# Pupil - larger
draw_pixel_rect(eye_x + 7, eye_y + 7, 9, 9, pupil_color)
# Eye shine - more prominent
draw_pixel_rect(eye_x + 4, eye_y + 4, pixel_size*2, pixel_size*2, (255, 255, 255))

# Draw nostril - slightly larger
nostril_x, nostril_y = base_x + 38, base_y - 65
draw_pixel_rect(nostril_x, nostril_y, pixel_size*2, pixel_size, outline_color)

# Draw tail with more segments - longer, more tapered like real plesiosaur
tail_segments = [
    (base_x + 720, base_y + 68, 85, 72),
    (base_x + 795, base_y + 76, 75, 60),
    (base_x + 860, base_y + 83, 65, 50),
    (base_x + 915, base_y + 89, 55, 40),
    (base_x + 960, base_y + 94, 45, 32),
    (base_x + 995, base_y + 98, 35, 24),
]

# Draw tail outline
for seg in tail_segments:
    draw_pixel_ellipse(seg[0] - pixel_size, seg[1] - pixel_size, seg[2] + pixel_size*2, seg[3] + pixel_size*2, outline_color)

# Draw tail body
for seg in tail_segments:
    draw_pixel_ellipse(seg[0], seg[1], seg[2], seg[3], body_color)

# Draw flippers with more detail - more paddle-like, realistic shape
# Front left flipper (bottom) - larger, more paddle-shaped
flipper1_x, flipper1_y = base_x + 310, base_y + 140
draw_pixel_ellipse(flipper1_x - pixel_size, flipper1_y - pixel_size, 140 + pixel_size*2, 48 + pixel_size*2, outline_color)
draw_pixel_ellipse(flipper1_x, flipper1_y, 140, 48, body_color)
# Add lighter color on top of flipper
draw_pixel_ellipse(flipper1_x + 10, flipper1_y + 5, 100, 30, belly_color)
# Flipper details (bone structure lines)
for i in range(4):
    draw_pixel_rect(flipper1_x + 30 + i*26, flipper1_y + 34, pixel_size, 20, outline_color)

# Front right flipper (top)
flipper2_x, flipper2_y = base_x + 310, base_y + 2
draw_pixel_ellipse(flipper2_x - pixel_size, flipper2_y - pixel_size, 140 + pixel_size*2, 42 + pixel_size*2, outline_color)
draw_pixel_ellipse(flipper2_x, flipper2_y, 140, 42, body_color)
# Add lighter color
draw_pixel_ellipse(flipper2_x + 10, flipper2_y + 8, 100, 26, belly_color)
# Flipper details
for i in range(4):
    draw_pixel_rect(flipper2_x + 30 + i*26, flipper2_y, pixel_size, 16, outline_color)

# Back left flipper (bottom) - slightly smaller
flipper3_x, flipper3_y = base_x + 580, base_y + 140
draw_pixel_ellipse(flipper3_x - pixel_size, flipper3_y - pixel_size, 120 + pixel_size*2, 42 + pixel_size*2, outline_color)
draw_pixel_ellipse(flipper3_x, flipper3_y, 120, 42, body_color)
# Add lighter color
draw_pixel_ellipse(flipper3_x + 8, flipper3_y + 4, 85, 26, belly_color)
# Flipper details
for i in range(3):
    draw_pixel_rect(flipper3_x + 28 + i*26, flipper3_y + 30, pixel_size, 18, outline_color)

# Back right flipper (top)
flipper4_x, flipper4_y = base_x + 580, base_y + 10
draw_pixel_ellipse(flipper4_x - pixel_size, flipper4_y - pixel_size, 120 + pixel_size*2, 38 + pixel_size*2, outline_color)
draw_pixel_ellipse(flipper4_x, flipper4_y, 120, 38, body_color)
# Add lighter color
draw_pixel_ellipse(flipper4_x + 8, flipper4_y + 6, 85, 24, belly_color)
# Flipper details
for i in range(3):
    draw_pixel_rect(flipper4_x + 28 + i*26, flipper4_y, pixel_size, 14, outline_color)

# Add some texture spots on body - more realistic pattern
spot_color = (50, 120, 170)
spot_positions = [
    (body_x + 110, body_y + 42, 26, 26),
    (body_x + 190, body_y + 52, 32, 32),
    (body_x + 280, body_y + 48, 22, 22),
    (body_x + 240, body_y + 78, 28, 28),
    (body_x + 370, body_y + 60, 24, 24),
    (body_x + 420, body_y + 55, 20, 20),
]

for spot in spot_positions:
    draw_pixel_ellipse(spot[0], spot[1], spot[2], spot[3], spot_color)

# Add some smaller spots for more texture
small_spots = [
    (body_x + 150, body_y + 70, 14, 14),
    (body_x + 320, body_y + 75, 16, 16),
    (body_x + 400, body_y + 80, 14, 14),
]

for spot in small_spots:
    draw_pixel_ellipse(spot[0], spot[1], spot[2], spot[3], spot_color)

# Draw two little people riding on the plesiosaur's back
# Person colors
skin_color = (255, 220, 180)
hair_color_1 = (100, 60, 40)  # Brown hair
hair_color_2 = (40, 40, 40)   # Dark hair
shirt_color_1 = (220, 80, 80)  # Red shirt
shirt_color_2 = (80, 120, 220) # Blue shirt
pants_color_1 = (60, 80, 120)  # Blue pants
pants_color_2 = (80, 100, 60)  # Green pants

# Person 1 - sitting on front part of body
person1_x = body_x + 120
person1_y = body_y - 15

# Person 1 - legs
draw_pixel_rect(person1_x + 8, person1_y + 30, 12, 24, pants_color_1)
draw_pixel_rect(person1_x + 22, person1_y + 30, 12, 24, pants_color_1)
# Person 1 - body/shirt
draw_pixel_rect(person1_x + 6, person1_y + 12, 30, 20, shirt_color_1)
# Person 1 - arms
draw_pixel_rect(person1_x, person1_y + 14, 8, 18, skin_color)
draw_pixel_rect(person1_x + 34, person1_y + 14, 8, 18, skin_color)
# Person 1 - head
draw_pixel_ellipse(person1_x + 10, person1_y, 22, 22, skin_color)
# Person 1 - hair
draw_pixel_ellipse(person1_x + 8, person1_y - 6, 26, 14, hair_color_1)
# Person 1 - eyes
draw_pixel_rect(person1_x + 14, person1_y + 8, 4, 4, (0, 0, 0))
draw_pixel_rect(person1_x + 22, person1_y + 8, 4, 4, (0, 0, 0))
# Person 1 - smile
draw_pixel_rect(person1_x + 14, person1_y + 15, 12, pixel_size, (0, 0, 0))
# Person 1 - outline
draw_pixel_outline(person1_x + 6, person1_y + 12, 30, 20, outline_color, pixel_size)

# Person 2 - sitting on back part of body
person2_x = body_x + 280
person2_y = body_y - 12

# Person 2 - legs
draw_pixel_rect(person2_x + 8, person2_y + 30, 12, 24, pants_color_2)
draw_pixel_rect(person2_x + 22, person2_y + 30, 12, 24, pants_color_2)
# Person 2 - body/shirt
draw_pixel_rect(person2_x + 6, person2_y + 12, 30, 20, shirt_color_2)
# Person 2 - arms (waving)
draw_pixel_rect(person2_x, person2_y + 14, 8, 18, skin_color)
draw_pixel_rect(person2_x + 34, person2_y + 4, 8, 18, skin_color)  # Right arm raised
# Person 2 - head
draw_pixel_ellipse(person2_x + 10, person2_y, 22, 22, skin_color)
# Person 2 - hair
draw_pixel_ellipse(person2_x + 8, person2_y - 6, 26, 14, hair_color_2)
# Person 2 - eyes
draw_pixel_rect(person2_x + 14, person2_y + 8, 4, 4, (0, 0, 0))
draw_pixel_rect(person2_x + 22, person2_y + 8, 4, 4, (0, 0, 0))
# Person 2 - smile
draw_pixel_rect(person2_x + 14, person2_y + 15, 12, pixel_size, (0, 0, 0))
# Person 2 - outline
draw_pixel_outline(person2_x + 6, person2_y + 12, 30, 20, outline_color, pixel_size)

# Ensure pure white background by filling any gaps
# (The background is already white from initialization, this is just to be sure)
# No additional action needed as we started with white background

# Apply pixelation effect to entire image
img = img.resize((width // pixel_size, height // pixel_size), Image.NEAREST)
img = img.resize((width, height), Image.NEAREST)

# Save the image
output_path = 'static/assets/img/background.jpeg'
img.save(output_path, 'JPEG', quality=95)
print(f"Pixel art plesiosaur background saved to {output_path}")
