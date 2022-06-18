###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_Vishay_KBL")

newPart.addTag("kicadDesc", "Vishay KBL rectifier package, 5.08mm pitch, see http://www.vishay.com/docs/88655/kbl005.pdf")
newPart.addTag("kicadTags", "Vishay KBL rectifier diode bridge")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_Vishay_KBL.wrl")

OOMP.parts.append(newPart)