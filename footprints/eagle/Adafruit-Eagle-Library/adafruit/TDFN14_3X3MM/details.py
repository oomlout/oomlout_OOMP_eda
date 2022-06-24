###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "TDFN14_3X3MM")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/TDFN14_3X3MM")

newPart.addTag("description", """&lt;b&gt;TDFN 14 3x3x0.75mm&lt;/b&gt;
&lt;p&gt;Source: http://datasheets.maxim-ic.com/en/ds/MAX98306.pdf&lt;/p&gt;
&lt;p&gt;Based on recommendtions in: http://www.freescale.com/files/sensors/doc/data_sheet/MAG3110.pdf&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-TDFN14_3X3MM",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='TDFN14_3X3MM')

OOMP.parts.append(newPart)