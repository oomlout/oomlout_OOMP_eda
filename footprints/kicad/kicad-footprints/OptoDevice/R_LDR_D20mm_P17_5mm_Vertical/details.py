###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "R_LDR_D20mm_P17.5mm_Vertical")
newPart.addTag("oompName", "kicad-footprints/OptoDevice/R_LDR_D20mm_P17.5mm_Vertical")

newPart.addTag("kicadDesc", "Resistor, LDR 20mm diameter, pin pitch 17.5mm, see http://yourduino.com/docs/Photoresistor-5516-datasheet.pdf")
newPart.addTag("kicadTags", "Resistor LDR")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/R_LDR_D20mm_P17.5mm_Vertical.wrl")

OOMP.parts.append(newPart)