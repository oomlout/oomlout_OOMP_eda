###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_15.1x15.1x6.3mm_P10.9mm")

newPart.addTag("kicadDesc", "Single phase bridge rectifier case 15.1x15.1mm, pitch 10.9mm, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/pb1000.pdf")
newPart.addTag("kicadTags", "Diode Bridge PB10xxS")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_15.1x15.1x6.3mm_P10.9mm.wrl")

OOMP.parts.append(newPart)