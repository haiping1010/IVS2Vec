cd ..
for name in ????_w_out
do

base=${name%_w_out}

cp -r $name/$base'_wpocket_n.pdb'  all_pocket

done
