###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_15.2x15.2x6.3mm_P10.9mm")
newPart.addTag("oompName", "kicad-footprints/Diode_THT/Diode_Bridge_15.2x15.2x6.3mm_P10.9mm")

newPart.addTag("kicadDesc", "Single phase bridge rectifier case 15.2x15.2mm, pitch 10.9mm, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/kbpc600.pdf")
newPart.addTag("kicadTags", "Diode Bridge KBPC6xx")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_15.2x15.2x6.3mm_P10.9mm.wrl")

OOMP.parts.append(newPart)