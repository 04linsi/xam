from sklearn.base import ClassifierMixin

from .base import BaseStackingEstimator


class StackingClassifier(BaseStackingEstimator, ClassifierMixin):

    def __init__(self, models, meta_model, n_folds=5, stratified=True, verbose=False):
        super(StackingClassifier, self).__init__(
            models=models,
            meta_model=meta_model,
            n_folds=n_folds,
            stratified=stratified,
            verbose=verbose
        )
