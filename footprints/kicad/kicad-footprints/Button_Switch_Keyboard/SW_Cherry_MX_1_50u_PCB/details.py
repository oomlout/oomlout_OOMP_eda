###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Button_Switch_Keyboard")
newPart.addTag("oompIndex", "SW_Cherry_MX_1.50u_PCB")

newPart.addTag("kicadDesc", "Cherry MX keyswitch, 1.50u, PCB mount, http://cherryamericas.com/wp-content/uploads/2014/12/mx_cat.pdf")
newPart.addTag("kicadTags", "Cherry MX keyswitch 1.50u PCB")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Button_Switch_Keyboard.3dshapes/SW_Cherry_MX_1.50u_PCB.wrl")

OOMP.parts.append(newPart)