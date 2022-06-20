###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "LFCSP-32-1EP_5x5mm_P0.5mm_EP3.25x3.25mm")
newPart.addTag("oompName", "kicad-footprints/Package_CSP/LFCSP-32-1EP_5x5mm_P0.5mm_EP3.25x3.25mm")

newPart.addTag("kicadDesc", "32-Lead Frame Chip Scale Package LFCSP (5mm x 5mm); (see http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp-32/CP_32_27.pdf")
newPart.addTag("kicadTags", "LFCSP 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-32-1EP_5x5mm_P0.5mm.wrl")

OOMP.parts.append(newPart)