###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm")

newPart.addTag("kicadDesc", "TQFP, 100 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/tqfp_edsv/sv_100_4.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "TQFP QFP")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm.wrl")

OOMP.parts.append(newPart)