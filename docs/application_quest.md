# Git & GitHub

## check
```cmd
git branch
```
## push

```cmd
eval $(ssh-agent -s)
ssh-add .ssh_jieke/id_rsa_jieke 
git push
```
## pull

```cmd
# 确保你在 master 分支上
git checkout master

# 推送到远程仓库
git push origin master
```

## clone

```cmd
eval $(ssh-agent -s)
ssh-add .ssh_jieke/id_rsa_jieke 
git clone git@github.com:a-green-hand-jack/learning_diffusion.git
```

## check

### check jobs

```cmd
squeue -u $user_name  # default: hlv8980
```

### check resource

```cmd
sinfo
```

### kill jobs

```cmd
scancel $job_name   # sample: 3845773
```
# record

