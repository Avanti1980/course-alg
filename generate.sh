for i in {1..9}; do
    mpe2html slides/0$i.md 1
done
mpe2html slides/10.md 1
mpe2html index.md 1
