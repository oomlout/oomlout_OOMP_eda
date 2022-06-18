###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_FFC-FPC")
newPart.addTag("oompIndex", "Molex_502231-3300_1x33-1SH_P0.5mm_Vertical")

newPart.addTag("kicadDesc", "Molex 0.50mm Pitch Easy-On Type FFC/FPC Connector, For LVDS, 6.05mm Height, Vertical, Surface Mount, ZIF, 33 Circuits (https://www.molex.com/pdm_docs/sd/5022313300_sd.pdf)")
newPart.addTag("kicadTags", "molex FFC/FPC connector Pitch 0.5mm vertical")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_502231-3300_1x33-1SH_P0.5mm_Vertical.wrl")

OOMP.parts.append(newPart)