"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 1.7.0

validation, train 관련 함수들
"""

from sklearn.pipeline import Pipeline as SkPipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegressin
from sklearn.metrics import accuracy_score, f1_score

def train_model(train_data, options):
    model=SkPipeline([("scale",StandardScaler()),
                      ("classifier",LogisticRegression(
                          C=options
                      ))
                      ])

