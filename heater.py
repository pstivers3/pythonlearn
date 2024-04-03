#!/usr/bin/env python3

cyan = magenta = 300
black = 2

if (cyan > 240 and magenta > 229) or black > 12:
  heater = "maximum"
else:
  heater = "off"
print(heater)

