###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Module")
newPart.addTag("oompIndex", "BeagleBoard_PocketBeagle")

newPart.addTag("kicadDesc", "PocketBeagle, https://github.com/beagleboard/pocketbeagle/wiki/System-Reference-Manual#71_Expansion_Header_Connectors")
newPart.addTag("kicadTags", "PocketBeagle")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Module.3dshapes/BeagleBoard_PocketBeagle.wrl")

OOMP.parts.append(newPart)