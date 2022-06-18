###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "Linear_LGA-133_15.0x15.0mm_Layout12x12_P1.27mm")

newPart.addTag("kicadDesc", "Analog Devices (Linear Tech), 133-pin LGA uModule, 15.0x15.0x4.32mm, https://www.analog.com/media/en/technical-documentation/data-sheets/4637fc.pdf")
newPart.addTag("kicadTags", "133 pin lga")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Linear_LGA-133_15.0x15.0mm_Layout12x12_P1.27mm.wrl")

OOMP.parts.append(newPart)