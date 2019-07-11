put all your receptors PDB here.  make sure you install fpocket, mol2vec, and python2.7, and all python dependency that will used in the code.  Then:

1. bash run_x.bash     (prepocess the data)

2. bash  run_all.bash     (run the fpocket)

3.bash  run_poc.bash        (complete the pocket residue)

4. cp -r ????/????_wpocket_n.pdb   all_pocket_Metformin/

5.  cd  all_pocket_Metformin/  ;  bash  run_poc.bash  (convert pocket to vector,make sure the model_300dim.pkl is in the folder)

6. cd ligand  ; bash bach_mol2vec.bash  ; cp *.csv  ../


7. mkdir  mp_data ;source deactivate ;   python data_process_all.py  .     ( prepare final input data; don't forget the '.' )

8. python deep_dense_FC_load.py    (make sure you have the  FCdense.h5 is in the folder)
