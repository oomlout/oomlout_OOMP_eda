###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TerminalBlock_Phoenix")
newPart.addTag("oompIndex", "TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal")

newPart.addTag("kicadDesc", "Terminal Block Phoenix MKDS-1,5-2, 2 pins, pitch 5mm, size 10x9.8mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.farnell.com/datasheets/100425.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix")
newPart.addTag("kicadTags", "THT Terminal Block Phoenix MKDS-1,5-2 pitch 5mm size 10x9.8mm^2 drill 1.3mm pad 2.6mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)