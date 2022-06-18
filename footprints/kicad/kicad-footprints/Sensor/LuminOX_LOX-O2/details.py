###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor")
newPart.addTag("oompIndex", "LuminOX_LOX-O2")

newPart.addTag("kicadDesc", "SST LuminOX Luminescence-based O2 sensor, https://sstsensing.com/wp-content/uploads/2021/08/DS0030rev15_LuminOx.pdf")
newPart.addTag("kicadTags", "SST LuminOX O2")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/LuminOX_LOX-O2.wrl")

OOMP.parts.append(newPart)