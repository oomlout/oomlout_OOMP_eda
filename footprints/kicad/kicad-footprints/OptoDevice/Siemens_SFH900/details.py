###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Siemens_SFH900")

newPart.addTag("kicadDesc", "package for Siemens SFH900 reflex photo interrupter/coupler/object detector, see https://www.batronix.com/pdf/sfh900.pdf")
newPart.addTag("kicadTags", "Siemens SFH900 reflex photo interrupter coupler object detector")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Siemens_SFH900.wrl")

OOMP.parts.append(newPart)