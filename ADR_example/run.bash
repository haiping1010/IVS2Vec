cat  nonredudent.tab  | while read  line
do

base=${line:7:4}

echo $base
wget 'https://files.rcsb.org/download/'$base'.pdb'


done

