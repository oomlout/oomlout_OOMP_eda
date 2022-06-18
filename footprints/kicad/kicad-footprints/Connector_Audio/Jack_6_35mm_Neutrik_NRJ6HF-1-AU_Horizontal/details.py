###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_6.35mm_Neutrik_NRJ6HF-1-AU_Horizontal")

newPart.addTag("kicadDesc", "Slim Jacks, 6.35mm (1/4in) stereo jack, switched, gold plated contacts, fully threaded nose, sleeve contact/front panel connection, https://www.neutrik.com/en/product/nrj6hf-1-au")
newPart.addTag("kicadTags", "neutrik jack slim")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NRJ6HF-1-AU_Horizontal.wrl")

OOMP.parts.append(newPart)