###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_Round_D9.0mm")
newPart.addTag("oompName", "kicad-footprints/Diode_THT/Diode_Bridge_Round_D9.0mm")

newPart.addTag("kicadDesc", "4-lead round diode bridge package, diameter 9.0mm, pin pitch 5.0mm, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40r.pdf")
newPart.addTag("kicadTags", "diode bridge 9.0mm 8.85mm WOB pitch 5.0mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_Round_D9.0mm.wrl")

OOMP.parts.append(newPart)