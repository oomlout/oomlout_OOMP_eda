###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_6.35mm_Neutrik_NSJ8HC_Horizontal")

newPart.addTag("kicadDesc", "Stacking Jacks, Mono dual jack, full nose, https://www.neutrik.com/en/product/nsj8hc")
newPart.addTag("kicadTags", "neutrik jack stacking")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NSJ8HC_Horizontal.wrl")

OOMP.parts.append(newPart)