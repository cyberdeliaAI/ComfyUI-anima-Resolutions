# Anima Resolutions

A small ComfyUI custom node pack for choosing Anima-friendly first-pass image sizes, aligning Impact Pack detailer crops, and scaling images to dimensions that are divisible by a selected multiple.

It does not load a model, change sampler settings, or generate images.

## Features

- **Anima Resolutions**: select a first-pass size and output `resolution`, `width`, and `height` integers
- **Anima Detailer Align Hook**: round Impact Pack detailer sampling sizes up to a multiple, with 32 as the default
- **Anima Image Scale By Multiple**: resize an image and snap both dimensions to a multiple
- **Native Resize Methods**: nearest-exact, bilinear, area, bicubic, and true Lanczos through ComfyUI

## Nodes

### Anima Resolutions

Choose from 1024, 1280, and 1536 resolution presets with common square, portrait, landscape, and cinematic aspect ratios. This node only outputs integers and does not resize an image.

### Anima Detailer Align Hook

Connect `detailer_hook` to the matching input on an Impact Pack detailer node, such as Detailer For Each. The hook rounds the detailer's crop sampling width and height up to the selected alignment. Use `32` for Anima.

This node requires [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack). The other nodes work without Impact Pack.

### Anima Image Scale By Multiple

Scale an `IMAGE` by a chosen factor while keeping the resulting width and height divisible by 8, 16, 32, or 64. The node also outputs the final `width`, `height`, and actual average `applied_scale`. Set `max_long_edge` to `0` for no limit.

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

If your workflow uses the optional 1.5x image scale, the final image will be larger than the selected first-pass size. For example, `1024x1536` becomes `1536x2304`. The scale node snaps the result to the selected multiple when necessary.

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

