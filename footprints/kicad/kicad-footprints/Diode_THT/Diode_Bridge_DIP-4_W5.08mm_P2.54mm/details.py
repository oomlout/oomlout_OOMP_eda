###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_DIP-4_W5.08mm_P2.54mm")
newPart.addTag("oompName", "kicad-footprints/Diode_THT/Diode_Bridge_DIP-4_W5.08mm_P2.54mm")

newPart.addTag("kicadDesc", "4-lead dip package for diode bridges, row spacing 5.08mm, pin-spacing 2.54mm, see http://www.vishay.com/docs/88898/b2m.pdf")
newPart.addTag("kicadTags", "DIL DIP PDIP 5.08mm 2.54")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_DIP-4_W5.08mm_P2.54mm.wrl")

OOMP.parts.append(newPart)