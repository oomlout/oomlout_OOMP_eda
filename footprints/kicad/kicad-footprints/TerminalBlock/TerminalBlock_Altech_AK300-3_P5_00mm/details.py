###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TerminalBlock")
newPart.addTag("oompIndex", "TerminalBlock_Altech_AK300-3_P5.00mm")

newPart.addTag("kicadDesc", "Altech AK300 terminal block, pitch 5.0mm, 45 degree angled, see http://www.mouser.com/ds/2/16/PCBMETRC-24178.pdf")
newPart.addTag("kicadTags", "Altech AK300 terminal block pitch 5.0mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TerminalBlock.3dshapes/TerminalBlock_Altech_AK300-3_P5.00mm.wrl")

OOMP.parts.append(newPart)