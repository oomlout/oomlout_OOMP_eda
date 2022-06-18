###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "D_SMA-SMB_Universal_Handsoldering")

newPart.addTag("kicadDesc", "Diode, Universal, SMA (DO-214AC) or SMB (DO-214AA), Handsoldering,")
newPart.addTag("kicadTags", "Diode Universal SMA (DO-214AC) SMB (DO-214AA) Handsoldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_SMB.wrl")

OOMP.parts.append(newPart)