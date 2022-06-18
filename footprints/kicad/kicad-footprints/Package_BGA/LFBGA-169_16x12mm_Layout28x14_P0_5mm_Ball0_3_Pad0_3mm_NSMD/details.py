###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "LFBGA-169_16x12mm_Layout28x14_P0.5mm_Ball0.3_Pad0.3mm_NSMD")

newPart.addTag("kicadDesc", "https://4donline.ihs.com/images/VipMasterIC/IC/SGST/SGSTS20279/SGSTS20279-1.pdf?hkey=EF798316E3902B6ED9A73243A3159BB0")
newPart.addTag("kicadTags", "eMMC Flash LFBGA169")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/LFBGA-169_16x12mm_Layout28x14.wrl")

OOMP.parts.append(newPart)