source activate my-rdkit-env


for name in  ????_wpocket_n.pdb
do


nohup python  test_poc.py $name &
sleep 1s



done
