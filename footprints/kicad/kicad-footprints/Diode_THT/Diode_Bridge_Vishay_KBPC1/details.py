###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_Vishay_KBPC1")

newPart.addTag("kicadDesc", "Single phase bridge rectifier case KBPC1, see http://www.vishay.com/docs/93585/vs-kbpc1series.pdf")
newPart.addTag("kicadTags", "Diode Bridge")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_Vishay_KBPC1.wrl")

OOMP.parts.append(newPart)