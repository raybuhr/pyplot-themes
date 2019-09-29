import warnings
from cycler import cycler
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import pyplot_themes.rcmod as rcmod
import pyplot_themes.palettes as palettes
from matplotlib.cbook.deprecation import MatplotlibDeprecationWarning


def theme_matplotlib_default(notebook=True):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", MatplotlibDeprecationWarning)
        default_rcparams = {k: v for k, v in plt.rcParamsDefault.items()}
        notebook_settings = {
            "figure.dpi": 72.0,
            "figure.edgecolor": (1, 1, 1, 0),
            "figure.facecolor": (1, 1, 1, 0),
            "figure.figsize": [6.0, 4.0],
            "figure.subplot.bottom": 0.125,
            "interactive": True,
        }
        if notebook:
            default_rcparams.update(notebook_settings)
        rcmod.set_style(default_rcparams)


# alias
theme_reset = theme_matplotlib_default


def find_color_hex_value(color="black"):
    """Helper function to retrieve color hex value by name
    Parameters
    ----------
    color : str, black
        The name of the color you find the hex value of, useful for 
        building new color palettes. 
    """
    # try CSS4 colors
    hex_value = colors.CSS4_COLORS.get(color)
    # try xkcd colors
    if hex_value is None:
        hex_value = colors.XKCD_COLORS.get(f"xkcd:{color}")
    if hex_value is None:
        berkeley = {d["name"]: d["hex_value"] for d in palettes.UCBerkeley.info}
        hex_value = berkeley.get(color)
    if hex_value is None:
        print(f"The Color {color} was not found in available colors.")
        raise
    return hex_value


def list_available_colors():
    """Return a dict of all available colors by name and hex value.
    Note that some colors have multiple definitions because... reasons.
    """
    xkcd = {k.strip("xkcd:"): v for k, v in colors.XKCD_COLORS.items()}
    css4 = colors.CSS4_COLORS
    berkeley = {d["name"]: d["hex_value"] for d in palettes.UCBerkeley.info}
    all_colors = {**xkcd, **css4, **berkeley}
    return all_colors


def create_palette(hex_values):
    """Helper function to build a repeating list of colors for matplotlib
    Parameters
    ----------
    hex_values : list or iterable
        A list of hex values for colors to use as a color palette
    Examples
    --------
    >>> 
    """
    return cycler("color", hex_values)


def _theme_minimal():
    """A decent, minimal theme"""
    colorblind = [v for v in palettes.Colorblind.colors]
    light_gray = find_color_hex_value("lightgray")
    dark_gray = find_color_hex_value("gray")
    style_dict = {
        "grid.color": light_gray,
        "figure.facecolor": "white",
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.color": dark_gray,
        "ytick.color": dark_gray,
        "text.color": dark_gray,
        "font.size": 14.0,
        "font.family": ["sans-serif"],
        "font.sans-serif": ["Arial", "DejaVu Sans", "sans-serif"],
        "lines.solid_capstyle": "round",
        "patch.edgecolor": "w",
        "patch.force_edgecolor": True,
        "image.cmap": "rocket",
        "xtick.top": False,
        "ytick.right": False,
        "axes.labelcolor": dark_gray,
        "axes.axisbelow": True,
        "axes.facecolor": "white",
        "axes.edgecolor": light_gray,
        "axes.spines.left": True,
        "axes.spines.bottom": True,
        "axes.spines.right": True,
        "axes.spines.top": True,
        "axes.prop_cycle": create_palette(colorblind),
    }
    return style_dict


def theme_minimal(palette=None, grid=True, ticks=True, figsize=None, fontsize=None):
    """A decent, minimal theme
    Parameters
    ----------
    palette : list, None
        A list of hex values to pass in as a color palette
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    style = rcmod.theme_style(None, palette, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_dark(palette=None, grid=True, ticks=True, figsize=None, fontsize=None):
    """A decent, minimal dark theme
    Parameters
    ----------
    palette : list, None
        A list of hex values to pass in as a color palette
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    style = rcmod.theme_style(None, palette, grid, ticks, figsize)
    dark_style = rcmod.dark_settings()
    if palette is None:
        darkcolorblind = [v for v in palettes.Colorblind.colors][1:]
        dark_style.update({"axes.prop_cycle": create_palette(darkcolorblind)})
    style.update(dark_style)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_tableau(grid=True, ticks=True, figsize=None, fontsize=None):
    """Theme based on the defaults in Tableau
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    tableau_colors = [v for v in colors.TABLEAU_COLORS.values()]
    style = rcmod.theme_style(None, tableau_colors, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_solarized(scheme="dark", grid=True, ticks=True, figsize=None, fontsize=None):
    """Theme based on the defaults in Tableau
    Parameters
    ----------
    scheme : str, dark or light
        Use one of dark or light solarized color schemes
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    if scheme == "dark":
        # want colors to show up, so use opposite
        solarized_colors = palettes.Solarized.light
        fig_color = solarized_colors[-1]
        ax_color = solarized_colors[-2]
        pal_colors = solarized_colors[:-2]
    elif scheme == "light":
        # want colors to show up, so use opposite
        solarized_colors = palettes.Solarized.dark
        fig_color = solarized_colors[-1]
        ax_color = solarized_colors[-2]
        pal_colors = solarized_colors[:-2]
    else:
        print("Scheme must be one of dark or light")
        raise
    style = rcmod.theme_style(None, pal_colors, grid, ticks, figsize)
    style.update(
        {
            "figure.facecolor": fig_color,
            "axes.facecolor": fig_color,
            "axes.labelcolor": ax_color,
        }
    )
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_paul_tol(reverse_colors=False, grid=True, ticks=True, figsize=None, fontsize=None):
    """Theme based on the defaults in Tableau
    Parameters
    ----------
    reverse : bool, False
        Toggle color palette order forward or reverse
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    pal_colors = palettes.PaulTolColorSchemes.colors
    if reverse_colors:
        pal_colors = pal_colors[::-1]
    style = rcmod.theme_style(None, pal_colors, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_few(scheme="medium", grid=False, ticks=True, figsize=None, fontsize=None):
    """Theme based on the ideas of Stephen Few
    Parameters
    ----------
    scheme : str, medium, or dark or light
        Use one of dark or light solarized color schemes
    grid : bool, False
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    if scheme == "medium":
        pal_colors = palettes.Few.medium
    elif scheme == "light":
        pal_colors = palettes.Few.light
    elif scheme == "dark":
        pal_colors = palettes.Few.dark
    else:
        print("Few color scheme must be one of medium, light, or dark.")
        raise
    few_style = {
        "text.color": "black",
        "axes.labelcolor": "black",
        "xtick.color": "black",
        "ytick.color": "black",
    }
    style = rcmod.theme_style(few_style, pal_colors, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_ucberkeley(scheme="primary", grid=False, ticks=True, figsize=None, fontsize=None):
    """Theme based on the brand guidelines of Univeristy of California, Berkeley.
    https://brand.berkeley.edu/

    If you want to use the theme's default font, Open Sans, you may need to 
    download and install it from: https://www.fontsquirrel.com/fonts/open-sans

    Parameters
    ----------
    scheme : str, primary, secondary or all
        Use one of primary, secondary, or all colors in the UC Berkeley palette
    grid : bool, False
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    if scheme == "primary":
        pal_colors = palettes.UCBerkeley.primary_colors
    elif scheme == "secondary":
        pal_colors = palettes.UCBerkeley.secondary_colors
    elif scheme == "all":
        pal_colors = palettes.UCBerkeley.colors
    else:
        print("UCBerkeley color scheme must be one of primary, secondary, or all.")
        raise
    ucb_style = {
        "grid.color": "#EEEEEE",
        "figure.facecolor": "#FFFFFF",
        "text.color": "#003262",
        "axes.labelcolor": "#003262",
        "xtick.color": "#888888",
        "ytick.color": "#888888",
        "axes.edgecolor": "#EEEEEE",
        "axes.spines.left": True,
        "axes.spines.bottom": True,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "font.family": ["sans-serif"],
        "font.sans-serif": ["Open Sans", "DejaVu Sans", "sans-serif"],
        "axes.facecolor": "white",
    }
    style = rcmod.theme_style(ucb_style, pal_colors, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def _get_mpl_style_params(style):
    """Helper function to get the rcParams defined in existing matplotlib styles
    Parameters
    ----------
    style : str, the name of an existing style from matplotlib.pyplot.style.available
    """
    if style not in plt.style.available:
        print(f"Style ``{style}`` is not available")
        raise
    params = {k: v for k, v in plt.style.library.get(style).items()}
    return params


def theme_fivethirtyeight(grid=None, ticks=None, figsize=None, fontsize=None):
    """Use the matplotlib fivethirtyeight style
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    fivethirtyeight_style = _get_mpl_style_params("fivethirtyeight")
    style = rcmod.theme_style(fivethirtyeight_style, None, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_ggplot2(palette=None, grid=None, ticks=None, figsize=None, fontsize=None):
    """Use the matplotlib ggplot style
    Parameters
    ----------
    palette : list, None
        A list of hex values to pass in as a color palette
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    ggplot_style = _get_mpl_style_params("ggplot")
    style = rcmod.theme_style(ggplot_style, palette, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_solarized_light2(grid=None, ticks=None, figsize=None, fontsize=None):
    """Use the matplotlib Solarize_Light2 style
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    sl_style = _get_mpl_style_params("Solarize_Light2")
    style = rcmod.theme_style(sl_style, None, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


def theme_bmh(palette=None, grid=None, ticks=None, figsize=None, fontsize=None):
    """Use the matplotlib bmh style
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``
    fontsize : int or float, None
        Sets the font size for plots, for example ``fontsize=12.5``
    """
    bmh_style = _get_mpl_style_params("bmh")
    style = rcmod.theme_style(bmh_style, palette, grid, ticks, figsize)
    if fontsize is not None:
        style.update({"font.size": fontsize})
    rcmod.set_style(style)


theme_bayesian_methods_for_hackers = theme_bmh
