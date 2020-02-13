pushd $0/../scripts
export PYTHONPATH=$PWD
export ROOT=$PWD
echo $PYTHONPATH
popd
python3 $ROOT/main.py $* 
