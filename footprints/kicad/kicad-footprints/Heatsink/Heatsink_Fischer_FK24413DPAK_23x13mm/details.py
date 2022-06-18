###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Heatsink")
newPart.addTag("oompIndex", "Heatsink_Fischer_FK24413DPAK_23x13mm")

newPart.addTag("kicadDesc", "23x13 mm SMD heatsink for TO-252 TO-263 TO-268, https://www.fischerelektronik.de/pim/upload/fischerData/cadpdf/base/fk_244_13_d_pak.pdf")
newPart.addTag("kicadTags", "heatsink TO-252 TO-263 TO-268")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Fischer_FK24413DPAK_23x13mm.wrl")

OOMP.parts.append(newPart)