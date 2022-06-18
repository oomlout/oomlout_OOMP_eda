###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "ST_UFQFPN-20_3x3mm_P0.5mm")

newPart.addTag("kicadDesc", "UFQFPN 20-lead, 3 x 3 mm, 0.5 mm pitch, ultra thin fine pitch quad flat package (http://www.st.com/resource/en/datasheet/stm8s003f3.pdf)")
newPart.addTag("kicadTags", "UFQFPN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/ST_UFQFPN-20_3x3mm_P0.5mm.wrl")

OOMP.parts.append(newPart)