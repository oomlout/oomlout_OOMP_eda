###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Resonator-3Pin_W10.0mm_H5.0mm")

newPart.addTag("kicadDesc", "Ceramic Resomator/Filter 10.0x5.0mm^2 RedFrequency MG/MT/MX series, http://www.red-frequency.com/download/datenblatt/redfrequency-datenblatt-ir-zta.pdf, length*width=10.0x5.0mm^2 package, package length=10.0mm, package width=5.0mm, 3 pins")
newPart.addTag("kicadTags", "THT ceramic resonator filter")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator-3Pin_W10.0mm_H5.0mm.wrl")

OOMP.parts.append(newPart)