###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm")

newPart.addTag("kicadDesc", "16-Lead Lead Frame Chip Scale Package, 3x3mm, 0.5mm pitch, 1.854mm thermal pad (CP-16-22, http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp_16_22.pdf)")
newPart.addTag("kicadTags", "LFCSP 16 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm.wrl")

OOMP.parts.append(newPart)