source activate my-rdkit-env
for name in   *.sdf

do
base=${name%.sdf}
babel -isdf  $name  -osmi $base'_ligand.smi'
mol2vec featurize -i $base'_ligand.smi' -o  $base'.csv' -m  ../model_300dim.pkl  --uncommon UNK -r 1
echo $name
done

