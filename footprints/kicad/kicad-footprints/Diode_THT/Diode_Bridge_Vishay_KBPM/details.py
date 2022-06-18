###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_Vishay_KBPM")

newPart.addTag("kicadDesc", "Vishay KBM rectifier package, 3.95mm pitch (http://www.farnell.com/datasheets/2238158.pdf, http://www.cdil.com/s/kbp2005_.pdf)")
newPart.addTag("kicadTags", "Vishay KBM rectifier diode bridge")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_Vishay_KBPM.wrl")

OOMP.parts.append(newPart)