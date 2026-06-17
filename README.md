# Anima Resolutions

A small ComfyUI custom node for choosing Anima-friendly first-pass image sizes. It outputs the selected `resolution`, `width`, and `height` as integers so you can wire them into your workflow.

This plugin is only a resolution picker. It does not load a model, change sampler settings, generate images, or upscale by itself.

## Features

- **Three Resolution Presets**: 1024, 1280, and 1536
- **Dynamic Ratio Selection**: choose from multiple aspect ratios per preset
- **Common Aspect Ratios**: 1:1, 16:9, 9:16, 21:9, 4:3, 3:2, and more
- **Three Integer Outputs**: `resolution`, `width`, and `height`

## Recommended First-Pass Resolutions

For most Anima workflows, start around 1 to 1.6 megapixels for the first pass. Higher resolutions can work, but they are slower and may need more VRAM.

| Size | Best for | Megapixels |
| --- | --- | --- |
| 1024x1024 | square / general use | 1.05 MP |
| 896x1344 | portrait | 1.20 MP |
| 1024x1536 | high portrait | 1.57 MP |
| 1344x896 | landscape | 1.20 MP |
| 1536x1024 | wide landscape | 1.57 MP |
| 1536x864 | cinematic wide | 1.33 MP |

If your workflow uses an optional 1.5x upscale, the final image will be larger than the selected first-pass size. For example, `1024x1536` becomes `1536x2304` after a 1.5x upscale.

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Anima Resolutions"
3. Click Install
4. Restart ComfyUI

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/cyberdeliaAI/ComfyUI-anima-Resolutions.git
   ```

3. Restart ComfyUI


## Available Resolutions

### 1024 Resolution
- 1024x1024 (1:1)
- 1152x896 (9:7)
- 896x1152 (7:9)
- 1152x864 (4:3)
- 864x1152 (3:4)
- 1344x896 (3:2)
- 1248x832 (3:2)
- 896x1344 (2:3)
- 832x1248 (2:3)
- 1280x720 (16:9)
- 720x1280 (9:16)
- 1344x576 (21:9)
- 576x1344 (9:21)

### 1280 Resolution
- 1280x1280 (1:1)
- 1440x1120 (9:7)
- 1120x1440 (7:9)
- 1472x1104 (4:3)
- 1104x1472 (3:4)
- 1536x1024 (3:2)
- 1024x1536 (2:3)
- 1536x864 (16:9)
- 864x1536 (9:16)
- 1680x720 (21:9)
- 720x1680 (9:21)

### 1536 Resolution
- 1536x1536 (1:1)
- 1728x1344 (9:7)
- 1344x1728 (7:9)
- 1728x1296 (4:3)
- 1296x1728 (3:4)
- 1872x1248 (3:2)
- 1248x1872 (2:3)
- 2048x1152 (16:9)
- 1152x2048 (9:16)
- 2016x864 (21:9)
- 864x2016 (9:21)

