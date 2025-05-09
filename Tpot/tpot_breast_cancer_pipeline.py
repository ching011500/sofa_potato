from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.kernel_approximation import RBFSampler
from xgboost import XGBClassifier

# 將 TPOT 匯出的 pipeline 包成變數
exported_pipeline = Pipeline(steps=[
    ('minmaxscaler', MinMaxScaler()),
    ('rfe', RFE(estimator=ExtraTreesClassifier(
        max_features=0.4503212524738,
        min_samples_leaf=4,
        min_samples_split=7,
        n_jobs=1,
        random_state=42),
        step=0.9162776237062)),
    ('featureunion-1', FeatureUnion(transformer_list=[
        ('featureunion', FeatureUnion(transformer_list=[
            ('rbfsampler', RBFSampler(gamma=0.6120209822633)),
            ('minmaxscaler', MinMaxScaler())
        ]))
    ])),
    ('xgbclassifier', XGBClassifier(
        gamma=0.7827110910559,
        learning_rate=0.2724956463284,
        max_depth=10,
        min_child_weight=4,
        missing=float("nan"),
        n_estimators=100,
        n_jobs=1,
        nthread=1
    ))
])
