###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "VFSOP-8")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/VFSOP-8")

newPart.addTag("description", """&lt;b&gt;VFSOP8&lt;/b&gt; - 0.5mm pitch, 2.0x2.3mm
&lt;p&gt;Source: http://focus.ti.com/lit/ds/symlink/txs0102.pdf&lt;/p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-VFSOP-8",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='VFSOP-8')

OOMP.parts.append(newPart)