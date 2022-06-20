###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_Round_D9.8mm")
newPart.addTag("oompName", "kicad-footprints/Diode_THT/Diode_Bridge_Round_D9.8mm")

newPart.addTag("kicadDesc", "4-lead round diode bridge package, diameter 9.8mm, pin pitch 5.08mm, see http://www.vishay.com/docs/88769/woo5g.pdf")
newPart.addTag("kicadTags", "diode bridge 9.8mm WOG pitch 5.08mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_Round_D9.8mm.wrl")

OOMP.parts.append(newPart)