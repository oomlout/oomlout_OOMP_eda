###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR-6.35mm_Neutrik_NCJ5FI-H_Horizontal")

newPart.addTag("kicadDesc", "Combo I series, 3 pole XLR female receptacle with 6.35mm (1/4in) mono jack without switching contact, horizontal PCB mount, retention spring, https://www.neutrik.com/en/product/ncj5fi-h")
newPart.addTag("kicadTags", "neutrik jack combo i")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR-6.35mm_Neutrik_NCJ5FI-H_Horizontal.wrl")

OOMP.parts.append(newPart)