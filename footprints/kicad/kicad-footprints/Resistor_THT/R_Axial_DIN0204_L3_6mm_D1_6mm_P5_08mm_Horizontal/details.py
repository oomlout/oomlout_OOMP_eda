###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal")

newPart.addTag("kicadDesc", "Resistor, Axial_DIN0204 series, Axial, Horizontal, pin pitch=5.08mm, 0.167W, length*diameter=3.6*1.6mm^2, http://cdn-reichelt.de/documents/datenblatt/B400/1_4W%23YAG.pdf")
newPart.addTag("kicadTags", "Resistor Axial_DIN0204 series Axial Horizontal pin pitch 5.08mm 0.167W length 3.6mm diameter 1.6mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal.wrl")

OOMP.parts.append(newPart)