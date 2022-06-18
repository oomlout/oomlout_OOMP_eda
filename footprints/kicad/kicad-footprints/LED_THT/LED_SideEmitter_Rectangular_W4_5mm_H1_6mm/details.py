###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_SideEmitter_Rectangular_W4.5mm_H1.6mm")

newPart.addTag("kicadDesc", "LED_SideEmitter_Rectangular, Rectangular, SideEmitter,  Rectangular size 4.5x1.6mm^2, 2 pins, http://cdn-reichelt.de/documents/datenblatt/A500/LED15MMGE_LED15MMGN%23KIN.pdf")
newPart.addTag("kicadTags", "LED_SideEmitter_Rectangular Rectangular SideEmitter  Rectangular size 4.5x1.6mm^2 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_SideEmitter_Rectangular_W4.5mm_H1.6mm.wrl")

OOMP.parts.append(newPart)