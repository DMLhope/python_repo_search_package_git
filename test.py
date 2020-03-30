import re
data = "<a jdlasfjlaw;skjf> 6666</jslakdfja>"
test = re.sub(r'\</.*\>'," ",data)
test= re.sub(r'^\<.*\>'," ",test)
print (test)