###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Varistor")
newPart.addTag("oompIndex", "RV_Disc_D21.5mm_W8.4mm_P10mm")

newPart.addTag("kicadDesc", "Varistor, diameter 21.5mm, width 8.4mm, pitch 10mm")
newPart.addTag("kicadTags", "varistor SIOV")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D21.5mm_W8.4mm_P10mm.wrl")

OOMP.parts.append(newPart)