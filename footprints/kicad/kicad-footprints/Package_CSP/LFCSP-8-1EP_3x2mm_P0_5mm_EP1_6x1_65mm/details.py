###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "LFCSP-8-1EP_3x2mm_P0.5mm_EP1.6x1.65mm")

newPart.addTag("kicadDesc", "LFCSP 8pin Pitch 0.5mm, http://www.analog.com/media/en/package-pcb-resources/package/57080735642908cp_8_4.pdf")
newPart.addTag("kicadTags", "LFCSP 8pin thermal pad 3x2mm Pitch 0.5mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-8-1EP_3x2mm_P0.5mm_EP1.6x1.65mm.wrl")

OOMP.parts.append(newPart)