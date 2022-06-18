###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Antenna")
newPart.addTag("oompIndex", "Texas_SWRA416_868MHz_915MHz")

newPart.addTag("kicadDesc", "http://www.ti.com/lit/an/swra416/swra416.pdf")
newPart.addTag("kicadTags", "PCB antenna")
newPart.addTag("kicadAttr", "smd")

OOMP.parts.append(newPart)