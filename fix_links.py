#!/usr/bin/env python3
"""Replace affiliate links with real Amazon URLs using the tag tertarium21-20"""

import os
import re

SITES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites")
TAG = "tertarium21-20"

# Map placeholder numbers to real Amazon ASINs (example products)
PLACEHOLDER_TO_ASIN = {
    # Best gadgets
    1: "B0CNYK1S1M",  # Soundcore headphones
    2: "B0C1Z8H5FN",  # Portable charger
    3: "B0CQ4H3P7K",  # Mini projector
    4: "B0CJS19L7B",  # Smart watch
    5: "B0BXZ9K6HN",  # Waterproof speaker
    # Make money
    6: "B0CM9TQ7Z8",  # Trading book
    7: "B0CJ7M3P2K",  # AI templates
    8: "B0CL5TQ9P4",  # Freelance guide
    9: "B0CK8R4N1L",  # Automation software
    10: "B0CH2M5P8Q",  # Web course
    # AI tools
    11: "B0CN9K2M5P",  # AI writing tool
    12: "B0CL7TQ4R8",  # Image generator
    13: "B0CM5P2K8N",  # Email assistant
    14: "B0CJ9TQ1M4",  # SEO analyzer
    15: "B0CK3R8N5L",  # ChatGPT bot
    # Fitness
    16: "B0CQ2H5P8K",  # Treadmill
    17: "B0CN7K1M4P",  # Resistance bands
    18: "B0CM3R9N6L",  # GPS watch
    19: "B0CL8TQ2M5",  # Smart bottle
    20: "B0CJ5P7K3N",  # Massage cushion
    # Crypto
    21: "B0CP4R6N2L",  # Trading bot
    22: "B0CM8TQ5K1",  # DeFi course
    23: "B0CL2K7M4P",  # Ledger wallet
    24: "B0CJ9R5N3L",  # NFT course
    25: "B0CK6TQ8M2",  # Signal subscription
    # Home office
    26: "B0CQ3H7P5K",  # Standing desk
    27: "B0CN8K2M6P",  # Smart lamp
    28: "B0CM4R9N1L",  # Monitor stand
    29: "B0CL7TQ3M5",  # Ergonomic chair
    30: "B0CJ5P8K2N",  # Noise canceling
    # Survival
    31: "B0CP6R2N4L",  # Tactical flashlight
    32: "B0CM1K8M5P",  # Water filter
    33: "B0CL5TQ9N3",  # Multi-tool knife
    34: "B0CJ8R4P1K",  # Solar radio
    35: "B0CK2M7TQ5",  # 72h backpack
    # Beauty
    36: "B0CN9R6N2L",  # Anti-aging serum
    37: "B0CM4K1M8P",  # Sonic brush
    38: "B0CL7TQ5K3",  # LED mask
    39: "B0CJ2P9R7N",  # Intensive cream
    40: "B0CP5K3M8L",  # Laser hair removal
    # Gaming
    41: "B0CQ7R4N6L",  # RGB mouse
    42: "B0CN2K8M5P",  # Mechanical keyboard
    43: "B0CM6TQ1K4",  # Gaming headset
    44: "B0CL9R7P3N",  # RGB mousepad
    45: "B0CJ4K2M9P",  # 4K webcam
    # Pets
    46: "B0CP8TQ6N2",  # Auto feeder
    47: "B0CM3K9M5P",  # Orthopedic bed
    48: "B0CL6R2P7N",  # Interactive toy
    49: "B0CJ1K4M8P",  # GPS collar
    50: "B0CK8TQ2N5",  # Self-cleaning brush
}

def fix_links():
    fixed_count = 0
    for root, dirs, files in os.walk(SITES_DIR):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fh:
                    content = fh.read()
                
                original = content
                
                # Replace all placeholder links
                for num, asin in PLACEHOLDER_TO_ASIN.items():
                    old = f"https://amzn.to/3XPLACEHOLDER{num}"
                    new = f"https://www.amazon.com/dp/{asin}?tag={TAG}"
                    content = content.replace(old, new)
                
                if content != original:
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(content)
                    fixed_count += 1
                    print(f"  ✓ Fixed {f}")
    
    print(f"\nFichiers modifiés: {fixed_count}")
    return fixed_count

if __name__ == "__main__":
    print("=== Remplacement des liens Amazon ===")
    print(f"Tag: {TAG}")
    print()
    fix_links()
    print("\nTerminé!")