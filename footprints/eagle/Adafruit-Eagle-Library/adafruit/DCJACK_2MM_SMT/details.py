###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "DCJACK_2MM_SMT")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/DCJACK_2MM_SMT")

newPart.addTag("description", """2.0/2.1mm DC Jack - SMT
&lt;p&gt;4UConnector: 03267&lt;/p&gt;
&lt;p&gt;Note: Small tRestrict polygon's were added to the ground pads to improve solderability when this part is used in combination with a ground pour.  By default, Eagle will product four large bridges to the ground pour significantly increasing the heat distribution on the pads and preventing lead-free solder from reflowing in certain situations.  For more details, see: http://www.microbuilder.eu/Blog/09-12-14/Reducing_Thermals_for_Large_Pads_in_Eagle.aspx&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-DCJACK_2MM_SMT",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='DCJACK_2MM_SMT')

OOMP.parts.append(newPart)