###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "Vishay_HVM-DIP-3_W7.62mm")

newPart.addTag("kicadDesc", "3-lead though-hole mounted high-volatge DIP package (based on standard DIP-4), row spacing 7.62 mm (300 mils), see https://www.vishay.com/docs/91361/hexdip.pdf")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 7.62mm 300mil Vishay HVMDIP HEXDIP")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/Vishay_HVM-DIP-3_W7.62mm.wrl")

OOMP.parts.append(newPart)