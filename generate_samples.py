"""
Benchmark Leaf Image Generator for AgriVision Guard.
Generates realistic, textured synthetic leaf images representing key
pathological conditions from the PlantVillage dataset for rapid demonstration.
"""

import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
from config import SAMPLES_DIR

def create_base_leaf(leaf_type: str, base_color: tuple, size: tuple = (400, 400)) -> Image.Image:
    """Create a textured leaf mask and surface based on crop morphology."""
    w, h = size
    img = Image.new("RGBA", size, (245, 247, 245, 255))
    draw = ImageDraw.Draw(img)
    
    # Background texture
    bg_noise = np.random.normal(0, 3, (h, w, 3)).astype(np.int16)
    
    # Draw leaf contour based on crop
    cx, cy = w // 2, h // 2
    
    if leaf_type == "apple":
        # Ovate leaf with gentle serrations
        points = []
        for angle_deg in range(0, 360, 4):
            rad = math.radians(angle_deg)
            # Oval modulation
            r = 140 * (1.0 - 0.3 * math.sin(rad))
            # Serration ripple
            r += 4 * math.sin(rad * 28)
            x = cx + r * math.cos(rad) * 0.75
            y = cy + r * math.sin(rad) * 1.15
            points.append((x, y))
        draw.polygon(points, fill=base_color)
        
        # Primary Midrib & Secondary Veins
        draw.line([(cx, cy + 150), (cx, cy - 145)], fill=(base_color[0]-15, base_color[1]+20, base_color[2]-15), width=4)
        for y_pos in range(cy - 100, cy + 110, 25):
            draw.line([(cx, y_pos), (cx - 70, y_pos - 25)], fill=(base_color[0]-10, base_color[1]+15, base_color[2]-10), width=2)
            draw.line([(cx, y_pos), (cx + 70, y_pos - 25)], fill=(base_color[0]-10, base_color[1]+15, base_color[2]-10), width=2)
            
    elif leaf_type == "corn":
        # Long blade-like leaf with parallel venation
        points = [
            (cx - 50, cy + 175),
            (cx - 45, cy - 120),
            (cx, cy - 180), # Pointed tip
            (cx + 45, cy - 120),
            (cx + 50, cy + 175)
        ]
        draw.polygon(points, fill=base_color)
        # Strong central midrib and parallel veins
        draw.line([(cx, cy + 175), (cx, cy - 180)], fill=(base_color[0]+25, base_color[1]+35, base_color[2]+15), width=6)
        for offset in [-35, -25, -15, 15, 25, 35]:
            draw.line([(cx + offset, cy + 175), (cx + offset * 0.6, cy - 140)], fill=(base_color[0]+10, base_color[1]+15, base_color[2]+5), width=2)
            
    elif leaf_type == "grape":
        # Broad 5-lobed palmate leaf
        points = []
        for angle_deg in range(0, 360, 3):
            rad = math.radians(angle_deg)
            # 5-lobe harmonic modulation
            r = 135 * (1.0 + 0.28 * math.cos(5 * rad) - 0.15 * math.sin(rad))
            r += 3 * math.sin(rad * 32)
            x = cx + r * math.cos(rad) * 1.05
            y = cy + r * math.sin(rad) * 0.95
            points.append((x, y))
        draw.polygon(points, fill=base_color)
        # Palmate main veins radiating from petiole junction
        p_base = (cx, cy + 90)
        draw.line([p_base, (cx, cy - 140)], fill=(base_color[0]-12, base_color[1]+18, base_color[2]-10), width=4)
        draw.line([p_base, (cx - 120, cy - 60)], fill=(base_color[0]-12, base_color[1]+18, base_color[2]-10), width=3)
        draw.line([p_base, (cx + 120, cy - 60)], fill=(base_color[0]-12, base_color[1]+18, base_color[2]-10), width=3)
        draw.line([p_base, (cx - 95, cy + 40)], fill=(base_color[0]-12, base_color[1]+18, base_color[2]-10), width=3)
        draw.line([p_base, (cx + 95, cy + 40)], fill=(base_color[0]-12, base_color[1]+18, base_color[2]-10), width=3)

    elif leaf_type in ["potato", "tomato"]:
        # Serrated compound leaflet
        points = []
        for angle_deg in range(0, 360, 3):
            rad = math.radians(angle_deg)
            r = 130 * (1.0 - 0.4 * math.sin(rad))
            # Deep serrations for tomato/potato
            r += 8 * math.sin(rad * 22)
            x = cx + r * math.cos(rad) * 0.72
            y = cy + r * math.sin(rad) * 1.18
            points.append((x, y))
        draw.polygon(points, fill=base_color)
        draw.line([(cx, cy + 155), (cx, cy - 155)], fill=(base_color[0]-15, base_color[1]+22, base_color[2]-15), width=4)
        for y_pos in range(cy - 110, cy + 120, 28):
            draw.line([(cx, y_pos), (cx - 65, y_pos - 20)], fill=(base_color[0]-10, base_color[1]+16, base_color[2]-10), width=2)
            draw.line([(cx, y_pos), (cx + 65, y_pos - 20)], fill=(base_color[0]-10, base_color[1]+16, base_color[2]-10), width=2)

    return img.filter(ImageFilter.SMOOTH_MORE)


def add_apple_scab(img: Image.Image) -> Image.Image:
    """Olive-green to velvety dark brown lesions on apple leaf."""
    draw = ImageDraw.Draw(img)
    spots = [(175, 150, 24), (230, 220, 30), (160, 260, 20), (220, 130, 18), (195, 185, 26)]
    for x, y, r in spots:
        # Chlorotic yellow outer border
        draw.ellipse([(x - r - 4, y - r - 4), (x + r + 4, y + r + 4)], fill=(160, 155, 45, 230))
        # Olive/dark brown velvety center
        draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=(55, 52, 28, 245))
        # Textural stippling inside spot
        for _ in range(8):
            dx = np.random.randint(-r//2, r//2)
            dy = np.random.randint(-r//2, r//2)
            draw.point((x + dx, y + dy), fill=(30, 35, 15, 255))
    return img


def add_corn_rust(img: Image.Image) -> Image.Image:
    """Cinnamon-brown to brick-red powdery pustules on corn blade."""
    draw = ImageDraw.Draw(img)
    # Scatter rust pustules along venation
    for _ in range(35):
        x = np.random.randint(170, 230)
        y = np.random.randint(90, 310)
        rx = np.random.randint(3, 6)
        ry = np.random.randint(6, 12) # Elongated along veins
        # Yellow halo
        draw.ellipse([(x - rx - 2, y - ry - 2), (x + rx + 2, y + ry + 2)], fill=(205, 175, 55, 210))
        # Cinnamon-red rust uredinia
        draw.ellipse([(x - rx, y - ry), (x + rx, y + ry)], fill=(175, 65, 25, 250))
    return img


def add_corn_northern_blight(img: Image.Image) -> Image.Image:
    """Long, cigar-shaped tan lesions on corn blade."""
    draw = ImageDraw.Draw(img)
    lesions = [(185, 160, 16, 55), (210, 245, 18, 65), (195, 100, 12, 40)]
    for x, y, rx, ry in lesions:
        # Chlorotic border
        draw.ellipse([(x - rx - 3, y - ry - 3), (x + rx + 3, y + ry + 3)], fill=(190, 170, 60, 220))
        # Tan/grayish cigar lesion center
        draw.ellipse([(x - rx, y - ry), (x + rx, y + ry)], fill=(145, 130, 95, 240))
        # Darker concentric ring
        draw.ellipse([(x - rx//2, y - ry//2), (x + rx//2, y + ry//2)], outline=(110, 90, 60, 255), width=2)
    return img


def add_grape_black_rot(img: Image.Image) -> Image.Image:
    """Circular reddish-brown spots with dark margins and tiny black pycnidia."""
    draw = ImageDraw.Draw(img)
    spots = [(160, 160, 22), (240, 180, 26), (180, 240, 20), (225, 260, 18), (140, 210, 15)]
    for x, y, r in spots:
        # Dark brown border
        draw.ellipse([(x - r - 2, y - r - 2), (x + r + 2, y + r + 2)], fill=(65, 30, 20, 240))
        # Reddish-brown interior
        draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=(145, 75, 45, 245))
        # Tiny black pycnidia pimples
        for _ in range(6):
            px = x + np.random.randint(-r+5, r-5)
            py = y + np.random.randint(-r+5, r-5)
            draw.ellipse([(px-2, py-2), (px+2, py+2)], fill=(20, 15, 15, 255))
    return img


def add_grape_esca(img: Image.Image) -> Image.Image:
    """Striking 'tiger-stripe' interveinal chlorosis and necrosis."""
    draw = ImageDraw.Draw(img)
    # Interveinal chlorotic yellow bands
    stripes = [
        [(150, 140), (130, 170), (110, 190)],
        [(250, 140), (270, 170), (290, 190)],
        [(180, 120), (170, 90), (160, 70)],
        [(220, 120), (230, 90), (240, 70)],
        [(160, 220), (140, 250), (120, 270)]
    ]
    for band in stripes:
        # Bright yellow halo
        draw.line(band, fill=(210, 190, 45, 210), width=18)
        # Reddish-brown necrotic core
        draw.line(band, fill=(130, 50, 30, 240), width=8)
    return img


def add_early_blight_targets(img: Image.Image) -> Image.Image:
    """Distinct concentric bullseye target rings on potato or tomato leaf."""
    draw = ImageDraw.Draw(img)
    spots = [(170, 160, 32), (235, 225, 28), (150, 250, 22), (230, 140, 19)]
    for x, y, r in spots:
        # Yellow chlorotic margin
        draw.ellipse([(x - r - 6, y - r - 6), (x + r + 6, y + r + 6)], fill=(205, 190, 50, 220))
        # Outer dark brown lesion
        draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=(85, 55, 35, 245))
        # Concentric rings
        draw.ellipse([(x - int(r*0.75), y - int(r*0.75)), (x + int(r*0.75), y + int(r*0.75))], outline=(60, 35, 20, 255), width=2)
        draw.ellipse([(x - int(r*0.5), y - int(r*0.5)), (x + int(r*0.5), y + int(r*0.5))], fill=(95, 65, 40, 255))
        draw.ellipse([(x - int(r*0.25), y - int(r*0.25)), (x + int(r*0.25), y + int(r*0.25))], outline=(45, 25, 15, 255), width=2)
    return img


def add_late_blight_water_soaked(img: Image.Image) -> Image.Image:
    """Large expanding water-soaked dark olive to black greasy lesions."""
    draw = ImageDraw.Draw(img)
    lesions = [(160, 140, 45, 38), (230, 210, 52, 42), (180, 270, 38, 30)]
    for x, y, rx, ry in lesions:
        # Pale yellow-green water-soaked rim
        draw.ellipse([(x - rx - 8, y - ry - 8), (x + rx + 8, y + ry + 8)], fill=(140, 160, 80, 210))
        # Dark brown/black decayed core
        draw.ellipse([(x - rx, y - ry), (x + rx, y + ry)], fill=(45, 40, 30, 245))
        # Delicate white mold border trace (sporangia)
        draw.ellipse([(x - rx + 3, y - ry + 3), (x + rx - 3, y + ry - 3)], outline=(225, 230, 220, 180), width=2)
    return img


def add_tomato_bacterial_spot(img: Image.Image) -> Image.Image:
    """Small dark circular spots with prominent yellow halos."""
    draw = ImageDraw.Draw(img)
    for _ in range(40):
        x = np.random.randint(145, 255)
        y = np.random.randint(110, 290)
        r = np.random.randint(3, 7)
        # Yellow halo
        draw.ellipse([(x - r - 3, y - r - 3), (x + r + 3, y + r + 3)], fill=(215, 200, 40, 230))
        # Black/dark brown spot center
        draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=(35, 25, 20, 255))
    return img


def add_tomato_yellow_curl(img: Image.Image) -> Image.Image:
    """Upward curling leaf margins and severe bright yellow chlorosis."""
    draw = ImageDraw.Draw(img)
    # Severe yellow chlorotic wash across margins
    draw.polygon([(140, 120), (120, 220), (145, 300), (190, 220)], fill=(215, 210, 60, 140))
    draw.polygon([(260, 120), (280, 220), (255, 300), (210, 220)], fill=(215, 210, 60, 140))
    # Curled edge folds
    draw.line([(125, 140), (135, 240)], fill=(160, 150, 40, 230), width=4)
    draw.line([(275, 140), (265, 240)], fill=(160, 150, 40, 230), width=4)
    return img


def generate_all_samples():
    """Build and save benchmark sample images for all 5 crops."""
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Healthy leaf colors
    apple_green = (65, 138, 55)
    corn_green = (75, 155, 60)
    grape_green = (55, 145, 65)
    potato_green = (50, 125, 50)
    tomato_green = (58, 135, 52)
    
    samples_map = {
        # Apple
        "apple_scab.jpg": lambda: add_apple_scab(create_base_leaf("apple", (70, 130, 60))),
        "apple_healthy.jpg": lambda: create_base_leaf("apple", apple_green),
        
        # Corn
        "corn_common_rust.jpg": lambda: add_corn_rust(create_base_leaf("corn", (80, 145, 65))),
        "corn_northern_leaf_blight.jpg": lambda: add_corn_northern_blight(create_base_leaf("corn", (85, 140, 60))),
        "corn_healthy.jpg": lambda: create_base_leaf("corn", corn_green),
        
        # Grape
        "grape_black_rot.jpg": lambda: add_grape_black_rot(create_base_leaf("grape", (60, 135, 65))),
        "grape_esca.jpg": lambda: add_grape_esca(create_base_leaf("grape", (65, 140, 60))),
        "grape_healthy.jpg": lambda: create_base_leaf("grape", grape_green),
        
        # Potato
        "potato_early_blight.jpg": lambda: add_early_blight_targets(create_base_leaf("potato", (60, 125, 55))),
        "potato_late_blight.jpg": lambda: add_late_blight_water_soaked(create_base_leaf("potato", (55, 120, 50))),
        "potato_healthy.jpg": lambda: create_base_leaf("potato", potato_green),
        
        # Tomato
        "tomato_bacterial_spot.jpg": lambda: add_tomato_bacterial_spot(create_base_leaf("tomato", (65, 130, 55))),
        "tomato_early_blight.jpg": lambda: add_early_blight_targets(create_base_leaf("tomato", (60, 130, 50))),
        "tomato_late_blight.jpg": lambda: add_late_blight_water_soaked(create_base_leaf("tomato", (55, 120, 48))),
        "tomato_yellow_leaf_curl.jpg": lambda: add_tomato_yellow_curl(create_base_leaf("tomato", (95, 145, 50))),
        "tomato_healthy.jpg": lambda: create_base_leaf("tomato", tomato_green),
    }
    
    print("[SampleGenerator] Generating 15 curated benchmark images...")
    for filename, generator_func in samples_map.items():
        img = generator_func()
        # Convert RGBA to RGB for standard JPEG
        rgb_img = Image.new("RGB", img.size, (245, 248, 245))
        rgb_img.paste(img, mask=img.split()[3])
        save_path = SAMPLES_DIR / filename
        rgb_img.save(save_path, "JPEG", quality=92)
        print(f"  + Generated: {filename} ({save_path.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    generate_all_samples()
