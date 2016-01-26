# Git hooks

[Apresentação](https://docs.google.com/presentation/d/13ytGnC-iRAp-T4zG-Q1FutOuMGNgdB9EWXTHKry_D3E/edit?usp=sharing)

## pre-commit
[Jig](https://pythonhosted.org/jig/)

```shell
pip install jig
jig init .
jig install .jigplugins.txt
jig runnow
```

## post-commit
[lolcommits](https://lolcommits.github.io/)
```shell
gem install lolcommits
```

[Install](https://github.com/mroth/lolcommits/wiki/Installing-on-Linux)

## post-receive
[Deploy](http://ryanflorence.com/deploying-websites-with-a-tiny-git-hook/)

```shell
ssh usuario@servidor-remoto && cd algum/diretorio && git init
vim .git/hooks/post-receive
#!/bin/sh
cd ..
GIT_DIR='.git'
umask 002 && git reset --hard
```
```shell
git remote add production ssh://usuario@servidor-remoto/algum/diretorio/
# edit, add, commit
git push production master
```

[Algumas discussões sobre os hooks] (http://programmers.stackexchange.com/questions/260778/is-it-a-good-practice-to-run-unit-tests-in-version-control-hooks)
