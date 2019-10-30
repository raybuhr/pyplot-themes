class Colorblind:
    info = {
        "Black": "#000000",
        "Orange": "#E69F00",
        "Sky Blue": "#56B4E9",
        "Bluish Green": "#009E73",
        "Yellow": "#F0E442",
        "Blue": "#0072B2",
        "Vermillion": "#D55E00",
        "Reddish Purple": "#CC79A7",
    }
    colors = list(info.values())


class Solarized:
    dark = [
        "#002b36",
        "#073642",
        "#586e75",
        "#657b83",
        "#839496",
        "#93a1a1",
        "#eee8d5",
        "#fdf6e3",
    ]
    light = dark[::-1]


class PaulTolColorSchemes:
    colors = [
        "#332288",
        "#6699CC",
        "#88CCEE",
        "#44AA99",
        "#117733",
        "#999933",
        "#DDCC77",
        "#661100",
        "#CC6677",
        "#AA4466",
        "#882255",
        "#AA4499",
    ]


class Few:
    light = [
        "#8C8C8C",
        "#88BDE6",
        "#FBB258",
        "#90CD97",
        "#F6AAC9",
        "#BFA554",
        "#BC99C7",
        "#EDDD46",
        "#F07E6E",
    ]
    medium = [
        "#4D4D4D",
        "#5DA5DA",
        "#FAA43A",
        "#60BD68",
        "#F17CB0",
        "#B2912F",
        "#B276B2",
        "#DECF3F",
        "#F15854",
    ]
    dark = [
        "#000000",
        "#265DAB",
        "#DF5C24",
        "#059748",
        "#E5126F",
        "#9D722A",
        "#7B3A96",
        "#C7B42E",
        "#CB2027",
    ]


class FiveThirtyEight:
    colors = ["#008fd5", "#fc4f30", "#e5ae38", "#6d904f", "#8b8b8b", "#810f7c"]


class UCBerkeley:
    """From https://brand.berkeley.edu/colors/"""

    info = [
        {"hex_value": "#003262", "name": "Berkeley blue", "type": "primary"},
        {"hex_value": "#3B7EA1", "name": "Founder’s Rock", "type": "primary"},
        {"hex_value": "#FDB515", "name": "California Gold", "type": "primary"},
        {"hex_value": "#C4820E", "name": "Medalist", "type": "primary"},
        {"hex_value": "#D9661F", "name": "Wellman Tile", "type": "secondary"},
        {"hex_value": "#EE1F60", "name": "Rose Garden", "type": "secondary"},
        {"hex_value": "#ED4E33", "name": "Golden Gate", "type": "secondary"},
        {"hex_value": "#6C3302", "name": "South Hall", "type": "secondary"},
        {"hex_value": "#DDD5C7", "name": "Bay Fog", "type": "secondary"},
        {"hex_value": "#00B0DA", "name": "Lawrence", "type": "secondary"},
        {"hex_value": "#00A598", "name": "Lap Lane", "type": "secondary"},
        {"hex_value": "#46535E", "name": "Pacific", "type": "secondary"},
        {"hex_value": "#B9D3B6", "name": "Sather Gate", "type": "secondary"},
        {"hex_value": "#CFDD45", "name": "Ion", "type": "secondary"},
        {"hex_value": "#859438", "name": "Soybean", "type": "secondary"},
        {"hex_value": "#584F29", "name": "Stone Pine", "type": "secondary"},
    ]
    colors = [d["hex_value"] for d in info]
    primary_colors = [d["hex_value"] for d in info if d["type"] == "primary"]
    secondary_colors = [d["hex_value"] for d in info if d["type"] == "secondary"]


class Autumn1:
    """From https://duoparadigms.com/2013/10/11/10-color-palettes-perfect-autumnfall-season/"""

    colors = ["#D1CEC5", "#997C67", "#755330", "#B0703C", "#DBA72E", "#E3CCA1"]


class Autumn2:
    """From https://duoparadigms.com/2013/10/11/10-color-palettes-perfect-autumnfall-season/"""

    colors = ["#6D7696", "#59484F", "#455C4F", "#CC5543", "#EDB579", "#DBE6AF"]


class Canyon:
    """From https://duoparadigms.com/2013/10/11/10-color-palettes-perfect-autumnfall-season/"""

    colors = ["#6E352C", "#CF5230", "#F59A44", "#E3C598", "#8A6E64", "#6E612F"]


class Chili:
    """From https://duoparadigms.com/2013/10/11/10-color-palettes-perfect-autumnfall-season/"""

    colors = ["#283811", "#66492F", "#B8997F", "#A68887", "#D94330", "#5C0811"]


class Tomato:
    """From https://duoparadigms.com/2013/10/11/10-color-palettes-perfect-autumnfall-season/"""

    colors = ["#D6CFC9", "#C2C290", "#4A572C", "#803018", "#E34819", "#E87F60"]


class Sequential:
    """Color gradients based on a single base color"""
    blues = [
        "#00008b",
        "#302197",
        "#483ba2",
        "#5d54ae",
        "#6f6db9",
        "#7f87c5",
        "#8fa1d0",
        "#9ebcdb",
        "#add8e6",
    ]

    cyans = [
        "#002728",
        "#003d43",
        "#00565a",
        "#007073",
        "#008b8d",
        "#00a6a8",
        "#00c3c4",
        "#00e1e1",
        "#00ffff",
    ]

    greens = [
        "#002100",
        "#003900",
        "#005200",
        "#006c00",
        "#0e880a",
        "#3aa22b",
        "#59bd46",
        "#75d860",
        "#91f479",
    ]

    oranges = [
        "#ffc54e",
        "#ffa122",
        "#f18100",
        "#d56a00",
        "#b95300",
        "#9e3d00",
        "#842600",
        "#6b0a00",
        "#4b0000",
    ]

    purples = [
        "#47004c",
        "#68006a",
        "#880c87",
        "#a02f9e",
        "#b948b6",
        "#d261ce",
        "#ec79e7",
        "#fd98fb",
        "#ffc0ff",
    ]

    reds = [
        "#780000",
        "#940000",
        "#b10000",
        "#cf0000",
        "#ed0000",
        "#ff361d",
        "#ff663f",
        "#ff875a",
        "#ffa473",
    ]


class Diverging:
    """Color palettes with gradients ranging from one color to another"""

    blueorange = [
        "#00008b",
        "#3220c4",
        "#5f4bde",
        "#8278ea",
        "#9ca7ec",
        "#fcbf67",
        "#e68b1e",
        "#c25b01",
        "#963200",
        "#670600",
    ]

    orangeblue = blueorange[::-1]

    bluepurple = [
        "#1f0c97",
        "#5335c4",
        "#845bee",
        "#b889f8",
        "#e4bafd",
        "#fdb2fd",
        "#e37ce2",
        "#be4fbb",
        "#922891",
        "#630065",
    ]

    purpleblue = bluepurple[::-1]

    bluered = [
        "#00008b",
        "#392a9b",
        "#564baa",
        "#6f6db9",
        "#8590c8",
        "#99b3d7",
        "#ff9c96",
        "#fc7463",
        "#ea513d",
        "#d1301f",
        "#b11109",
        "#8b0000",
    ]

    redblue = bluered[::-1]

    greenpurple = [
        "#003b00",
        "#106210",
        "#238c23",
        "#51b64a",
        "#83df76",
        "#fdb2fd",
        "#e37ce2",
        "#be4fbb",
        "#922891",
        "#630065",
    ]

    purplegreen = greenpurple[::-1]

    greenred = [
        "#003b00",
        "#0d5b0d",
        "#1b7e1c",
        "#3aa136",
        "#60c457",
        "#98e48e",
        "#ff9c96",
        "#fc7463",
        "#ea513d",
        "#d1301f",
        "#b11109",
        "#8b0000",
    ]

    redgreen = greenred[::-1]
