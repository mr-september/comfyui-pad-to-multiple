# ComfyUI Pad to Multiple

A simple ComfyUI custom node that pads images to ensure width and height are multiples of a specified number (e.g., 16, 32, 64). Padding is added only to the right and bottom edges with a configurable solid color.

## Why This Exists

Many AI models (VAEs, UNets, etc.) require input dimensions to be divisible by specific numbers (commonly 8, 16, or 32). This node ensures your images meet those requirements without resizing or cropping, preserving the original content while adding minimal padding.

## Features

- Pads right and bottom edges only (preserves top-left alignment)
- Configurable multiple (1-256, default 16)
- Choice of pad colors: black, white, or gray
- Zero dependencies beyond PyTorch (already in ComfyUI)
