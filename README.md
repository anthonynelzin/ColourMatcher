# ColourMatcher

ColourMatcher extracts the dominant hue from an image and returns its name from the following list:

| Hue (LCH) | Hue (HSL) | Name (Goya) |
|:--|:--|:--|
| X | 0.00000 | black |
| 40 | 9.81818 | sienna |
| 60 | 28.54838 | brown |
| 80 | 40.57142 | khaki |
| 100 | 58.53658 | olive |
| 120 | 81.62790 | sage |
| 140 | 130.58823 | jungle |
| 160 | 150.96774 | green |
| 180 | 168.51063 | forest |
| 200 | 184.66019 | lichen |
| 220 | 195.59055 | turquoise |
| 240 | 202.60273 | petrol |
| 260 | 206.70967 | blue |
| 280 | 209.99999 | indigo |
| 300 | 245.24999 | violet |
| 320 | 286.40000 | purple |
| 340 | 317.87234 | zinzolin |
| 0 | 334.21052 | garnet |
| 20 | 349.82142 | tomato |

Those hues stem from an HSL conversion of my “Goya” LCH system of colours, rounded to five decimals. ColourMatcher uses a bisect algorithm to find the closest hue, without caring for saturation/chroma nor lightness. Black is chosen only if the hue is equal to 0.

## Usage

	python3 ColourMatcher.py [-h] [-c CLUSTERS] path
	
By default, ColourMatcher uses *k*-means clustering with four clusters to determine the most common hue. Raising the number of clusters seems to provide more coherent results on multiple passes with high-complexity pictures, at the cost of processing speed and energy expenditure.

## Requirements

- pillow
- sklearn

## Licence

EUPL 1.2