# Generating and Visualizing Data
A set of programs that visualize data obtained from various sources and in different formats.
I used matplotlib to visualize data in a window, and pygal to generate SVG files for interactivity.

## Sample data visuals using SVG files:
- [Probabilities for total sums when rolling two dice](https://github.com/mecosteas/Generating-and-Visualizing-Data/blob/master/visuals/dice_visual.svg) (right click image and open in new tab)
- [Most starred python projects on GitHub](https://github.com/mecosteas/Generating-and-Visualizing-Data/blob/master/visuals/python_repos.svg) (right click image and open in new tab)

## Sample program output:
- Random walks. The green dot is where the walk begins, and the walk ends at the red dot. The initial steps are in the lighter blue color, while the steps closer to the end of the walk are darker blue.

![Image of random walks generated](https://github.com/mecosteas/Generating-and-Visualizing-Data/blob/master/images/random-walks-4.jpg)
- Comparing Death Valley, CA high/low temperatures with Sitka, AK
![Image of temperature comparison between Death Valley, CA and Sitka, AK](https://github.com/mecosteas/Generating-and-Visualizing-Data/blob/master/images/temp_range_comparison.png)
- Average price of avocados by date and region. Each color is a separate region.
![Image of price of avocados](https://github.com/mecosteas/Generating-and-Visualizing-Data/blob/master/images/avocados.png)

## Dependencies:
- pyplot (rw_visual.py, high_lows.py, avocados.py)
- pygal (dice_visual.py, python_repos.py)
- pandas (avocados.py)
- requests (python_repos.py)
