# Problem-Solving

## Maintain Submodule

+ directory structure
```
Parent_dir
|
|--submodule1
...
```
+ update submodule
```
$ cd submodule

work ...

$ sh git.sh # use my script

$ cd ..

$ git add .

$ git commit -m "submodule change"

$ git push
```
**즉, 서브모듈에서 작업한 내용을 푸쉬하면 서브모듈의 origin으로 반영되고 부모 레포지토리에서는 반영 이전의 커밋이 남아있기때문에 부모레포지토리도 푸쉬해야한다.**
