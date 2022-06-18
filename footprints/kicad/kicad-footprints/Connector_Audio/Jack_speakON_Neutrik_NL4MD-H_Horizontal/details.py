###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_speakON_Neutrik_NL4MD-H_Horizontal")

newPart.addTag("kicadDesc", "speakON Chassis Connectors, 4 pole chassis connector, grey D-size flange, self tapping screw holes (A-screw), horizontal PCB mount, https://www.neutrik.com/en/product/nl4md-h")
newPart.addTag("kicadTags", "neutrik speakon")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON_Neutrik_NL4MD-H_Horizontal.wrl")

OOMP.parts.append(newPart)