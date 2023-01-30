s='ahmad ksdjfsfjsfksf saqeeb  '
sub_s='saqeeb'
l=len(s)
result=s.find(sub_s,0,l)
if result==-1:
    print('string is not found')
else:
    print('string is present',sub_s)
