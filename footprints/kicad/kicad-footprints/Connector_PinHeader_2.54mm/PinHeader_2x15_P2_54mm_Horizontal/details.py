###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_PinHeader_2.54mm")
newPart.addTag("oompIndex", "PinHeader_2x15_P2.54mm_Horizontal")

newPart.addTag("kicadDesc", "Through hole angled pin header, 2x15, 2.54mm pitch, 6mm pin length, double rows")
newPart.addTag("kicadTags", "Through hole angled pin header THT 2x15 2.54mm double row")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_PinHeader_2.54mm.3dshapes/PinHeader_2x15_P2.54mm_Horizontal.wrl")

OOMP.parts.append(newPart)