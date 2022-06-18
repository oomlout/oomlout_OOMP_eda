###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transistor_Power_Module")
newPart.addTag("oompIndex", "Littelfuse_Package_H_XBN2MM")

newPart.addTag("kicadDesc", "24-lead TH, Package H, https://www.littelfuse.com/~/media/electronics/datasheets/power_semiconductors/littelfuse_power_semiconductor_igbt_module_mg1215h_xbn2mm_datasheet.pdf.pdf")
newPart.addTag("kicadTags", "brifge rectifier igbt diode module")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Littelfuse_Package_H_XBN2MM.wrl")

OOMP.parts.append(newPart)