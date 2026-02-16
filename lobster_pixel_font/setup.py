from setuptools import setup, find_packages

setup(
    name="lobster-pixel-font",
    version="1.0.0",
    packages=["lobster_pixel_font"],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'lobster-font=lobster_pixel_font.main:main',
        ],
    },
    author="Mila",
    description="A minimal 5x3 pixel font using 🦞 emojis.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/lobster-pixel-font",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
