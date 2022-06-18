###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_FFC-FPC")
newPart.addTag("oompIndex", "Molex_54132-5033_1x50-1MP_P0.5mm_Horizontal")

newPart.addTag("kicadDesc", "Molex FFC/FPC connector, 50 bottom-side contacts, 0.5mm pitch, 2.0mm height, https://www.molex.com/pdm_docs/sd/541325033_sd.pdf")
newPart.addTag("kicadTags", "FFC FPC")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_54132-5033_1x50-1MP_P0.5mm_Horizontal.wrl")

OOMP.parts.append(newPart)