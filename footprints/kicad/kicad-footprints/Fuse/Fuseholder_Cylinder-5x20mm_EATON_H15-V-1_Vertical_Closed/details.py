###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fuse")
newPart.addTag("oompIndex", "Fuseholder_Cylinder-5x20mm_EATON_H15-V-1_Vertical_Closed")

newPart.addTag("kicadDesc", "PCB fuse holders for 5 mm x 20 mm fuses; 250V; 10A (http://www.cooperindustries.com/content/dam/public/bussmann/Electronics/Resources/product-datasheets/bus-elx-ds-4426-h15.pdf)")
newPart.addTag("kicadTags", "fuse holder vertical 5x20mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_EATON_H15-V-1_Vertical_Closed.wrl")

OOMP.parts.append(newPart)