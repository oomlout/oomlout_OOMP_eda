###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_32.0x5.6x17.0mm_P10.0mm_P7.5mm")

newPart.addTag("kicadDesc", "Diotec 32x5.6x17mm rectifier package, 7.5mm/10mm pitch, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40c3700.pdf")
newPart.addTag("kicadTags", "Diotec rectifier diode bridge")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_32.0x5.6x17.0mm_P10.0mm_P7.5mm.wrl")

OOMP.parts.append(newPart)