# -*- coding: utf-8 -*-
"""Douyin QR: crop circle+bump, whiten background via border flood fill.

Flood fill from the crop borders recolors the connected navy background to
white; QR strokes are isolated navy islands inside white areas, so they are
never reached. Keeps the top-right bump circle fully intact.
"""
from PIL import Image, ImageDraw

SRC = r'D:/LabWebsite/GBU_Zhao_Lab_Reference/抖音码.png'
OUT = r'D:/LabWebsite/GBU_Zhao_Lab/static/uploads/qr-douyin.png'

orig = Image.open(SRC).convert('RGB')
w, h = orig.size
g = orig.convert('L')
px = g.load()

# --- big circle bbox via brightness profiles -------------------------------
def frac_row(y):
    return sum(1 for x in range(0, w, 2) if px[x, y] > 200) / (w // 2)

rows = [(y, frac_row(y)) for y in range(int(h * 0.08), int(h * 0.62))]
cr = [y for y, f in rows if f > 0.30]
top, bot = min(cr), max(cr)

def frac_col(x):
    return sum(1 for y in range(top, bot + 1, 2) if px[x, y] > 200) / ((bot - top) // 2 + 1)

cc = [x for x in range(0, w) if frac_col(x) > 0.30]
left, right = min(cc), max(cc)
cx, cy = (left + right) // 2, (top + bot) // 2
diam = max(right - left, bot - top)
R = diam / 2.0
print('circle: center', (cx, cy), 'diam', diam)

# --- crop: big circle + bump (measured center (910,418), r~76) + margin ----
PAD = 22
x0 = min(cx - R, 910 - 76) - PAD
x1 = max(cx + R, 910 + 76) + PAD
y0 = min(cy - R, 418 - 76) - PAD
y1 = max(cy + R, 418 + 76) + PAD
side = int(max(x1 - x0, y1 - y0))
ox, oy = int(x0), int(y0)
crop = orig.crop((ox, oy, ox + side, oy + side))
print('crop from', (ox, oy), 'side', side)

# --- flood fill background from borders ------------------------------------
# seed from a grid of border points; thresh tolerant to the navy gradient
bg = crop.copy()
seeds = []
for i in range(0, side, 12):
    seeds += [(i, 0), (i, side - 1), (0, i), (side - 1, i)]
for s in seeds:
    p = bg.getpixel(s)
    # only seed from navy-ish (dark, bluish) pixels
    if max(p) < 130:
        ImageDraw.floodfill(bg, s, (255, 255, 255), thresh=48)

# corner cleanup: round the square into a circle-ish? No - keep square tile;
# any unfilled corner remnants get a second pass with larger thresh
for i in range(0, side, 6):
    for s in [(i, 0), (i, side - 1), (0, i), (side - 1, i)]:
        p = bg.getpixel(s)
        if max(p) < 200:
            ImageDraw.floodfill(bg, s, (255, 255, 255), thresh=90)

bg.save(OUT)
print('saved:', bg.size)

# report: how much of the border is still non-white (should be ~0)
chk = bg.convert('L')
cpx = chk.load()
nonwhite = sum(1 for i in range(0, side, 4)
               for s in [(i, 2), (i, side - 3), (2, i), (side - 3, i)]
               if cpx[s] < 200)
total = len(range(0, side, 4)) * 4
print('border non-white: {}/{} ({:.1f}%)'.format(nonwhite, total, 100 * nonwhite / total))
