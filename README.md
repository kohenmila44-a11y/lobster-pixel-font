🦞 Lobster Pixel Font v1
A minimal, single-line (or 5x3 grid) pixel font for retro-style terminal output, designed with a "crustacean" aesthetic.

Features
5x3 Classic: A tall, readable retro font (5 units high, 3 units wide).
Ultra-Minimal: A single-row symbolic representation for maximum compression.
Emoji-First: Uses the 🦞 emoji as the primary pixel unit.
Installation
The font generator is a self-contained Python package.

# Clone or move into the directory
cd lobster_pixel_font
Usage
CLI
Generate pixel text directly from your terminal:

# Classic 5x3 Style
python3 -m lobster_pixel_font.main "CLAWS"

# Ultra-Minimal Style
python3 -m lobster_pixel_font.main "CRAB" -s ultra
Library
Use it in your own Python scripts:

from lobster_pixel_font.generator import generate_5x3, generate_ultra

print(generate_5x3("HELLO"))
print(generate_ultra("LOBSTER"))
Font System Rules
Height: 5 units (5x3 style)
Width: 3 units (5x3 style)
Pixel: 🦞
Space: 2 empty spaces for grid alignment.
Designed for production use in GameBoy-flavored UIs.
