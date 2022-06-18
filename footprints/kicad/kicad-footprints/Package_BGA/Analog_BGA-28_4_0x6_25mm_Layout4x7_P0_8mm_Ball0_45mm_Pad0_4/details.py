###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Analog_BGA-28_4.0x6.25mm_Layout4x7_P0.8mm_Ball0.45mm_Pad0.4")

newPart.addTag("kicadDesc", "Analog BGA-28 4.0mm x 6.25mm package, pitch 0.4mm pad, based on https://www.analog.com/media/en/technical-documentation/data-sheets/8063fa.pdf")
newPart.addTag("kicadTags", "BGA 28 0.8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Analog_BGA-28_4.0x6.25mm_Layout4x7_P0.8mm_Ball0.45mm_Pad0.4.wrl")

OOMP.parts.append(newPart)