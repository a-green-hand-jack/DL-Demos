# 数据迁移和软链接操作记录

## 背景
由于项目空间限制，将大容量数据文件夹迁移至scratch目录下，并通过软链接保持原有代码结构。

## 目录信息
- 原始目录：`/projects/p32013/WJK/DL-Demos/`
- Scratch目录：`/scratch/hlv8980/WJK/DL-Demos/`

## 迁移的文件夹
以下文件夹因体积较大被迁移到scratch：
1. data
2. wandb
3. pretrain_models4. 

## 具体操作步骤

1. 创建scratch目标目录（如果不存在）：
```bash
mkdir -p /scratch/hlv8980/WJK/DL-Demos/
```

2. 移动文件夹到scratch：
```bash
mv /projects/p32013/WJK/DL-Demos/data /scratch/hlv8980/WJK/DL-Demos/
mv /projects/p32013/WJK/DL-Demos/wandb /scratch/hlv8980/WJK/DL-Demos/
mv /projects/p32013/WJK/DL-Demos/pretrain_models /scratch/hlv8980/WJK/DL-Demos/
mv /projects/p32013/WJK/DL-Demos/results /scratch/hlv8980/WJK/DL-Demos/
```

3. 在原目录创建软链接：
```bash
cd /projects/p32013/WJK/DL-Demos/
ln -s /scratch/hlv8980/WJK/DL-Demos/data ./data
ln -s /scratch/hlv8980/WJK/DL-Demos/wandb ./wandb
ln -s /scratch/hlv8980/WJK/DL-Demos/pretrain_models ./pretrain_models
ln -s /scratch/hlv8980/WJK/DL-Demos/results ./results
```

## 验证方法
使用以下命令检查软链接是否正确创建：
```bash
ls -l
```

软链接正确创建后会显示类似如下输出：
```
lrwxrwxrwx 1 hlv8980 p32013 xx xx xx data -> /scratch/hlv8980/WJK/DL-Demos/data
lrwxrwxrwx 1 hlv8980 p32013 xx xx xx wandb -> /scratch/hlv8980/WJK/DL-Demos/wandb
lrwxrwxrwx 1 hlv8980 p32013 xx xx xx pretrain_models -> /scratch/hlv8980/WJK/DL-Demos/pretrain_models
lrwxrwxrwx 1 hlv8980 p32013 xx xx xx results -> /scratch/hlv8980/WJK/DL-Demos/results
```

## 注意事项
- 确保scratch目录有足够的存储空间
- 软链接创建后，原有代码无需修改路径
- 定期检查scratch空间使用情况
  - checkscratch X
