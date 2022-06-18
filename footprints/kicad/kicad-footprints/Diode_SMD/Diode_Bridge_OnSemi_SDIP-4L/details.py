###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "Diode_Bridge_OnSemi_SDIP-4L")

newPart.addTag("kicadDesc", "SMD diode bridge OnSemi SDIP-4L, see https://www.onsemi.com/pdf/datasheet/df10s1-d.pdf")
newPart.addTag("kicadTags", "OnSemi Diode Bridge SDIP-4L")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_OnSemi_SDIP-4L.wrl")

OOMP.parts.append(newPart)