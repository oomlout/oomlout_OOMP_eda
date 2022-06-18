###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.95x4.9mm_Mask2.4x3.1mm_ThermalVias")

newPart.addTag("kicadDesc", "8-pin HTSOP package with 1.27mm pin pitch, compatible with SOIC-8, 3.9x4.9mm body, exposed pad, thermal vias, http://www.ti.com/lit/ds/symlink/drv8870.pdf")
newPart.addTag("kicadTags", "HTSOP 1.27")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.85x4.9mm_Mask2.4x3.1mm_ThermalVias.wrl")

OOMP.parts.append(newPart)