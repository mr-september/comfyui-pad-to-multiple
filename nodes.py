import math

import torch
import torch.nn.functional as F


class ImagePadToMultiple:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "multiple_of": ("INT", {"default": 16, "min": 1, "max": 256}),
                "pad_color": (["black", "white", "gray"], {"default": "black"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "pad_to_multiple"
    CATEGORY = "image/transform"

    def pad_to_multiple(self, image, multiple_of, pad_color):
        _, height, width, _ = image.shape
        new_height = math.ceil(height / multiple_of) * multiple_of
        new_width = math.ceil(width / multiple_of) * multiple_of

        pad_bottom = new_height - height
        pad_right = new_width - width

        if pad_bottom == 0 and pad_right == 0:
            return (image,)

        color_values = {
            "black": 0.0,
            "gray": 0.5,
            "white": 1.0,
        }
        fill_value = color_values[pad_color]

        padded = F.pad(image, (0, 0, 0, pad_right, 0, pad_bottom), mode="constant", value=fill_value)
        return (padded,)
