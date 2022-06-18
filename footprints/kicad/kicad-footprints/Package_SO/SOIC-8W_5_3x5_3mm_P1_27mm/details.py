###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SOIC-8W_5.3x5.3mm_P1.27mm")

newPart.addTag("kicadDesc", "8-Lead Plastic Small Outline (SM) - 5.28 mm Body [SOIC] (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf)")
newPart.addTag("kicadTags", "SOIC 1.27")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-8W_5.3x5.3mm_P1.27mm.wrl")

OOMP.parts.append(newPart)