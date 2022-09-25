# ColourMatcher

ColourMatcher extracts the dominant hue from an image and returns its name from the following list:

| Hue (LCH) | Hue (HSL) | Name (Goya) |
|:--|:--|:--|
| X | 0.00000 | black |
| 40 | 9.35779 | brick |
| 60 | 26.89655 | brown |
| 80 | 39.58763 | khaki |
| 100 | 58.40000 | olive |
| 120 | 84.30379 | moss |
| 140 | 129.39759 | forest |
| 160 | 149.64705 | mint |
| 180 | 167.58620 | seafoam |
| 200 | 185.62499 | turquoise |
| 220 | 196.99999 | marine |
| 240 | 203.47825 | cyan |
| 260 | 207.75510 | azure |
| 280 | 211.21621 | indigo |
| 300 | 243.84615 | mauve |
| 320 | 285.78947 | violet |
| 340 | 317.05263 | zinzolin |
| 0 | 333.10345 | garnet |
| 20 | 348.31858 | coral |

Those hues stem from an HSL conversion of my “Goya” LCH system of colours, rounded to five decimals. ColourMatcher uses a bisect algorithm to find the closest hue, without caring for saturation/chroma nor lightness. Black is chosen only if the hue is equal to 0.

## Usage

	python3 ColourMatcher.py [-h] [-c CLUSTERS] path
	
By default, ColourMatcher uses *k*-means clustering with four clusters to determine the most common hue. Raising the number of clusters seems to provide more coherent results on multiple passes with high-complexity pictures, at the cost of processing speed and energy expenditure.

## Requirements

- pillow
- sklearn

## Licence

EUPL 1.2