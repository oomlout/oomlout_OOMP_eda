###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-0.75sqmm_1x05_P7mm_D1.25mm_OD3.5mm")

newPart.addTag("kicadDesc", "Soldered wire connection, for 5 times 0.75 mm² wires, reinforced insulation, conductor diameter 1.25mm, outer diameter 3.5mm, size source Multi-Contact FLEXI-xV 0.75 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 0.75sqmm")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.75sqmm_1x05_P7mm_D1.25mm_OD3.5mm.wrl")

OOMP.parts.append(newPart)