###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_DIP-4_W7.62mm_P5.08mm")

newPart.addTag("kicadDesc", "4-lead dip package for diode bridges, row spacing 7.62 mm (300 mils), see http://cdn-reichelt.de/documents/datenblatt/A400/HDBL101G_20SERIES-TSC.pdf")
newPart.addTag("kicadTags", "DIL DIP PDIP 5.08mm 7.62mm 300mil")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_DIP-4_W7.62mm_P5.08mm.wrl")

OOMP.parts.append(newPart)