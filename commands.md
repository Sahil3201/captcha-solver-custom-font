## Commands to run:
python ./generate.py --width 128 --height 64 --length 5 --symbols symbols.txt --count 32 --output-dir test

python ./train.py --width 128 --height 64 --length 5 --symbols symbols.txt --batch-size 32 --epochs 5 --output-model test.h5 --train-dataset training_data --validate-dataset validation_data

python ./classify.py --model-name test.h5 --captcha-dir .\lunawats-project1\ --output stuff.txt --symbols symbols.txt
