###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_speakON_Neutrik_NL8MD-V-1_Vertical")

newPart.addTag("kicadDesc", "speakON Chassis Connectors, 8 pole chassis connector, nickel metal square G-size flange, self tapping screw holes (A-screw), vertical PCB mount, https://www.neutrik.com/en/product/nl8md-v-1")
newPart.addTag("kicadTags", "neutrik speakon")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON_Neutrik_NL8MD-V-1_Vertical.wrl")

OOMP.parts.append(newPart)