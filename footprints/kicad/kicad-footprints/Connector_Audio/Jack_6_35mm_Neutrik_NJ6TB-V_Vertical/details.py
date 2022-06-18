###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_6.35mm_Neutrik_NJ6TB-V_Vertical")

newPart.addTag("kicadDesc", "6.35mm (1/4 in) Vertical Jack, 3 x switching (normalling) stereo jack  B-gauge type (T/TN/R/RN/S/SN), https://www.neutrik.com/en/product/nj6tb-v")
newPart.addTag("kicadTags", "neutrik jack vertical")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NJ6TB-V_Vertical.wrl")

OOMP.parts.append(newPart)