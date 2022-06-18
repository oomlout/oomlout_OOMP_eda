###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm_ThermalVias")

newPart.addTag("kicadDesc", "VSON 10 Thermal on 11 3x3mm Pitch 0.5mm http://chip.tomsk.ru/chip/chipdoc.nsf/Package/D8A64DD165C2AAD9472579400024FC41!OpenDocument")
newPart.addTag("kicadTags", "VSON 10 Thermal on 11 3x3mm Pitch 0.5mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm.wrl")

OOMP.parts.append(newPart)