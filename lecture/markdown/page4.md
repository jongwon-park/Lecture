## miniconda 가상환경 만들기
<font size="5" >

1. Create a new environment named "new_env" that contains Python 3.9
```bash
$ conda create --name new_env python=3.9
```

2. Activate the new environment
```bash
$ conda activate new_env
```

3. Verify that the new_env environment has been added and is active
```bash
$ conda info --envs
```

4. Deactivate the environment
```bash
$ conda activate
```

5. Managing packages
```bash
(new_env) $ conda search beautifulsoup4
(new_env) $ conda install beautifulsoup4
(new_env) $ conda list
```

</font>
