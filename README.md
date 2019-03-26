# Alfredworkflow_current_activity
### 初衷
工作中，经常需要查看当前运行的 `APP`　可见页面，本身电脑上是使用了 `Alfred` ,所以，就编写了这个 `workflow` 用于快速获取可见页面，便于开发中的使用，一定程度上提高开发效率

### 初步配置
`python` 中本身可以通过 `os.environ`、`os.getenv(key)` 获取系统环境变量的配置; 但是，在workflow 中执行 python 脚本的时候无法获取，获取的是 Alfred 的配置，由于是初步接触 workflow ，尚不知道如何获取，故先通过代码写死
```
打开两个python 脚本，修改代码中的 `adb_path` 的值，替换为自己的 adb 路径
```

### 使用
- 输入 ’cur‘ 即可看到效果
- 在结果页面，点击回车会将页面名称自动复制到剪切板，便于粘贴
