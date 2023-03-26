import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics.base_metric import generate_column_metrics
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset
from evidently.metrics import *
from evidently.test_suite import TestSuite
from evidently.tests.base_test import generate_column_tests
from evidently.test_preset import DataStabilityTestPreset, NoTargetPerformanceTestPreset
from evidently.tests import *
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

df = pd.read_csv("data/processed/current_data.csv", sep=",", header=0)
df1 = pd.read_csv("data/processed/reference_data.csv", sep=",", header=0)

report = Report(metrics=[
    DataDriftPreset(), 
])


report.run(reference_data=df1, current_data=df)
report
#report.show(mode='inline')

print(report.json())

#report.save("data_drift.html")


numerical_features = ["pm10", "temp","dwpt","rhum","prcp","snow","wdir","wspd","wpgt","pres","tsun","coco"]
column_mapping = ColumnMapping()

column_mapping.datetime = "date"
column_mapping.numerical_features = numerical_features

data_drift_dashboard = Dashboard(tabs=[DataDriftTab(verbose_level=0)])

data_drift_dashboard.calculate(df1, df, column_mapping=column_mapping)
data_drift_dashboard.show(mode="inline")

data_drift_dashboard.save("data/processed/data_drift.html")