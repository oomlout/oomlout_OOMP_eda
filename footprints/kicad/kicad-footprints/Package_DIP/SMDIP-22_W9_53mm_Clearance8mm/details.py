###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "SMDIP-22_W9.53mm_Clearance8mm")

newPart.addTag("kicadDesc", "22-lead surface-mounted (SMD) DIP package, row spacing 9.53 mm (375 mils), Clearance8mm")
newPart.addTag("kicadTags", "SMD DIP DIL PDIP SMDIP 2.54mm 9.53mm 375mil Clearance8mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/SMDIP-22_W9.53mm.wrl")

OOMP.parts.append(newPart)