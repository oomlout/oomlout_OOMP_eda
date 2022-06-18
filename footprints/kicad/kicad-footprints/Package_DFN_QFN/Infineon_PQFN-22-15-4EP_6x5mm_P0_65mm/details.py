###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm")

newPart.addTag("kicadDesc", "PQFN 22 leads, 5x6mm, 0.127mm stencil (https://www.infineon.com/dgdl/ir4301.pdf?fileId=5546d462533600a4015355d5fc691819, https://www.infineon.com/dgdl/Infineon-AN1170-AN-v05_00-EN.pdf?fileId=5546d462533600a40153559ac3e51134)")
newPart.addTag("kicadTags", "pqfn 22 5x6mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm.wrl")

OOMP.parts.append(newPart)