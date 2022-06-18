###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TI_SO-PowerPAD-8_ThermalVias")
newPart.addTag("oompName", "kicad-footprints/Package_SO/TI_SO-PowerPAD-8_ThermalVias")

newPart.addTag("kicadDesc", "8-pin HTSOP package with 1.27mm pin pitch, compatible with SOIC-8, 3.9x4.9mm² body, exposed pad, thermal vias with large copper area, as proposed in http://www.ti.com/lit/ds/symlink/tps5430.pdf")
newPart.addTag("kicadTags", "HTSOP 1.27")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSOP-8-1EP_3.9x4.9mm_Pitch1.27mm.wrl")

OOMP.parts.append(newPart)