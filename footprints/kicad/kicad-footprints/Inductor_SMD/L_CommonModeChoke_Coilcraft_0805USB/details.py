###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_CommonModeChoke_Coilcraft_0805USB")

newPart.addTag("kicadDesc", "Coilcraft 0805USB Series Common Mode Choke, https://www.coilcraft.com/pdfs/0805usb.pdf")
newPart.addTag("kicadTags", "surface mount common mode bead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_CommonModeChoke_Coilcraft_0805USB.wrl")

OOMP.parts.append(newPart)