## Generating captchas
```
python generate.py --symbols assets/symbols.txt --font assets/clouds_font.ttf --output-file data/data.csv --output-dir data/test --count 100
```

python ./train.py --width 128 --height 64 --length 6 --symbols assets/symbols.txt --batch-size 128 --epochs 5 --output-model test.h5 --train-dataset data/train --validate-dataset data/validate --training-labels data/train.csv --validate-labels data/validate.csv


python ./classify.py --model-name test.h5 --captcha-dir data/test --output stuff.txt --symbols assets/symbols.txt