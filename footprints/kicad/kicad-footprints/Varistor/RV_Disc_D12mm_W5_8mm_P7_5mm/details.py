###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Varistor")
newPart.addTag("oompIndex", "RV_Disc_D12mm_W5.8mm_P7.5mm")

newPart.addTag("kicadDesc", "Varistor, diameter 12mm, width 5.8mm, pitch 7.5mm")
newPart.addTag("kicadTags", "varistor SIOV")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D12mm_W5.8mm_P7.5mm.wrl")

OOMP.parts.append(newPart)