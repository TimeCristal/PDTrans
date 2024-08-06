# python prepdata.py
python PDTrans/prepdata.py --data_folder PDTrans/data/elect --dataset elect
python evaluate.py --dataset='elect' --model-name='output_elect' --restore-file='best'

python PDTrans/prepare_data_exchange.py --data_folder PDTrans/data/exchange --dataset exchange

python PDTrans/train.py --model-name output_exchange --data-folder PDTrans/data/exchange --dataset exchange --lr 0.0001 --num_epochs 100
