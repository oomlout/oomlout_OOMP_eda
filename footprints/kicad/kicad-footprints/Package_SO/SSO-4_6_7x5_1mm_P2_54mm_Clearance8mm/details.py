###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SSO-4_6.7x5.1mm_P2.54mm_Clearance8mm")

newPart.addTag("kicadDesc", "4-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://www.vishay.com/docs/84299/vor1142b4.pdf")
newPart.addTag("kicadTags", "SSO Stretched SO SOIC 2.54")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSO-4_6.7x5.1mm_P2.54mm_Clearance8mm.wrl")

OOMP.parts.append(newPart)