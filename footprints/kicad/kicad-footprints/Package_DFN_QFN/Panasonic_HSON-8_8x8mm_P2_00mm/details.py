###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Panasonic_HSON-8_8x8mm_P2.00mm")

newPart.addTag("kicadDesc", "Panasonic HSON-8, 8x8x1.25mm (https://industrial.panasonic.com/content/data/SC/ds/ds7/c0/PKG_HSON008-A-0808XXI_EN.pdf)")
newPart.addTag("kicadTags", "panasonic hson")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Panasonic_HSON-8_8x8mm_P2.00mm.wrl")

OOMP.parts.append(newPart)