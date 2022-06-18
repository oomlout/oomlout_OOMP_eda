###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_FFC-FPC")
newPart.addTag("oompIndex", "Molex_54548-1071_1x10-1MP_P0.5mm_Horizontal")

newPart.addTag("kicadDesc", "Molex FFC/FPC connector, 10 bottom-side contacts, 0.5mm pitch, 1.2mm height, https://www.molex.com/pdm_docs/sd/545481071_sd.pdf")
newPart.addTag("kicadTags", "FFC FPC connector")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_54548-1071_1x10-1MP_P0.5mm_Horizontal.wrl")

OOMP.parts.append(newPart)