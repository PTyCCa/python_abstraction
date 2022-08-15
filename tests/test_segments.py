from points import make_decart_point
from lessons.segments import get_begin_point, get_end_point, get_mid_point_of_segment, make_segment  # noqa: E501, I001


def test_segments():
    begin_point = make_decart_point(4, 2)
    end_point = make_decart_point(0, 0)
    segment = make_segment(begin_point, end_point)
    assert get_begin_point(segment) == begin_point
    assert get_end_point(segment) == end_point
    assert make_decart_point(2, 1) == get_mid_point_of_segment(segment)

    segment2 = make_segment(make_decart_point(3, 2), make_decart_point(2, 3))
    assert make_decart_point(2.5, 2.5) == get_mid_point_of_segment(segment2)