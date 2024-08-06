# python prepdata.py
python PDTrans/prepdata.py --data_folder PDTrans/data/elect --dataset elect
python evaluate.py --dataset='elect' --model-name='output_elect' --restore-file='best'