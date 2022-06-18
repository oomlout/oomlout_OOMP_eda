###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_AMASS")
newPart.addTag("oompIndex", "AMASS_XT30PW-M_1x02_P2.50mm_Horizontal")

newPart.addTag("kicadDesc", "Connector XT30 Horizontal PCB Male, https://www.tme.eu/en/Document/ce4077e36b79046da520ca73227e15de/XT30PW%20SPEC.pdf")
newPart.addTag("kicadTags", "RC Connector XT30")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_AMASS.3dshapes/AMASS_XT30PW-M_1x02_P2.50mm_Horizontal.wrl")

OOMP.parts.append(newPart)