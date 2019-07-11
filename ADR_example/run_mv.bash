mkdir -p  NMR

cat  NMR.list | while read line
do
cp -r ${line:0:4}*  NMR


done
