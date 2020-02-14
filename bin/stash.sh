pushd $0/../scripts >> /tmp/dev.nul
export PYTHONPATH=$PWD:$PYTHONPATH
export ROOT=$PWD
popd >> /tmp/dev.nul
python3 $ROOT/main.py $* 
