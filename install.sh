pushd $0/..
echo $PWD/bin/stash.sh \$\* > ~/.local/bin/bhstash
chmod +x              ~/.local/bin/bhstash
popd
