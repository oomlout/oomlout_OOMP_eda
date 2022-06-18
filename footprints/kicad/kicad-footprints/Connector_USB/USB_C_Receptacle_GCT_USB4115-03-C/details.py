###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_USB")
newPart.addTag("oompIndex", "USB_C_Receptacle_GCT_USB4115-03-C")

newPart.addTag("kicadDesc", "USB TYPE C, VERT RCPT PCB, SMT, https://gct.co/files/drawings/usb4115.pdf")
newPart.addTag("kicadTags", "USB C Type-C Receptacle SMD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Receptacle_GCT_USB4115-03-C.wrl")

OOMP.parts.append(newPart)