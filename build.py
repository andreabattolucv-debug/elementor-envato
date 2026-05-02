#!/usr/bin/env python3
"""
OHH Italy Landing Page — Build Script
Assembla tutti i moduli in elementor-ready.html

Uso:
  python3 build.py
"""

import os, glob, datetime

MODULES_DIR = os.path.join(os.path.dirname(__file__), 'modules')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'elementor-ready.html')
PREVIEW_FILE = os.path.join(os.path.dirname(__file__), 'index.html')

PREVIEW_WRAP_START = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OHH! Italy — Luxury Italian Travel, Curated for You</title>
</head>
<body>
"""

PREVIEW_WRAP_END = """
</body>
</html>
"""

def build():
    # Get all module files sorted by name
    module_files = sorted(glob.glob(os.path.join(MODULES_DIR, '*.html')))

    if not module_files:
        print("❌ No module files found in /modules/")
        return

    parts = []
    for path in module_files:
        name = os.path.basename(path)
        with open(path) as f:
            content = f.read().strip()
        parts.append(content)
        print(f"  ✓ {name}")

    assembled = '\n\n'.join(parts)

    # Write elementor-ready.html (no html/body wrapper)
    with open(OUTPUT_FILE, 'w') as f:
        f.write(assembled + '\n')
    print(f"\n✅ elementor-ready.html — {len(assembled):,} chars")

    # Write index.html (with html/body wrapper for browser preview)
    with open(PREVIEW_FILE, 'w') as f:
        f.write(PREVIEW_WRAP_START + assembled + PREVIEW_WRAP_END)
    print(f"✅ index.html (preview) — updated")
    print(f"\n🕐 Built at {datetime.datetime.now().strftime('%H:%M:%S')}")

if __name__ == '__main__':
    print("🔨 Building OHH Italy Landing Page...\n")
    build()
