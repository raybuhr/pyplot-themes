import matplotlib as mpl
from pyplot_themes import themes as themes

def grid_style(grid=True):
    """toggle grid on/off"""
    grid_style = {
        "axes.grid": False,
    }
    # Set grid on or off
    if grid:
        grid_style.update({
            "axes.grid": True,
            "grid.linestyle": "-",
        })
    return  grid_style


def axes_ticks_style(ticks=True):
    """toggle axes ticks on/off"""
    ticks_style = {
        "xtick.bottom": False,
        "ytick.left": False,
    }
    # Show or hide the axes ticks
    if ticks:
        ticks_style.update({
            "xtick.bottom": True,
            "ytick.left": True,
        })
    return ticks_style


def theme_style(params=None, palette=None, grid=True, ticks=True, figsize=[12.0, 8.0]):
    """Return a parameter dict for the aesthetic style of the plots.
    This affects things like the color of the axes, whether a grid is
    enabled by default, and other aesthetic elements.
    Parameters
    ----------
    params : dict, None
        A dictionary of parameters, typically provided by calling a theme.
    palette : list, None
        A list of hex values to use as the color palette
    grid : bool, True
        A toggle for whether to use gridlines.
    ticks : bool, True
        A toggle for whether to use tick marks.
    figsize : list or tupe, [12.0, 8.0]
        The width and height of plots, defaults to 12 by 8.
    """
    if isinstance(params, dict):
        style_dict = params
    else:
        style_dict = themes._theme_minimal()

    if palette is not None:
        pal_style = {
            "axes.prop_cycle": themes.create_palette(palette),
        }
        style_dict.update(pal_style)

    if grid is not None:
        grids_params = grid_style(grid=grid)
        style_dict.update(grids_params)

    if ticks is not None:
        tick_params = axes_ticks_style(ticks=ticks)
        style_dict.update(tick_params)

    if figsize is not None:
        style_dict.update({"figure.figsize": figsize})

    return style_dict


def set_style(style_params):
    """Pass a dict of style params to matplotlib
    Paramaters
    ----------
    style_params : dict, style params used to override matplotlib.rcParams
    """
    mpl.rcParams.update(style_params)


def dark_settings():
    # Set the color of the background, spines, and grids
    return {
        "axes.facecolor": "#2E2E30",
        "axes.edgecolor": "#EEEEEE",
        "grid.color": "#EEEEEE",
        "axes.spines.left": True,
        "axes.spines.bottom": True,
        "axes.spines.right": True,
        "axes.spines.top": True,
    }


