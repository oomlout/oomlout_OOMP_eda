###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Button_Switch_THT")
newPart.addTag("oompIndex", "KSA_Tactile_SPST")

newPart.addTag("kicadDesc", "KSA http://www.ckswitches.com/media/1457/ksa_ksl.pdf")
newPart.addTag("kicadTags", "SWITCH SMD KSA SW")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/KSA_Tactile_SPST.wrl")

OOMP.parts.append(newPart)