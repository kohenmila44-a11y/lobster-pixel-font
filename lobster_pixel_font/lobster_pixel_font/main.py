#!/usr/bin/env python3
import sys
import argparse
from lobster_pixel_font.generator import print_lobster

def main():
    parser = argparse.ArgumentParser(description="🦞 Lobster Pixel Font v1 - CLI Generator")
    parser.add_argument("text", help="The text to convert to lobster pixels")
    parser.add_argument("-s", "--style", choices=["5x3", "ultra"], default="5x3", 
                        help="Font style: '5x3' (tall) or 'ultra' (single-line)")
    
    args = parser.parse_args()
    
    print_lobster(args.text, args.style)

if __name__ == "__main__":
    main()
