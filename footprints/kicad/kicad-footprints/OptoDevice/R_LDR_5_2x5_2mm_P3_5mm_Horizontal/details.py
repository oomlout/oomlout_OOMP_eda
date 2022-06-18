###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "R_LDR_5.2x5.2mm_P3.5mm_Horizontal")

newPart.addTag("kicadDesc", "Resistor, LDR 5.2x5.2, upright, see http://cdn-reichelt.de/documents/datenblatt/A500/M996011A.pdf")
newPart.addTag("kicadTags", "Resistor LDR5.2x5.2")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/R_LDR_5.2x5.2mm_P3.5mm_Horizontal.wrl")

OOMP.parts.append(newPart)