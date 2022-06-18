###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Button_Switch_SMD")
newPart.addTag("oompIndex", "SW_SPST_TL3305A")

newPart.addTag("kicadDesc", "https://www.e-switch.com/system/asset/product_line/data_sheet/213/TL3305.pdf")
newPart.addTag("kicadTags", "TL3305 Series Tact Switch")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_SPST_TL3305A.wrl")

OOMP.parts.append(newPart)