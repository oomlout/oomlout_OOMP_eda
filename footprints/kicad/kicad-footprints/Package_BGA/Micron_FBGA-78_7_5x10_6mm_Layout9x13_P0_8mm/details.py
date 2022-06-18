###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Micron_FBGA-78_7.5x10.6mm_Layout9x13_P0.8mm")

newPart.addTag("kicadDesc", "FBGA-78, 10.6x7.5mm, 78 Ball, 9x13 Layout, 0.8mm Pitch, https://www.micron.com/-/media/client/global/documents/products/data-sheet/dram/ddr3/4gb_ddr3l.pdf#page=24")
newPart.addTag("kicadTags", "BGA 78 0.8")
newPart.addTag("kicadAttr", "smd")

OOMP.parts.append(newPart)