###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "Battery_Panasonic_CR3032-VCN_Vertical_CircularHoles")

newPart.addTag("kicadDesc", "Panasonic CR-3032/VCN battery, https://industrial.panasonic.com/cdbs/www-data/pdf2/AAA4000/AAA4000D508.PDF")
newPart.addTag("kicadTags", "battery CR-3032 coin cell vertical")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/Battery_Panasonic_CR3032-VCN_Vertical_CircularHoles.wrl")

OOMP.parts.append(newPart)