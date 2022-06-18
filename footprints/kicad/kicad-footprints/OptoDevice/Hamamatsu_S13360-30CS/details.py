###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Hamamatsu_S13360-30CS")

newPart.addTag("kicadDesc", "SiPM, 2pin")
newPart.addTag("kicadTags", "Hamamatsu SiPM")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Hamamatsu_S13360-30CS.wrl")

OOMP.parts.append(newPart)