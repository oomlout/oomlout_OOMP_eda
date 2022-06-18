###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "VSSOP-8_2.4x2.1mm_P0.5mm")

newPart.addTag("kicadDesc", "http://www.ti.com/lit/ml/mpds050d/mpds050d.pdf")
newPart.addTag("kicadTags", "VSSOP DCU R-PDSO-G8 Pitch0.5mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/VSSOP-8_2.4x2.1mm_P0.5mm.wrl")

OOMP.parts.append(newPart)