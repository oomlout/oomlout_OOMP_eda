###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "Texas_S-PVSON-N8_ThermalVias")

newPart.addTag("kicadDesc", "8-Lead Plastic VSON, 3x3mm Body, 0.65mm Pitch, S-PVSON-N8, http://www.ti.com/lit/ds/symlink/opa2333.pdf")
newPart.addTag("kicadTags", "DFN 0.65 S-PVSON-N8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_S-PVSON-N8.wrl")

OOMP.parts.append(newPart)