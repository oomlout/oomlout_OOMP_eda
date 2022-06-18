###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_USB")
newPart.addTag("oompIndex", "USB3_Micro-B_Connfly_DS1104-01")

newPart.addTag("kicadDesc", "Micro USB B receptable with flange, bottom-mount, SMD, right-angle (http://en.connfly.com/static/upload/file/pdf/DS1104-01.pdf)")
newPart.addTag("kicadTags", "USB 3.0 Micro B SMD right angle")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB3_Micro-B_Connfly_DS1104-01.wrl")

OOMP.parts.append(newPart)