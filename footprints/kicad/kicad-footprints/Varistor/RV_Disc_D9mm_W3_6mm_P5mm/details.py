###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Varistor")
newPart.addTag("oompIndex", "RV_Disc_D9mm_W3.6mm_P5mm")

newPart.addTag("kicadDesc", "Varistor, diameter 9mm, width 3.6mm, pitch 5mm")
newPart.addTag("kicadTags", "varistor SIOV")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D9mm_W3.6mm_P5mm.wrl")

OOMP.parts.append(newPart)