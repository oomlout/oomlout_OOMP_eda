###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SO-4_4.4x2.3mm_P1.27mm")

newPart.addTag("kicadDesc", "4-Lead Plastic Small Outline (SO), see http://datasheet.octopart.com/OPIA403BTRE-Optek-datasheet-5328560.pdf")
newPart.addTag("kicadTags", "SO SOIC 1.27")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-4_4.4x2.3mm_P1.27mm.wrl")

OOMP.parts.append(newPart)