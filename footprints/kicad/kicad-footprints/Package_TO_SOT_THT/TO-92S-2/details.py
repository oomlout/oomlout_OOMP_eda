###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-92S-2")

newPart.addTag("kicadDesc", "TO-92S package, 2-pin, drill 0.75mm (https://www.diodes.com/assets/Package-Files/TO92S%20(Type%20B).pdf)")
newPart.addTag("kicadTags", "to-92S transistor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-92S-2.wrl")

OOMP.parts.append(newPart)