import colorsys

# RGB to HLS konvertatsiyasi
rgb_color = (0.5, 0.2, 0.8)
hls_color = colorsys.rgb_to_hls(*rgb_color)

print("RGB rangi:", rgb_color)
print("HLS rangi:", hls_color)

# HLS to RGB konvertatsiyasi
new_rgb_color = colorsys.hls_to_rgb(*hls_color)
print("Yangi RGB rangi:", new_rgb_color)
