###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Everlight_ITR8307")

newPart.addTag("kicadDesc", "package for Everlight ITR8307 with PCB cutout, light-direction upwards, see http://www.everlight.com/file/ProductFile/ITR8307.pdf")
newPart.addTag("kicadTags", "refective opto couple photo coupler")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Everlight_ITR8307.wrl")

OOMP.parts.append(newPart)