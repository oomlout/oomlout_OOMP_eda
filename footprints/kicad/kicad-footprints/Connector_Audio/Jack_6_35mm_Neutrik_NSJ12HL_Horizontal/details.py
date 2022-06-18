###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_6.35mm_Neutrik_NSJ12HL_Horizontal")

newPart.addTag("kicadDesc", "Stacking Jacks, Stereo dual jack, quick fix nose, https://www.neutrik.com/en/product/nsj12hl")
newPart.addTag("kicadTags", "neutrik jack stacking")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NSJ12HL_Horizontal.wrl")

OOMP.parts.append(newPart)