###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "E18-MS1-PCB")

newPart.addTag("kicadDesc", "http://www.cdebyte.com/en/downpdf.aspx?id=122")
newPart.addTag("kicadTags", "Zigbee")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/E18-MS1-PCB.wrl")

OOMP.parts.append(newPart)