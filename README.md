# ColourMatcher

ColourMatcher extracts the dominant hue from an image and returns its name from the following list:

| Hue (OKLCH) | Hue (HSL) | Name (Goya) |
|:--|:--|:--|
| X | 0.00000 | mono |
| 0 | 336.216 | garnet |
| 20 | 355.304 | coral |
| 40 | 18.701 | brick |
| 60 | 26.962 | brown |
| 80 | 35.915 | khaki |
| 100 | 49.000 | olive |
| 120 | 71.455 | moss |
| 140 | 106.667 | forest |
| 160 | 153.171 | mint |
| 180 | 168.96 | seafoam |
| 200 | 184.962 | turquoise |
| 220 | 196.051 | marine |
| 240 | 203.657 | cyan |
| 260 | 217.447 | azure |
| 280 | 240.612 | indigo |
| 300 | 264.742 | mauve |
| 320 | 288.837 | violet |
| 340 | 316.421 | zinzolin |

Those hues stem from an HSL conversion of my “Goya” OKLCH system of colours, rounded to three decimals. ColourMatcher uses a bisect algorithm to find the closest hue, without caring for saturation/chroma nor lightness. Mono is chosen only if the hue is equal to 0.

## Usage

	python3 ColourMatcher.py [-h] [-c CLUSTERS] path
	
By default, ColourMatcher uses *k*-means clustering with four clusters to determine the most common hue. Raising the number of clusters seems to provide more coherent results on multiple passes with high-complexity pictures, at the cost of processing speed and energy expenditure.

## Requirements

- pillow
- sklearn

## Licence

EUPL 1.2