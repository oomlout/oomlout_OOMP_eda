###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "Texas_S-PWSON-N10_ThermalVias")

newPart.addTag("kicadDesc", "3x3mm Body, 0.5mm Pitch, S-PWSON-N10, DSC, http://www.ti.com/lit/ds/symlink/tps63060.pdf")
newPart.addTag("kicadTags", "0.5 S-PWSON-N10 DSC")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_S-PWSON-N10.wrl")

OOMP.parts.append(newPart)