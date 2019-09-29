from cycler import cycler
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import pyplot_themes.rcmod as rcmod
import pyplot_themes.palettes as palettes


def get_color(color):
    """Helper function to retrieve color hex value by name"""
    # try CSS4 colors
    hex_value = colors.CSS4_COLORS.get(color)
    # try xkcd colors
    if hex_value is None:
        hex_value = colors.XKCD_COLORS.get(f"xkcd:color")
    if hex_value is None:
        print(f"The Color {color} was not found in available colors.")
        raise
    return hex_value


def create_palette(hex_values):
    """Helper function to build a repeating list of colors for matplotlib"""
    return cycler('color', hex_values)


def _theme_minimal():
    """A decent, minimal theme"""
    colorblind = [v for v in palettes.Colorblind.colors]
    light_gray = get_color("lightgray")
    dark_gray = get_color("gray")
    style_dict = {
        "grid.color": light_gray,
        "figure.facecolor": "white",
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.color": dark_gray,
        "ytick.color": dark_gray,
        "text.color": dark_gray,
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


def theme_minimal(palette=None, grid=True, ticks=True, figsize=None):
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
        Sets the figsize for plots, for example ``figsize=[9,6]``.
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    style = rcmod.theme_style(None, palette, grid, ticks, figsize)
    rcmod.set_style(style)


def theme_tableau(grid=True, ticks=True, figsize=None):
    """Theme based on the defaults in Tableau
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``.
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    tableau_colors = [v for v in colors.TABLEAU_COLORS.values()]
    style = rcmod.theme_style(None, tableau_colors, grid, ticks, figsize)
    rcmod.set_style(style)


def theme_solarized(scheme="dark", grid=True, ticks=True, figsize=None):
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
        Sets the figsize for plots, for example ``figsize=[9,6]``.
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
    style.update({
        "figure.facecolor": fig_color,
        "axes.facecolor": fig_color,
        "axes.labelcolor": ax_color,
    })
    rcmod.set_style(style)


def theme_paul_tol(reverse=False, grid=True, ticks=True, figsize=None):
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
        Sets the figsize for plots, for example ``figsize=[9,6]``.
    """
    if figsize is None:
        figsize = [12.0, 8.0]
    pal_colors = palettes.PaulTolColorSchemes.colors
    if reverse:
        pal_colors = pal_colors[::-1]
    style = rcmod.theme_style(None, pal_colors, grid, ticks, figsize)
    rcmod.set_style(style)


def theme_few(scheme="medium", grid=False, ticks=True, figsize=None):
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
        Sets the figsize for plots, for example ``figsize=[9,6]``.
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
    rcmod.set_style(style)


def get_mpl_style_params(style):
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


def theme_fivethirtyeight(grid=None, ticks=None, figsize=None):
    """Use the matplotlib fivethirtyeight style
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``.
    """
    fivethirtyeight_style = get_mpl_style_params("fivethirtyeight")
    style = rcmod.theme_style(fivethirtyeight_style, None, grid, ticks, figsize)
    rcmod.set_style(style)


def theme_ggplot2(palette=None, grid=None, ticks=None, figsize=None):
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
        Sets the figsize for plots, for example ``figsize=[9,6]``.
    """
    ggplot_style = get_mpl_style_params("ggplot")
    style = rcmod.theme_style(ggplot_style, palette, grid, ticks, figsize)
    rcmod.set_style(style)


def theme_solarized_light2(grid=None, ticks=None, figsize=None):
    """Use the matplotlib Solarize_Light2 style
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``.
    """
    sl_style = get_mpl_style_params("Solarize_Light2")
    style = rcmod.theme_style(sl_style, None, grid, ticks, figsize)
    rcmod.set_style(style)

def theme_bmh(palette=None, grid=None, ticks=None, figsize=None):
    """Use the matplotlib bmh style
    Parameters
    ----------
    grid : bool, True
        Toggle gridlines on/off
    axes : bool, True
        Toggle tick marks on/off
    figsize : list or tuple, None
        Sets the figsize for plots, for example ``figsize=[9,6]``.
    """
    bmh_style = get_mpl_style_params("bmh")
    style = rcmod.theme_style(bmh_style, palette, grid, ticks, figsize)
    rcmod.set_style(style)

theme_bayesian_methods_for_hackers = theme_bmh
