#!/usr/bin/env python3

"""
    Anthony Nelzin-Santos
    anthony@nelzin.fr
    https://anthony.nelzin.fr

    European Union Public License 1.2
"""

import argparse
import colorsys
import os
from bisect import bisect_left
from collections import Counter
from PIL import Image
from sklearn.cluster import MiniBatchKMeans

palette = {
    'sienna': 7.27272,
    'brown': 22.49999,
    'khaki': 35.65217,
    'olive': 49.83050,
    'sage': 61.17647,
    'lichen': 87.39130,
    'jungle': 129.54545,
    'green': 162.22222,
    'forest': 173.41463,
    'turquoise': 184.71909,
    'petrol': 193.39805,
    'cerulean': 198.21428,
    'blue': 201.91304,
    'indigo': 223.12499,
    'violet': 259.56522,
    'purple': 278.18182,
    'zinzolin': 315.00000,
    'garnet': 335.40983,
    'tomato': 351.56250,
}

# Get the dominant colour of the image
def get_colour(path, clusters):
    # We’ll work in the RGB mode
    image = Image.open(path)
    image = image.convert("RGB")
    
    # Let’s cluster the colours
    pixels = list(image.getdata())
    cluster = MiniBatchKMeans(n_clusters = clusters)
    labels = cluster.fit_predict(pixels)
    count = Counter(labels)
    
    # Convert the most common RGB cluster into an HSL hue
    r, g, b = cluster.cluster_centers_[count.most_common(1)[0][0]]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    hue = h*360
    
    # Return the dominant hue
    return hue
    
# Get the closest pre-defined colour
# Bisect is faster than min on ordered lists,
# but I could have used this one-liner:
# 
# min(colours, key=lambda x:abs(x-hue))
# 
# Another way of doing it with an ordered list:
#
# closest = colours[0]
# for i in range(1, len(colours)):
#    if abs(colours[i] - hue) < abs(closest - hue):
#        closest = colours[i];
# return closest
def conform_colour(palette, hue):
    colours = list(palette.values())
    position = bisect_left(colours, hue)
    
    if hue == 0.0:
        return "0"
    else: 
        if position == 0:
            return colours[0]
        if position == len(colours):
            return colours[-1]
        
        before = colours[position - 1]
        after = colours[position]
        
        if after - hue < hue - before:
            return after
        else:
            return before
    
# Name the colour
def name_colour(palette, colour):
    if colour == "0":
        name = 'black'
    else:
        name = list(palette.keys())[list(palette.values()).index(colour)]
    
    return name

def main():
    parser = argparse.ArgumentParser(description="Gets the dominant hue from an image and returns its name.")
    parser.add_argument("path", help="Path to the image.")
    parser.add_argument("-c", "--clusters", help="Number of processing clusters.", type=int)
    
    args = parser.parse_args()
    
    if args.clusters:
        clusters = args.clusters
    else:
        clusters = 4

    hue = get_colour(args.path, clusters)
    colour = conform_colour(palette, hue)
    name = name_colour(palette, colour)
    
    print(name)
    
def colourMatcher(path):
    hue = get_colour(path, 4)
    colour = conform_colour(palette, hue)
    name = name_colour(palette, colour)
    
    return name
    
if __name__ == '__main__':
    main()