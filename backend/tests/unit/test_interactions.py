"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1

# def test_filter_with_none_item_id_returns_all_interactions() -> None:
#     """Test that when item_id is None, all interactions are returned."""
#     interactions = [
#         _make_log(1, 1, 1),
#         _make_log(2, 2, 2),
#         _make_log(3, 3, 3)
#     ]
#     result = _filter_by_item_id(interactions, None)
#     assert len(result) == 3
#     assert result == interactions


# def test_filter_with_non_existent_item_id_returns_empty_list() -> None:
#     """Test that filtering by non-existent item_id returns empty list."""
#     interactions = [
#         _make_log(1, 1, 1),
#         _make_log(2, 2, 2),
#         _make_log(3, 3, 3)
#     ]
#     result = _filter_by_item_id(interactions, 999)  # Несуществующий ID
#     assert len(result) == 0
#     assert result == []


# def test_filter_preserves_order_of_interactions() -> None:
#     """Test that filtering preserves the original order of interactions."""
#     interactions = [
#         _make_log(1, 1, 2),
#         _make_log(2, 2, 1),
#         _make_log(3, 3, 2),
#         _make_log(4, 4, 1)
#     ]
#     result = _filter_by_item_id(interactions, 2)
#     assert len(result) == 2
#     assert result[0].id == 1  # Первый элемент с item_id=2
#     assert result[1].id == 3  # Второй элемент с item_id=2


# def test_filter_with_multiple_matching_items_returns_all() -> None:
#     """Test that when multiple items match the item_id, all are returned."""
#     interactions = [
#         _make_log(1, 1, 5),
#         _make_log(2, 2, 5),
#         _make_log(3, 3, 5),
#         _make_log(4, 4, 6),
#         _make_log(5, 5, 5)
#     ]
#     result = _filter_by_item_id(interactions, 5)
#     assert len(result) == 4  # Должно быть 4 элемента с item_id=5
#     assert all(i.item_id == 5 for i in result)


# def test_filter_with_negative_item_id() -> None:
#     """Test that filtering works with negative item_id values."""
#     interactions = [
#         _make_log(1, 1, -1),
#         _make_log(2, 2, -2),
#         _make_log(3, 3, -1)
#     ]
#     result = _filter_by_item_id(interactions, -1)
#     assert len(result) == 2
#     assert result[0].id == 1
#     assert result[1].id == 3


# def test_filter_with_zero_item_id() -> None:
#     """Test that filtering works with zero item_id."""
#     interactions = [
#         _make_log(1, 1, 0),
#         _make_log(2, 2, 1),
#         _make_log(3, 3, 0)
#     ]
#     result = _filter_by_item_id(interactions, 0)
#     assert len(result) == 2
#     assert result[0].id == 1
#     assert result[1].id == 3
