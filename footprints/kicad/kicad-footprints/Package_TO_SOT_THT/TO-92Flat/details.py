###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-92Flat")

newPart.addTag("kicadDesc", "TO-92Flat package, often used for hall sensors, drill 0.75mm (see e.g. http://www.ti.com/lit/ds/symlink/drv5023.pdf)")
newPart.addTag("kicadTags", "to-92Flat hall sensor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-92Flat.wrl")

OOMP.parts.append(newPart)