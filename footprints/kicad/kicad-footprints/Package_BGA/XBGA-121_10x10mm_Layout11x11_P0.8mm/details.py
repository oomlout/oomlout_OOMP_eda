###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "XBGA-121_10x10mm_Layout11x11_P0.8mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/XBGA-121_10x10mm_Layout11x11_P0.8mm")

newPart.addTag("kicadDesc", "XBGA-121, 11x11 raster, 10x10mm package, pitch 0.6mm; http://ww1.microchip.com/downloads/en/DeviceDoc/39969b.pdf")
newPart.addTag("kicadTags", "BGA 121 0.8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/XBGA-121_10x10mm_Layout11x11_P0.8mm.wrl")

OOMP.parts.append(newPart)