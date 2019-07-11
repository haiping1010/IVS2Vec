for name in ????_w.pdb; do grep -r "^ATOM\|^TER\|^END" $name > $name'x'; grep -v "'" $name'x' > $name'xx' ;mv $name'xx' $name; done
