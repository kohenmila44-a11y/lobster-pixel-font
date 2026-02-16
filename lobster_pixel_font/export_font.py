import json
from lobster_pixel_font.font_data import FONT_5x3, FONT_ULTRA

def export_json():
    data = {
        "metadata": {
            "name": "Lobster Pixel Font",
            "version": "1.0.0",
            "author": "Mila",
            "grid": "5x3"
        },
        "glyphs": FONT_5x3,
        "ultra_minimal": FONT_ULTRA
    }
    with open("lobster_font.json", "w") as f:
        json.dump(data, f, indent=4)
    print("🦞 Font exported to lobster_font.json")

if __name__ == "__main__":
    export_json()
