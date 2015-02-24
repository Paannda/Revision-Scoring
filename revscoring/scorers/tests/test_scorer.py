from collections import namedtuple

from nose.tools import eq_

from ...features import badwords_added, misspellings_added
from ..scorer import Scorer


def test_scorer():
    FakeExtractor = namedtuple("FakeExtractor", ['extract', 'language'])
    extractor = FakeExtractor(lambda rid, features: [3, 5],
                              "herpderp")
    
    FakeModel = namedtuple("FakeModel", ['score', 'features', 'language'])
    multiply = FakeModel(lambda feature_values:feature_values[0] * \
                                               feature_values[1],
                         ["foo", "bar"],
                         "herpderp")
    divide = FakeModel(lambda feature_values:feature_values[0] / \
                                             feature_values[1],
                       ["foo", "bar"],
                       "herpderp")
    
    scorer = Scorer({"multiply": multiply, "divide": divide}, extractor)
    
    score_doc = scorer.score(1234567890)
    eq_(score_doc['divide'], 3/5)
    eq_(score_doc['multiply'], 3*5)
