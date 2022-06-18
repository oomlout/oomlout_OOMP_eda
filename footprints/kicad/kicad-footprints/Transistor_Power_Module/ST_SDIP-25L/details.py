###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transistor_Power_Module")
newPart.addTag("oompIndex", "ST_SDIP-25L")

newPart.addTag("kicadDesc", "25-lead TH, SDIP-25L, https://www.st.com/resource/en/datasheet/stgips20k60.pdf")
newPart.addTag("kicadTags", "igbt diode module")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/ST_SDIP-25L.wrl")

OOMP.parts.append(newPart)