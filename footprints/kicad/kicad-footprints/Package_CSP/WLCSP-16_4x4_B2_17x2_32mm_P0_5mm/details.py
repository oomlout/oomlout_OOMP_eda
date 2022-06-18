###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "WLCSP-16_4x4_B2.17x2.32mm_P0.5mm")

newPart.addTag("kicadDesc", "WLCSP-16, http://www.nxp.com/documents/data_sheet/LPC1102_1104.pdf, http://www.nxp.com/assets/documents/data/en/application-notes/AN3846.pdf")
newPart.addTag("kicadTags", "WLCSP-16 NXP")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-16_4x4_B2.17x2.32mm_P0.5mm.wrl")

OOMP.parts.append(newPart)