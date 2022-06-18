###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "LFCSP-VQ-24-1EP_4x4mm_P0.5mm_EP2.642x2.642mm")

newPart.addTag("kicadDesc", "LFCSP VQ, 24 pin, exposed pad, 4x4mm body, pitch 0.5mm (http://www.analog.com/media/en/package-pcb-resources/package/56702234806764cp_24_3.pdf, http://www.analog.com/media/en/technical-documentation/data-sheets/ADL5801.pdf)")
newPart.addTag("kicadTags", "LFCSP 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-VQ-24-1EP_4x4mm_P0.5mm_EP2.642x2.642mm.wrl")

OOMP.parts.append(newPart)