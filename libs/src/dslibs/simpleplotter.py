# https://towardsdatascience.com/looking-beyond-feature-importance-37d2807aaaa7
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import time
import matplotlib as mpl


def plot_keras_model_history(x1, x2, label1, label2):
    mpl.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_title("Baseline and predictions", color='C0')
    ax.plot(range(len(x1)), x1, color="#f00", label=label1)
    ax.plot(range(len(x2)), x2, color="#00f", label=label2)
    plt.legend()


def feature_importance(model, X):
    n_features = X.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), X.keys())
    plt.xlabel("importance")
    plt.ylabel("feature")
    plt.show()


def chart(results_arr):
    plt.plot(list(results_arr.keys()), list(results_arr.values()))
    plt.show()


# more: https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html
# https://community.ibm.com/community/user/cloudpakfordata/blogs/harris-yang1/2021/05/26/scikit-learn-churn-model-cpd35
# https://www.kaggle.com/kanncaa1/roc-curve-with-k-fold-cv
def simple_roc(y_true, y_pred):
    fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pred, pos_label=1)
    plt.plot(fpr, tpr)
    plt.xlabel('False Positive Rate', fontsize=16)
    plt.ylabel('True Positive Rate', fontsize=16)
    plt.title('ROC', fontsize=18)


def simple_confusion_matrix(y_test, y_pred, labels):
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(x=j, y=i, s=cm[i, j], va='center', ha='center')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.tight_layout()
    plt.show()

    return cm


def simple_heatmap(df):
    data_correlations = df.corr()
    plt.subplots(figsize=(12, 10))
    sns.heatmap(data_correlations, cmap='Blues', annot=True)


def simple_correlations(df, target_name):
    cols = df.columns
    for label in cols:
        if label != target_name:
            sns.catplot(x=label, y=target_name, data=df)


def simple_features_overview(df):
    for label in df.columns:
        sns.catplot(x=label, data=df, height=3, aspect=4)
