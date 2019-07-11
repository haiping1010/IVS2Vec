f=open('M201812186746803381A1F0E0DB47453E0216320D0C16F4T.tab', 'r')

oldname='From  '
arr=f.readlines()
fw=open('nonredudent.tab', 'w')
fww=open('nonredudent_pdb.list', 'w')
for name in arr:
    if name[0:6] != oldname:
        fw.write(name)
        nname=name.strip()
        fww.write(nname[-4:]+'\n')
        #nname=name.strip()
        #print (nname[-4:] )
        oldname=name[0:6]

