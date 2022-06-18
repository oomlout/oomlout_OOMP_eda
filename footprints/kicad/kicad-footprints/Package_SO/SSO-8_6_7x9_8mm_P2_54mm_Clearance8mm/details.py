###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SSO-8_6.7x9.8mm_P2.54mm_Clearance8mm")

newPart.addTag("kicadDesc", "8-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://www.vishay.com/docs/83831/lh1533ab.pdf")
newPart.addTag("kicadTags", "SSO Stretched SO SOIC Pitch 2.54")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSO-8_6.7x9.8mm_P2.54mm_Clearance8mm.wrl")

OOMP.parts.append(newPart)