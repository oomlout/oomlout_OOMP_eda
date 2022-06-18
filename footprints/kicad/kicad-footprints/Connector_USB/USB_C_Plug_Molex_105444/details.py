###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_USB")
newPart.addTag("oompIndex", "USB_C_Plug_Molex_105444")

newPart.addTag("kicadDesc", "Universal Serial Bus (USB) Shielded I/O Plug, Type C, Right Angle, Surface Mount, http://www.molex.com/pdm_docs/sd/1054440001_sd.pdf")
newPart.addTag("kicadTags", "USB Type-C Plug Edge Mount")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Plug_Molex_105444.wrl")

OOMP.parts.append(newPart)