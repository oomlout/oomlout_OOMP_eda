###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "UFBGA-132_7x7mm_P0.5mm")

newPart.addTag("kicadDesc", "UFBGA 132 Pins, 0.5mm Pitch, 0.3mm Ball, http://www.st.com/resource/en/datasheet/stm32l486qg.pdf")
newPart.addTag("kicadTags", "ufbga bga small-pitch")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-132_7x7mm_P0.5mm.wrl")

OOMP.parts.append(newPart)