"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.7.0

This code is used in preprocessing steps.
"""

from sklearn.model_selection import train_test_split

#Implement all methods required for processing

def validate_data(data):
    required={"row_id","target"}
    #check is data.colums containing row id and target columns. 
    if not required.issubset(data.columns):
        raise ValueError("Missing requred columns")
    if data.empty or data.isna().any().any():
        riase ValueError("Empty data or missing values")
    if not data["row_id"].is_unique:
        raise ValueError("Duplicate row id")
    return data.copy()


def split_data(data,options):
    ''' Train: 학습데이터.
    val: 하이퍼 파라미터 기반 최선의 모델을 선택하기 위한 학습 
    검증 데이터
    
    test: 학습 및 파라미터 튜닝 과정에 포함되지 않으며,
    최종 모델 선정 이후 해당 모델의 성능을 평가하는 보존용 데이터.
    학습 이전에 분리되어 최종 1번만 사용된다.
    '''
    dev,test = train_test_split(
        data,test_size=options["test_size"],
        random_state=options["seed"],
        stratify=data["targets"]
    )
    
    train, val = train_test_split(
        dev,test_size=options["val_size"],
        random_state=options["seed"],
        stratify=dev["target"],
    )
    
    return train,val,test

def add(a,b):
    return a+b