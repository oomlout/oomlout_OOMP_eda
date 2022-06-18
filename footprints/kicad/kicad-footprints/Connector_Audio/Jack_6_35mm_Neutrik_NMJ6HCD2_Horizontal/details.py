###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_6.35mm_Neutrik_NMJ6HCD2_Horizontal")

newPart.addTag("kicadDesc", "M Series, 6.35mm (1/4in) stereo jack, switched, with chrome ferrule and straight PCB pins, https://www.neutrik.com/en/product/nmj6hcd2")
newPart.addTag("kicadTags", "neutrik jack m")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NMJ6HCD2_Horizontal.wrl")

OOMP.parts.append(newPart)