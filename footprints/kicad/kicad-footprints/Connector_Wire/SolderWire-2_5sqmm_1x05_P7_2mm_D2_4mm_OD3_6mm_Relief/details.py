###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-2.5sqmm_1x05_P7.2mm_D2.4mm_OD3.6mm_Relief")

newPart.addTag("kicadDesc", "Soldered wire connection with feed through strain relief, for 5 times 2.5 mm² wires, basic insulation, conductor diameter 2.4mm, outer diameter 3.6mm, size source Multi-Contact FLEXI-E 2.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 2.5sqmm strain-relief")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-2.5sqmm_1x05_P7.2mm_D2.4mm_OD3.6mm_Relief.wrl")

OOMP.parts.append(newPart)