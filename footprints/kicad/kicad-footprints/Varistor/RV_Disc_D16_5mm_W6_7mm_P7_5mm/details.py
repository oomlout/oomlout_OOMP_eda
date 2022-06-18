###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Varistor")
newPart.addTag("oompIndex", "RV_Disc_D16.5mm_W6.7mm_P7.5mm")

newPart.addTag("kicadDesc", "Varistor, diameter 16.5mm, width 6.7mm, pitch 5mm, https://katalog.we-online.de/pbs/datasheet/820542711.pdf")
newPart.addTag("kicadTags", "varistor SIOV")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D16.5mm_W6.7mm_P7.5mm.wrl")

OOMP.parts.append(newPart)