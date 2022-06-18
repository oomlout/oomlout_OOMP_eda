###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_AMASS")
newPart.addTag("oompIndex", "AMASS_XT30UPB-F_1x02_P5.0mm_Vertical")

newPart.addTag("kicadDesc", "Connector XT30 Vertical PCB Female, https://www.tme.eu/en/Document/4acc913878197f8c2e30d4b8cdc47230/XT30UPB%20SPEC.pdf")
newPart.addTag("kicadTags", "RC Connector XT30")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_AMASS.3dshapes/AMASS_XT30UPB-F_1x02_P5.0mm_Vertical.wrl")

OOMP.parts.append(newPart)