import math

import torch
import torch.nn.functional as F


class ImagePadToMultiple:
    @classmethod
    def INPUT_TYPES(cls):
        directions = ["Top", "Bottom", "Left", "Right", "Left-Right", "Top-Bottom"]
        return {
            "required": {
                "image": ("IMAGE",),
                "multiple_of": ("INT", {"default": 16, "min": 1, "max": 256}),
                "pad_color": (["black", "white", "gray"], {"default": "black"}),
                "direction_1": (directions, {"default": "Bottom"}),
                "direction_2": (directions, {"default": "Right"}),
            }
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT")
    RETURN_NAMES = ("image", "width", "height")
    FUNCTION = "pad_to_multiple"
    CATEGORY = "image/transform"

    def pad_to_multiple(self, image, multiple_of, pad_color, direction_1, direction_2):
        _, height, width, _ = image.shape
        
        total_pad_h = math.ceil(height / multiple_of) * multiple_of - height
        total_pad_w = math.ceil(width / multiple_of) * multiple_of - width

        pad_top = 0
        pad_bottom = 0
        pad_left = 0
        pad_right = 0

        selections = set([direction_1, direction_2])

        horiz_selections = [s for s in selections if s in ("Left", "Right", "Left-Right")]
        if horiz_selections:
            h_targets = set()
            for s in horiz_selections:
                if s == "Left": h_targets.add("left")
                elif s == "Right": h_targets.add("right")
                elif s == "Left-Right": 
                    h_targets.add("left")
                    h_targets.add("right")
            
            if len(h_targets) == 1:
                if "left" in h_targets:
                    pad_left = total_pad_w
                else:
                    pad_right = total_pad_w
            elif len(h_targets) == 2:
                pad_left = total_pad_w // 2
                pad_right = total_pad_w - pad_left

        vert_selections = [s for s in selections if s in ("Top", "Bottom", "Top-Bottom")]
        if vert_selections:
            v_targets = set()
            for s in vert_selections:
                if s == "Top": v_targets.add("top")
                elif s == "Bottom": v_targets.add("bottom")
                elif s == "Top-Bottom": 
                    v_targets.add("top")
                    v_targets.add("bottom")
            
            if len(v_targets) == 1:
                if "top" in v_targets:
                    pad_top = total_pad_h
                else:
                    pad_bottom = total_pad_h
            elif len(v_targets) == 2:
                pad_top = total_pad_h // 2
                pad_bottom = total_pad_h - pad_top

        new_width = width + pad_left + pad_right
        new_height = height + pad_top + pad_bottom

        if pad_top == 0 and pad_bottom == 0 and pad_left == 0 and pad_right == 0:
            return (image, int(new_width), int(new_height))

        color_values = {
            "black": 0.0,
            "gray": 0.5,
            "white": 1.0,
        }
        fill_value = color_values[pad_color]

        padded = F.pad(image, (0, 0, pad_left, pad_right, pad_top, pad_bottom), mode="constant", value=fill_value)
        return (padded, int(new_width), int(new_height))
