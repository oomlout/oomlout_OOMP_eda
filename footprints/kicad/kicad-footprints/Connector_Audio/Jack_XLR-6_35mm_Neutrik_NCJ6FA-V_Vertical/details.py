###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR-6.35mm_Neutrik_NCJ6FA-V_Vertical")

newPart.addTag("kicadDesc", "Combo A series, 3 pole XLR female receptacle with 6.35mm (1/4in) stereo jack, vertical PCB mount, https://www.neutrik.com/en/product/ncj6fa-v")
newPart.addTag("kicadTags", "neutrik jack combo a")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR-6.35mm_Neutrik_NCJ6FA-V_Vertical.wrl")

OOMP.parts.append(newPart)