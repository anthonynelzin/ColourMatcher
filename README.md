# ColourMatcher

ColourMatcher extracts the dominant hue from an image and returns its name from the following list:

| Hue | Name |
|:--|:--|
| 0.00000 | black |
| 7.27272 | sienna |
| 22.49999 | brown |
| 35.65217 | khaki |
| 49.83050 | olive |
| 61.17647 | sage |
| 87.39130 | lichen |
| 129.54545 | jungle |
| 162.22222 | green |
| 173.41463 | forest |
| 184.71909 | turquoise |
| 193.39805 | petrol |
| 198.21428 | cerulean |
| 201.91304 | blue |
| 223.12499 | indigo |
| 259.56522 | violet |
| 278.18182 | purple |
| 315.00000 | zinzolin |
| 335.40983 | garnet |
| 351.56250 | tomato |

Those hues stem from an HSL conversion of my “Goya” LCH system of colours, rounded to five decimals. ColourMatcher uses a bisect algorithm to find the closest hue, without caring for saturation/chroma nor lightness. Black is chosen only if the hue is equal to 0.

## Usage

	python3 ColourMatcher.py [-h] [-c CLUSTERS] path
	
By default, ColourMatcher uses *k*-means clustering with four clusters to determine the most common hue. Raising the number of clusters seems to provide more coherent results on multiple passes with high-complexity pictures, at the cost of processing speed and energy expenditure.

## Requirements

- pillow
- sklearn

## Licence

EUPL 1.2