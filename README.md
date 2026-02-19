# ComfyUI Pad to Multiple

A minimal ComfyUI custom node package that adds one node: **ImagePadToMultiple**.

It pads an image on the **right** and **bottom** only so both width and height are divisible by a selected integer, without resizing, cropping, or stretching.

## Node

- **Name:** `ImagePadToMultiple`
- **Category:** `image/transform`
- **Inputs:**
  - `image` (`IMAGE`)
  - `multiple_of` (`INT`, default `16`, min `1`, max `256`)
  - `pad_color` (`black`, `white`, `gray`)
- **Output:**
  - `image` (`IMAGE`)

## Example

![ImagePadToMultiple example](assets/example.svg)

## Install

Clone this repository into your ComfyUI `custom_nodes` folder and restart ComfyUI.
