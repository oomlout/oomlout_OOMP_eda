###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "LFCSP-WD-10-1EP_3x3mm_P0.5mm_EP1.64x2.38mm_ThermalVias")

newPart.addTag("kicadDesc", "LFCSP-WD, 10 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp-10/CP_10_9.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "LFCSP-WD NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-WD-10-1EP_3x3mm_P0.5mm_EP1.64x2.38mm.wrl")

OOMP.parts.append(newPart)