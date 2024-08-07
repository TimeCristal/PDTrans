
python prepdata.py
python evaluate.py --dataset='elect' --model-name='output_elect' --restore-file='best'

#this is ok to be run OUTSIDE top dir
python PDTrans/prepdata.py --data_folder PDTrans/data/elect --dataset elect

python PDTrans/train.py --model-name PDTrans/output_elect --data-folder PDTrans/data --dataset elect --lr 0.0001

#this is ok to be run INSIDE top dir
python evaluate.py --dataset elect --model-name output_elect --restore-file='best'
