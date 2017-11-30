#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python ST7735 library for Orange Pi Zero
# 5x7 pixel bitmap font
# Copyright 2016-2017 jackw01 / FuzzyTek
# Distributed under the MIT license

font5x7 = {
    "width": 5,
    "height": 7,
    "linespacing": 4,
    "charspacing": 1
}

# Lower Case

font5x7["a"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 1),
                (0, 1, 1, 1, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 1)
        )
}
font5x7["b"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["c"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["d"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 1),
                (0, 0, 0, 0, 1),
                (0, 1, 1, 1, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["e"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["f"] = {
        "descender": 0,
        "kerning": -1,
        "pixels": (
                (0, 0, 1, 1, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["g"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 1, 1, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 1),
                (0, 0, 0, 0, 1),
                (0, 1, 1, 1, 0)
        )
}
font5x7["h"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["i"] = {
        "descender": 0,
        "kerning": -4,
        "pixels": (
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["j"] = {
        "descender": -2,
        "kerning": -3,
        "pixels": (
                (0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0)
        )
}
font5x7["k"] = {
        "descender": 0,
        "kerning": -1,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 1, 0),
                (1, 0, 1, 0, 0),
                (1, 1, 0, 0, 0),
                (1, 0, 1, 0, 0),
                (1, 0, 0, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["l"] = {
        "descender": 0,
        "kerning": -3,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["m"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 1, 0, 1, 0),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["n"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 1, 1, 0),
                (1, 1, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["o"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["p"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0)
        )
}
font5x7["q"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 1, 1, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 1),
                (0, 0, 0, 0, 1),
                (0, 0, 0, 0, 1)
        )
}
font5x7["r"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 1, 1, 0),
                (1, 1, 0, 0, 1),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["s"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 1, 1, 1),
                (1, 0, 0, 0, 0),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["t"] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["u"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["v"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 1, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["w"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["x"] = {
        "descender": 0,
        "kerning": -1,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 1, 0),
                (1, 0, 0, 1, 0),
                (0, 1, 1, 0, 0),
                (1, 0, 0, 1, 0),
                (1, 0, 0, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["y"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 1, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (1, 1, 0, 0, 0)
        )
}
font5x7["z"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 1, 1, 1, 1),
                (0, 0, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 1, 1, 1, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7[" "] = {
        "descender": 0,
        "kerning": -4,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

# Upper Case

font5x7["A"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 1, 0),
                (0, 1, 0, 1, 0),
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["B"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["C"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["D"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["E"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 1),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["F"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 1),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["G"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 0),
                (1, 0, 1, 1, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["H"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["I"] = {
        "descender": 0,
        "kerning": -4,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["J"] = {
        "descender": 0,
        "kerning": -1,
        "pixels": (
                (0, 0, 0, 1, 0),
                (0, 0, 0, 1, 0),
                (0, 0, 0, 1, 0),
                (0, 0, 0, 1, 0),
                (0, 0, 0, 1, 0),
                (1, 0, 0, 1, 0),
                (0, 1, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["K"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 1, 0),
                (1, 0, 1, 0, 0),
                (1, 1, 0, 0, 0),
                (1, 0, 1, 0, 0),
                (1, 0, 0, 1, 0),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["L"] = {
        "descender": 0,
        "kerning": -1,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["M"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 0, 1, 1),
                (1, 1, 0, 1, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["N"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 1, 0, 0, 1),
                (1, 1, 0, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 0, 1, 1),
                (1, 0, 0, 1, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["O"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["P"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["Q"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 1, 0),
                (0, 0, 0, 0, 1)
        )
}
font5x7["R"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["S"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 0),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["T"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 1),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["U"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["V"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 1, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["W"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 1, 0, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["X"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["Y"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["Z"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 1),
                (0, 0, 0, 0, 1),
                (0, 0, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

# Numbers

font5x7["0"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 1, 1),
                (1, 0, 1, 0, 1),
                (1, 1, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["1"] = {
        "descender": 0,
        "kerning": -3,
        "pixels": (
                (0, 1, 0, 0, 0),
                (1, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["2"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["3"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 1),
                (0, 0, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["4"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 1),
                (0, 0, 0, 1, 1),
                (0, 0, 1, 0, 1),
                (0, 1, 0, 0, 1),
                (1, 1, 1, 1, 1),
                (0, 0, 0, 0, 1),
                (0, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["5"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 1),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (0, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["6"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 1, 1, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["7"] = {
        "descender": 0,
        "kerning": -1,
        "pixels": (
                (1, 1, 1, 1, 0),
                (0, 0, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["8"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}
font5x7["9"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 1),
                (0, 0, 0, 0, 1),
                (0, 0, 0, 1, 0),
                (0, 1, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["."] = {
        "descender": 0,
        "kerning": -4,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["<"] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7[">"] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["@"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 0, 0, 1),
                (1, 0, 1, 0, 1),
                (1, 1, 0, 0, 1),
                (0, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (0, 1, 1, 1, 0)
        )
}

font5x7["#"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 0, 1, 0),
                (1, 1, 1, 1, 1),
                (0, 1, 0, 1, 0),
                (1, 1, 1, 1, 1),
                (0, 1, 0, 1, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["$"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (0, 0, 1, 0, 0),
                (0, 1, 1, 1, 0),
                (1, 0, 1, 0, 1),
                (1, 0, 1, 0, 0),
                (0, 1, 1, 1, 0),
                (0, 0, 1, 0, 1),
                (1, 0, 1, 0, 1),
                (0, 1, 1, 1, 0),
                (0, 0, 1, 0, 0)
        )
}

font5x7["%"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (1, 1, 0, 0, 1),
                (1, 1, 0, 0, 1),
                (0, 0, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 1, 1),
                (1, 0, 0, 1, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["^"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 1, 0, 0),
                (0, 1, 0, 1, 0),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["{"] = {
        "descender": -2,
        "kerning": -2,
        "pixels": (
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 0)
        )
}

font5x7["}"] = {
        "descender": -2,
        "kerning": -2,
        "pixels": (
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0)
        )
}

font5x7["&"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 1, 0, 1),
                (1, 0, 0, 1, 0),
                (0, 1, 1, 0, 1),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["*"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0),
                (1, 0, 1, 0, 1),
                (0, 1, 1, 1, 0),
                (1, 0, 1, 0, 1),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["("] = {
        "descender": -2,
        "kerning": -2,
        "pixels": (
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 0)
        )
}

font5x7[")"] = {
        "descender": -2,
        "kerning": -2,
        "pixels": (
                (1, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0)
        )
}

font5x7["="] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["["] = {
        "descender": -2,
        "kerning": -3,
        "pixels": (
                (1, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 1, 0, 0, 0)
        )
}

font5x7["]"] = {
        "descender": -2,
        "kerning": -3,
        "pixels": (
                (1, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 1, 0, 0, 0)
        )
}

font5x7["|"] = {
        "descender": -2,
        "kerning": -4,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0)
        )
}

font5x7["!"] = {
        "descender": 0,
        "kerning": -4,
        "pixels": (
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["?"] = {
        "descender": 0,
        "kerning": 0,
        "pixels": (
                (0, 1, 1, 1, 0),
                (1, 0, 0, 0, 1),
                (0, 0, 0, 0, 1),
                (0, 0, 0, 1, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7[","] = {
        "descender": -1,
        "kerning": -4,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7[":"] = {
        "descender": 0,
        "kerning": -4,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7[";"] = {
        "descender": 0,
        "kerning": -4,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["+"] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 1, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["-"] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["/"] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 1, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["°"] = {
        "descender": 0,
        "kerning": -2,
        "pixels": (
                (0, 1, 0, 0, 0),
                (1, 0, 1, 0, 0),
                (0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0)
        )
}

font5x7["NULL"] = {
        "descender": -2,
        "kerning": 0,
        "pixels": (
                (1, 1, 1, 1, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 0, 0, 0, 1),
                (1, 1, 1, 1, 1)
        )
}
