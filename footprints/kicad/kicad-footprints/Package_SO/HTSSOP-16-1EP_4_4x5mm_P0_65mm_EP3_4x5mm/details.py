###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm")

newPart.addTag("kicadDesc", "16-Lead Plastic HTSSOP (4.4x5x1.2mm); Thermal pad; (http://www.ti.com/lit/ds/symlink/drv8833.pdf)")
newPart.addTag("kicadTags", "SSOP 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-16-1EP_4.4x5mm_Pitch0.65mm_EP3.4x5mm.wrl")

OOMP.parts.append(newPart)