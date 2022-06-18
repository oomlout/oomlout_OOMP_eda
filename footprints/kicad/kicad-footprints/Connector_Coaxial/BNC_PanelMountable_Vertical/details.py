###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Coaxial")
newPart.addTag("oompIndex", "BNC_PanelMountable_Vertical")

newPart.addTag("kicadDesc", "Panel-mountable BNC connector mounted through PCB, vertical")
newPart.addTag("kicadTags", "BNC connector")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/BNC_PanelMountable_Vertical.wrl")

OOMP.parts.append(newPart)