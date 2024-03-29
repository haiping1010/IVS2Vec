source activate my-rdkit-env
for name in Metformin.mol2

do
base=${name%.mol2}
babel -imol2  $name  -osmi $base'_ligand.smi'
mol2vec featurize -i $base'_ligand.smi' -o  $base'.csv' -m  /share/home/zhanghaiping/program/mol2vec/examples/models/model_300dim.pkl  --uncommon UNK -r 1
echo $name
done

