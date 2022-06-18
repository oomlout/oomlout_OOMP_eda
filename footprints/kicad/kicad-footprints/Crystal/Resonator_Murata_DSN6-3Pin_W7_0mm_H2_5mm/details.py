###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Resonator_Murata_DSN6-3Pin_W7.0mm_H2.5mm")
newPart.addTag("oompName", "kicad-footprints/Crystal/Resonator_Murata_DSN6-3Pin_W7.0mm_H2.5mm")

newPart.addTag("kicadDesc", "Ceramic Resomator/Filter Murata DSN6, http://cdn-reichelt.de/documents/datenblatt/B400/DSN6NC51H.pdf, length*width=7.0x2.5mm^2 package, package length=7.0mm, package width=2.5mm, 3 pins")
newPart.addTag("kicadTags", "THT ceramic resonator filter DSN6")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_Murata_DSN6-3Pin_W7.0mm_H2.5mm.wrl")

OOMP.parts.append(newPart)