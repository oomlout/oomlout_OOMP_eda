###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_19.0x19.0x6.8mm_P12.7mm")

newPart.addTag("kicadDesc", "Single phase bridge rectifier case 19x19mm, pitch 12.7mm, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/pb1000.pdf")
newPart.addTag("kicadTags", "Diode Bridge PB10xx")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_19.0x19.0x6.8mm_P12.7mm.wrl")

OOMP.parts.append(newPart)