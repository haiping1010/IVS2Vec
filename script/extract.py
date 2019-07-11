import sys
if len(sys.argv) <1 :
   print("python python2_L.py xxx")
filebase=sys.argv[1]
##filebase=file.replace(".pdb","")

fr=open('pockets/pocket1_atm.pdb','r')
arr=[]
for name in fr.readlines():
    if name[0:4]=='ATOM':
       id=name[17:26]
       print id
       arr.append(id)
frr=open('../'+filebase+'.pdb', 'r')
fw=open(filebase+'pocket_n.pdb','w')
for nameline in frr.readlines():
    for id in list(set(arr)):
        if nameline[17:26]==id:
            fw.write(nameline)
