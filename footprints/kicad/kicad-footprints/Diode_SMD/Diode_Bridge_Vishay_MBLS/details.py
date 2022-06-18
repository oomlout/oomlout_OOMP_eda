###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "Diode_Bridge_Vishay_MBLS")

newPart.addTag("kicadDesc", "SMD diode bridge MBLS, see http://www.vishay.com/docs/89959/mbl104s.pdf http://www.vishay.com/docs/88854/padlayouts.pdf")
newPart.addTag("kicadTags", "DFS")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Vishay_MBLS.wrl")

OOMP.parts.append(newPart)