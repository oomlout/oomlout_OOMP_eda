###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fuse")
newPart.addTag("oompIndex", "Fuseholder_Cylinder-5x20mm_EATON_HBV_Vertical_Closed")

newPart.addTag("kicadDesc", "5 mm x 20 mm fuse holders; Vertical w/ Stability Pins; 250V; 6.3-16A (http://www.cooperindustries.com/content/dam/public/bussmann/Electronics/Resources/product-datasheets/Bus_Elx_DS_2118_HB_PCB_Series.pdf)")
newPart.addTag("kicadTags", "fuse holder vertical 5x20mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_EATON_HBV_Vertical_Closed.wrl")

OOMP.parts.append(newPart)