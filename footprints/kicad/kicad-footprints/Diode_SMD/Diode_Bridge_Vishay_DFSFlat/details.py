###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "Diode_Bridge_Vishay_DFSFlat")

newPart.addTag("kicadDesc", "SMD diode bridge Low Profile DFS \"Flat\", see http://www.vishay.com/docs/88874/dfl15005.pdf")
newPart.addTag("kicadTags", "DFS")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Vishay_DFSFlat.wrl")

OOMP.parts.append(newPart)