###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_PCBEdge")
newPart.addTag("oompIndex", "BUS_PCI_Express_Mini_Full")

newPart.addTag("kicadDesc", "Mini-PCI Express bus connector full size with clips (https://s3.amazonaws.com/fit-iot/download/facet-cards/documents/PCI_Express_miniCard_Electromechanical_specs_rev1.2.pdf#page=24)")
newPart.addTag("kicadTags", "mini pcie")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_PCBEdge.3dshapes/BUS_PCI_Express_Mini_Full.wrl")

OOMP.parts.append(newPart)