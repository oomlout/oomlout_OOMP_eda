###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TerminalBlock_Philmore")
newPart.addTag("oompIndex", "TerminalBlock_Philmore_TB132_1x02_P5.00mm_Horizontal")

newPart.addTag("kicadDesc", "Terminal Block Philmore , 2 pins, pitch 5mm, size 10x10.2mm^2, drill diamater 1.2mm, pad diameter 2.4mm, see http://www.philmore-datak.com/mc/Page%20197.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Philmore")
newPart.addTag("kicadTags", "THT Terminal Block Philmore  pitch 5mm size 10x10.2mm^2 drill 1.2mm pad 2.4mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TerminalBlock_Philmore.3dshapes/TerminalBlock_Philmore_TB132_1x02_P5.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)