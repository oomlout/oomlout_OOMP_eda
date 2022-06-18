###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Vishay_IFSC-1515AH_4x4x1.8mm")

newPart.addTag("kicadDesc", "Low Profile, High Current Inductors (https://www.vishay.com/docs/34295/sc15ah01.pdf)")
newPart.addTag("kicadTags", "SMD Vishay Inductor Low Profile")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Vishay_IFSC-1515AH_4x4x1.8mm.wrl")

OOMP.parts.append(newPart)