###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm")

newPart.addTag("kicadDesc", "80-Lead Plastic Thin Quad Flatpack (PF) - 14x14mm body, 9.5mm sq thermal pad (http://www.analog.com/media/en/technical-documentation/data-sheets/AD9852.pdf)")
newPart.addTag("kicadTags", "QFP 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm.wrl")

OOMP.parts.append(newPart)