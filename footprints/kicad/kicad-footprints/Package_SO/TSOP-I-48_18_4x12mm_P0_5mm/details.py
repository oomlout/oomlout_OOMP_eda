###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TSOP-I-48_18.4x12mm_P0.5mm")

newPart.addTag("kicadDesc", "TSOP I, 32 pins, 18.4x8mm body (https://www.micron.com/~/media/documents/products/technical-note/nor-flash/tn1225_land_pad_design.pdf)")
newPart.addTag("kicadTags", "TSOP I 32")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSOP-I-48_18.4x12mm_P0.5mm.wrl")

OOMP.parts.append(newPart)