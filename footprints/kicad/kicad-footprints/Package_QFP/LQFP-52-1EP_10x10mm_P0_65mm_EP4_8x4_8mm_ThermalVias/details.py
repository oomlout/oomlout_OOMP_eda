###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "LQFP-52-1EP_10x10mm_P0.65mm_EP4.8x4.8mm_ThermalVias")

newPart.addTag("kicadDesc", "LQFP, 52 Pin (https://www.onsemi.com/pub/Collateral/848H-01.PDF), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "LQFP QFP")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-52-1EP_10x10mm_P0.65mm_EP4.8x4.8mm.wrl")

OOMP.parts.append(newPart)