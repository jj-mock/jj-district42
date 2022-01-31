from baby_steps import given, then, when
from jj.mock import HistoryResponse

from blahblah import generate
from jj_district42 import HistoryResponseSchema


def test_history_response_generation():
    with given:
        sch = HistoryResponseSchema()

    with when:
        res = generate(sch)

    with then:
        assert isinstance(res, HistoryResponse)
