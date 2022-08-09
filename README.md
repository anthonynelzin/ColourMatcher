# ColourMatcher

ColourMatcher extracts the dominant hue from an image and returns its name from the following list:

| Hue (LCH) | Hue (HSL) | Name (Goya) |
|:--|:--|:--|
| X | 0.00000 | black |
| 40 | 6.97674 | sienna |
| 60 | 23.11475 | brown |
| 80 | 37.42574 | khaki |
| 100 | 59.18918 | olive |
| 120 | 90.00000 | sage |
| 140 | 120.00000 | jungle |
| 160 | 144.82758 | green |
| 180 | 166.51685 | forest |
| 200 | 187.12871 | lichen |
| 220 | 198.92307 | turquoise |
| 240 | 206.05263 | petrol |
| 260 | 210.36585 | blue |
| 280 | 213.65853 | indigo |
| 300 | 241.26315 | violet |
| 320 | 285.31914 | purple |
| 340 | 314.54545 | zinzolin |
| 0 | 330.61224 | garnet |
| 20 | 342.97297 | tomato |

Those hues stem from an HSL conversion of my “Goya” LCH system of colours, rounded to five decimals. ColourMatcher uses a bisect algorithm to find the closest hue, without caring for saturation/chroma nor lightness. Black is chosen only if the hue is equal to 0.

## Usage

	python3 ColourMatcher.py [-h] [-c CLUSTERS] path
	
By default, ColourMatcher uses *k*-means clustering with four clusters to determine the most common hue. Raising the number of clusters seems to provide more coherent results on multiple passes with high-complexity pictures, at the cost of processing speed and energy expenditure.

## Requirements

- pillow
- sklearn

## Licence

EUPL 1.2