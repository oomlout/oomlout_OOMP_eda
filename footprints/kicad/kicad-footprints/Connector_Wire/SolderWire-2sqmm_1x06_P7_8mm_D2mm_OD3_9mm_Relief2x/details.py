###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-2sqmm_1x06_P7.8mm_D2mm_OD3.9mm_Relief2x")

newPart.addTag("kicadDesc", "Soldered wire connection with double feed through strain relief, for 6 times 2 mm² wires, reinforced insulation, conductor diameter 2mm, outer diameter 3.9mm, size source Multi-Contact FLEXI-xV 2.0 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 2sqmm double-strain-relief")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-2sqmm_1x06_P7.8mm_D2mm_OD3.9mm_Relief2x.wrl")

OOMP.parts.append(newPart)