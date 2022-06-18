###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_speakON_Neutrik_NLT4MD-V_Vertical")

newPart.addTag("kicadDesc", "STX Series, 4 pole male chassis connector, metal housing, vertical PCB mount,  self tapping screw holes (A-screw), https://www.neutrik.com/en/product/nlt4md-v")
newPart.addTag("kicadTags", "neutrik speakon stx")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_speakON_Neutrik_NLT4MD-V_Vertical.wrl")

OOMP.parts.append(newPart)