###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_6.35mm_Neutrik_NRJ6HF_Horizontal")

newPart.addTag("kicadDesc", "Slim Jacks, 6.35mm (1/4in) stereo jack, switched, fully threaded nose, https://www.neutrik.com/en/product/nrj6hf")
newPart.addTag("kicadTags", "neutrik jack slim")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NRJ6HF_Horizontal.wrl")

OOMP.parts.append(newPart)