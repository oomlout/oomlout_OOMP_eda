###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "LQFP-64-1EP_10x10mm_P0.5mm_EP6.5x6.5mm")

newPart.addTag("kicadDesc", "LQFP, 64 Pin (https://www.nxp.com/files-static/shared/doc/package_info/98ARH98426A.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "LQFP QFP")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-64-1EP_10x10mm_P0.5mm_EP6.5x6.5mm.wrl")

OOMP.parts.append(newPart)