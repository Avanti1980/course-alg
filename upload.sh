cp ~/.mume/parser.js js/
cp ~/.mume/mathjax_config.js js/
cp ~/Notes/ML/AdaBoost/adaboost.pdf notes/
cp ~/Notes/Math/Matrix-Theory/Matrix-Derivative/matrix-derivative.pdf notes/

git add *
git commit -m $1

case $2 in
"ee")
    git push gitee master
    ;;
"hub")
    git push github master
    ;;
"both")
    git push gitee master
    git push github master
    ;;
*)
    echo "error: 2nd par must be [ee|hub|both]!"
    ;;
esac
