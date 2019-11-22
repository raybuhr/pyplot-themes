
# pyplot-themes
Themes you can see that apply to matplotlib, seaborn, and pandas plots.

This package was inspired by the [`ggthemes` package in R](https://jrnold.github.io/ggthemes/), 
and the code influenced from the [`seaborn` package in python](https://seaborn.pydata.org/) (specifically `rcmod.py`).

## Installing

Install from PyPI

```
pip install pyplot-themes
```

Or directly from GitHub

```
pip install git+https://github.com/raybuhr/pyplot-themes.git
```

## Usage

### Environment 


```python
import sys
sys.version
```




    '3.7.1 (default, Dec 14 2018, 19:28:38) \n[GCC 7.3.0]'




```python
import matplotlib.pyplot as plt
from seaborn import palplot # only used to show off palettes 

from string import ascii_uppercase
import numpy as np


def example_scatter_plot(num_cats=6):
    for i in range(num_cats):
        cat = ascii_uppercase[i]
        x = np.random.random(100)
        y = np.random.random(100) + i
        plt.scatter(x, y, marker='o', label=cat)
    plt.legend(loc='best')


def example_bar_plot(num_cats=6):
    bar_width = 1 / num_cats + 1
    for i in range(num_cats):
        cat = ascii_uppercase[i]
        x = np.arange(11) + 5 * i
        y = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) + np.random.random(1)
        plt.bar(x, y, label=cat, width=bar_width)
    plt.legend(loc='best')


def example_plots(num_cats=6):
    example_scatter_plot(num_cats)
    plt.show()
    example_bar_plot(num_cats)
    plt.show()
```

## Default Matplotlib Theme


```python
example_plots()
```


![png](examples_files/examples_4_0.png)



![png](examples_files/examples_4_1.png)


As you can see, the default theme has good contrast in colors, but leaves a bit to be desired in the sige of the chart (i.e. figure size aka figsize) and font. 

## Usage


```python
import pyplot_themes as themes
themes.__version__
```




    '0.2.2'




```python
themes.theme_minimal()
```

This updates the global theme settings for matplotlib with a nice minimal style using colorblind safe colors.


```python
palplot(themes.palettes.Colorblind.colors)
```


![png](examples_files/examples_10_0.png)



```python
example_plots()
```


![png](examples_files/examples_11_0.png)



![png](examples_files/examples_11_1.png)


As you can see, our plots are much larger now, have accessible colors, and have some light gridlines to make identifying values a bit easier.

There are a few parameters available in all themes:
- grid: toggles grid lines on/off
- ticks: toggles tick marks on/off
- figsize: sets the default size of plots (you can still change each plot in an ad hoc manner if needed)
- fontsize: sets the default font size to be used

Some themes will allow you to pass in whatever colors you want, others you have to pick a color scheme from available options, some only let you reverse the order of the default color palette, and some don't let you mess with the colors at all. Experiment and find out what you like.


```python
themes.theme_minimal(grid=False, ticks=False, fontsize=18)
example_scatter_plot()
plt.title("Look Mom, no lines!")
```




    Text(0.5, 1.0, 'Look Mom, no lines!')




![png](examples_files/examples_14_1.png)


### Themes


```python
themes.theme_dark()
example_plots()
```


![png](examples_files/examples_16_0.png)



![png](examples_files/examples_16_1.png)



```python
themes.theme_tableau()
example_plots()
```


![png](examples_files/examples_17_0.png)



![png](examples_files/examples_17_1.png)



```python
palplot(themes.palettes.Solarized.dark)
```


![png](examples_files/examples_18_0.png)



```python
themes.theme_solarized(scheme="dark")
example_plots()
```


![png](examples_files/examples_19_0.png)



![png](examples_files/examples_19_1.png)



```python
palplot(themes.palettes.Solarized.light)
```


![png](examples_files/examples_20_0.png)



```python
themes.theme_solarized(scheme="light")
example_plots()
```


![png](examples_files/examples_21_0.png)



![png](examples_files/examples_21_1.png)



```python
palplot(themes.palettes.PaulTolColorSchemes.colors)
```


![png](examples_files/examples_22_0.png)



```python
themes.theme_paul_tol()
example_plots(12)
```


![png](examples_files/examples_23_0.png)



![png](examples_files/examples_23_1.png)



```python
themes.theme_paul_tol(reverse_colors=True, grid=False)
example_plots(num_cats=12)
```


![png](examples_files/examples_24_0.png)



![png](examples_files/examples_24_1.png)



```python
palplot(themes.palettes.Few.light)
palplot(themes.palettes.Few.medium)
palplot(themes.palettes.Few.dark)
```


![png](examples_files/examples_25_0.png)



![png](examples_files/examples_25_1.png)



![png](examples_files/examples_25_2.png)



```python
themes.theme_few(scheme="light")
example_plots()
```


![png](examples_files/examples_26_0.png)



![png](examples_files/examples_26_1.png)



```python
themes.theme_few(scheme="medium", figsize=[5, 5])
example_scatter_plot()
```


![png](examples_files/examples_27_0.png)



```python
themes.theme_few(scheme="dark")
example_bar_plot()
```


![png](examples_files/examples_28_0.png)



```python
themes.theme_ucberkeley(figsize=[10, 5])
example_plots(num_cats=4)
```


![png](examples_files/examples_29_0.png)



![png](examples_files/examples_29_1.png)



```python
themes.theme_ucberkeley(scheme="all", figsize=[12, 6])
example_plots(num_cats=16)
```


![png](examples_files/examples_30_0.png)



![png](examples_files/examples_30_1.png)


### Themes that come with matplotlib

These next themes actually come with matplotlib and you can use them without the `pyplot-themes` package.
The functions here are basically thin wrappers for calling the matplotlib defined styles, but use a bigger figsize by default.


```python
themes.theme_fivethirtyeight()
example_plots()
```


![png](examples_files/examples_32_0.png)



![png](examples_files/examples_32_1.png)



```python
themes.theme_ggplot2(figsize=[10, 5])
example_plots()
```


![png](examples_files/examples_33_0.png)



![png](examples_files/examples_33_1.png)


`bmh` stands for Bayesian Methods for Hackers


```python
themes.theme_bmh()
example_scatter_plot()
```


![png](examples_files/examples_35_0.png)


So we also have an alias for the spelled out version to make it easier to discover


```python
themes.theme_bayesian_methods_for_hackers()
example_bar_plot()
```


![png](examples_files/examples_37_0.png)


While this package provides light and dark solarized themes, `matplotlib` comes with a light version as well. This one is a good choice if you want to keep more contrast in the colors of your plots.


```python
themes.theme_solarized_light2()
example_plots()
```


![png](examples_files/examples_39_0.png)



![png](examples_files/examples_39_1.png)


### Modifying Themes

In addition to making it easy to find and call the matplotlib themes, `pyplot-themes` also makes it easier to modify them slightly. For example say you want to use the `ggplot2` theme, but you want to use the Paul Tol Color Schemes palette with it.


```python
themes.theme_ggplot2(palette=themes.palettes.PaulTolColorSchemes.colors, figsize=[12, 6])
example_bar_plot(num_cats=12)
```


![png](examples_files/examples_41_0.png)


Or maybe the `fivethirtyeight` colors


```python
themes.theme_ggplot2(palette=themes.palettes.FiveThirtyEight.colors)
example_bar_plot()
```


![png](examples_files/examples_43_0.png)


### Resetting to back to matplotlib defaults

Of course, sometimes when you are trying out different themes, you may find you modified a setting that you didn't quite like, but aren't sure what changed. To aid in debugging, we created a function to reset the theme back to what matplotlib starts with. Of course, you may just like the matplotlib defaults and that's ok.

Note: The default settings for matplotlib can be slightly different depending on if you are using in python files (e.g. scripts) vs. in jupyter notebooks using `%matplotlib inline`. The reset function assumes you are using a notebook by default, but provides a parameter to toggle that off if you are not:

```python
themes.theme_reset(notebook=False)
```


```python
themes.theme_reset()  # could also use the alias `themes.theme_matplotlib_default()`
example_bar_plot()
```


![png](examples_files/examples_45_0.png)


### Palettes

In addition to the themes above, there are a bunch of color palettes provided. Here are a few to show off.


```python
palplot(themes.palettes.Autumn1.colors)
```


![png](examples_files/examples_47_0.png)



```python
palplot(themes.palettes.Autumn2.colors)
```


![png](examples_files/examples_48_0.png)



```python
palplot(themes.palettes.Canyon.colors)
```


![png](examples_files/examples_49_0.png)



```python
palplot(themes.palettes.Chili.colors)
```


![png](examples_files/examples_50_0.png)



```python
palplot(themes.palettes.Tomato.colors)
```


![png](examples_files/examples_51_0.png)



```python
palplot(themes.palettes.Few.medium)
```


![png](examples_files/examples_52_0.png)



```python
palplot(themes.palettes.FiveThirtyEight.colors)
```


![png](examples_files/examples_53_0.png)



```python
palplot(themes.palettes.Solarized.light)
palplot(themes.palettes.Solarized.dark)
```


![png](examples_files/examples_54_0.png)



![png](examples_files/examples_54_1.png)



```python
palplot(themes.palettes.UCBerkeley.primary_colors)
palplot(themes.palettes.UCBerkeley.secondary_colors)
```


![png](examples_files/examples_55_0.png)



![png](examples_files/examples_55_1.png)


### Sequential Palettes


```python
palplot(themes.palettes.Sequential.blues)
palplot(themes.palettes.Sequential.cyans)
palplot(themes.palettes.Sequential.purples)
```


![png](examples_files/examples_57_0.png)



![png](examples_files/examples_57_1.png)



![png](examples_files/examples_57_2.png)



```python
palplot(themes.palettes.Sequential.greens)
palplot(themes.palettes.Sequential.oranges)
palplot(themes.palettes.Sequential.reds)
```


![png](examples_files/examples_58_0.png)



![png](examples_files/examples_58_1.png)



![png](examples_files/examples_58_2.png)


### Diverging Palettes


```python
palplot(themes.palettes.Diverging.blueorange)
palplot(themes.palettes.Diverging.orangeblue)
```


![png](examples_files/examples_60_0.png)



![png](examples_files/examples_60_1.png)



```python
palplot(themes.palettes.Diverging.bluepurple)
palplot(themes.palettes.Diverging.purpleblue)
```


![png](examples_files/examples_61_0.png)



![png](examples_files/examples_61_1.png)



```python
palplot(themes.palettes.Diverging.bluered)
palplot(themes.palettes.Diverging.redblue)
```


![png](examples_files/examples_62_0.png)



![png](examples_files/examples_62_1.png)



```python
palplot(themes.palettes.Diverging.greenpurple)
palplot(themes.palettes.Diverging.purplegreen)
```


![png](examples_files/examples_63_0.png)



![png](examples_files/examples_63_1.png)



```python
palplot(themes.palettes.Diverging.greenred)
palplot(themes.palettes.Diverging.redgreen)
```


![png](examples_files/examples_64_0.png)



![png](examples_files/examples_64_1.png)


### Using with Pandas


```python
import pandas as pd
```


```python
# some made up date
sales = np.random.randint(low=10, high=20, size=30) * [i**2 for i in range(1, 31)]
revenue = np.random.random(30) * sales
months = pd.date_range(start="2010-01-01", periods=30, freq="M")

df = pd.DataFrame({"sales": sales, "revenue": revenue.round(2)}, index=months)
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sales</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-31</th>
      <td>12</td>
      <td>2.76</td>
    </tr>
    <tr>
      <th>2010-02-28</th>
      <td>52</td>
      <td>45.05</td>
    </tr>
    <tr>
      <th>2010-03-31</th>
      <td>90</td>
      <td>11.80</td>
    </tr>
    <tr>
      <th>2010-04-30</th>
      <td>208</td>
      <td>203.93</td>
    </tr>
    <tr>
      <th>2010-05-31</th>
      <td>475</td>
      <td>337.08</td>
    </tr>
  </tbody>
</table>
</div>




```python
themes.theme_minimal()
df.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdc5285f2b0>




![png](examples_files/examples_69_1.png)



```python
themes.theme_dark(palette=themes.palettes.Autumn1.colors)
df.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fdc5297e668>




![png](examples_files/examples_70_1.png)


## Contributing

There are multiple ways you can help out with this project:

- submit a bug report
- submit a feature request
- Fork this git repo, change some code, and submit a Pull Request
    - adding documentation or examples counts as changing code
