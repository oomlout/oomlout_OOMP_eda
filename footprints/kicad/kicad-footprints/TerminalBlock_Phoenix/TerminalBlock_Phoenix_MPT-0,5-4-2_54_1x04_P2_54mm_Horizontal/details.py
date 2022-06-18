###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TerminalBlock_Phoenix")
newPart.addTag("oompIndex", "TerminalBlock_Phoenix_MPT-0,5-4-2.54_1x04_P2.54mm_Horizontal")

newPart.addTag("kicadDesc", "Terminal Block Phoenix MPT-0,5-4-2.54, 4 pins, pitch 2.54mm, size 10.6x6.2mm^2, drill diamater 1.1mm, pad diameter 2.2mm, see http://www.mouser.com/ds/2/324/ItemDetail_1725672-916605.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix")
newPart.addTag("kicadTags", "THT Terminal Block Phoenix MPT-0,5-4-2.54 pitch 2.54mm size 10.6x6.2mm^2 drill 1.1mm pad 2.2mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_MPT-0,5-4-2.54_1x04_P2.54mm_Horizontal.wrl")

OOMP.parts.append(newPart)