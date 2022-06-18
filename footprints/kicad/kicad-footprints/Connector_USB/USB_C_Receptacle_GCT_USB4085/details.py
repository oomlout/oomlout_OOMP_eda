###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_USB")
newPart.addTag("oompIndex", "USB_C_Receptacle_GCT_USB4085")

newPart.addTag("kicadDesc", "USB 2.0 Type C Receptacle, https://gct.co/Files/Drawings/USB4085.pdf")
newPart.addTag("kicadTags", "USB Type-C Receptacle Through-hole Right angle")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Receptacle_GCT_USB4085.wrl")

OOMP.parts.append(newPart)