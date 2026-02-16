# Lobster Pixel Font Generator

from .font_data import FONT_5x3, FONT_ULTRA, PIXEL, SPACE

def generate_5x3(text):
    """Generates the 5x3 tall pixel font."""
    text = text.upper()
    output = ["", "", "", "", ""]
    
    for char in text:
        grid = FONT_5x3.get(char, FONT_5x3[' '])
        for row_idx in range(5):
            row_str = ""
            for val in grid[row_idx]:
                row_str += PIXEL if val == 1 else SPACE
            output[row_idx] += row_str + "  " # Character spacing
            
    return "\n".join(output)

def generate_ultra(text):
    """Generates the ultra-minimal single-line symbolic font."""
    text = text.upper()
    output = []
    
    for char in text:
        symbol = FONT_ULTRA.get(char, " ")
        output.append(symbol)
        
    return " ".join(output)

def print_lobster(text, style='5x3'):
    if style == 'ultra':
        print(generate_ultra(text))
    else:
        print(generate_5x3(text))
