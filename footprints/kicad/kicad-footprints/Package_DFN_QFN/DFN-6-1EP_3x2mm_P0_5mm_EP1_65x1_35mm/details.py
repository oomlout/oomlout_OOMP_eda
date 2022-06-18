###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-6-1EP_3x2mm_P0.5mm_EP1.65x1.35mm")

newPart.addTag("kicadDesc", "DFN, 6 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-dfn/(DCB6)%20DFN%2005-08-1715%20Rev%20A.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "DFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-6-1EP_3x2mm_P0.5mm_EP1.65x1.35mm.wrl")

OOMP.parts.append(newPart)