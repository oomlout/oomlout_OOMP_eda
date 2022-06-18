###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_SMD")
newPart.addTag("oompIndex", "Relay_2P2T_10x6mm_TE_IMxxG")

newPart.addTag("kicadDesc", "Signal Relay, 10x6mm, 2 Form C, Gull Wings, https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7F108-98001%7FZ.1%7Fpdf%7FEnglish%7FENG_DS_108-98001_Z.1.pdf")
newPart.addTag("kicadTags", "TE IM-Series Relay DPDT Form C")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_2P2T_10x6mm_TE_IMxxG.wrl")

OOMP.parts.append(newPart)