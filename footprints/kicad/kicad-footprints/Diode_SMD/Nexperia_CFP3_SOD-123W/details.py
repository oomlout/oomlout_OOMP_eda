###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "Nexperia_CFP3_SOD-123W")

newPart.addTag("kicadDesc", "Nexperia CFP3 (SOD-123W), https://assets.nexperia.com/documents/outline-drawing/SOD123W.pdf")
newPart.addTag("kicadTags", "CFP3 SOD-123W")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Nexperia_CFP3_SOD-123W.wrl")

OOMP.parts.append(newPart)