###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "HTQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm_Mask4.4x4.4mm_ThermalVias")

newPart.addTag("kicadDesc", "64-Lead Plastic Thin Quad Flatpack (PT) - 10x10x1 mm Body, 2.00 mm Footprint [HTQFP] thermal pad")
newPart.addTag("kicadTags", "HTQFP-64 Pitch 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-64_10x10mm_Pitch0.5mm_EP8x8mm.wrl")

OOMP.parts.append(newPart)