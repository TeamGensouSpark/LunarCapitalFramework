import lunarlib
import sys

argvs=sys.argv
properties=lunarlib.properties.GradleProperties("gradle.properties").properties

try:keymod=argvs[0]
except:keymod=""

for key in lunarlib.tasks.__dict__.keys():
    if keymod.upper() == key.upper():
        lunarlib.tasks.__dict__.get(key)(**properties)
