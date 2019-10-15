"""
A selection of testing utilities for visions.
"""
from typing import Callable, Union, List, Dict, Optional
import pandas as pd


def option_coercion_evaluator(method: Callable) -> Callable:
    """A coercion test evaluator

    Evaluates a coercion method and optionally returns the coerced series.

    Args:
        method: A method coercing a Series to another Series.

    Returns:
        The coerced series if the coercion succeeds otherwise None.
    """

    def f(series: pd.Series) -> Optional[pd.Series]:
        try:
            return method(series)
        except (ValueError, TypeError, AttributeError, SystemError):
            return None

    return f


def coercion_test(method: Callable) -> Callable:
    """A coercion test generator

    Creates a coercion test based on a provided coercion method.

    Args:
        method: A method coercing a Series to another type.

    Returns:
        Whether the coercion failed or was successful.

    """
    # Returns True or False if the coercion succeeds
    tester = option_coercion_evaluator(method)

    def f(series: pd.Series) -> bool:
        result = tester(series)
        return True if result is not None else False

    return f


def coercion_equality_test(method: Callable) -> Callable:
    """A coercion equality test generator

    Creates a coercion test based on a provided coercion method which also enforces
    equality constraints on the output. This is useful when you want to change the
    data type of a series without necessarily changing the data, for example,
    when converting an integer to a float.

    Args:
        method: A method coercing a Series to another type.

    Returns:
        Whether the coercion failed or was successful.
    """
    tester = option_coercion_evaluator(method)

    def f(series: pd.Series) -> bool:
        result = tester(series)
        return False if result is None else series.eq(result).all()

    return f


def coercion_map_test(mapping: Union[List[Dict], Dict]) -> Callable:
    """Create a testing function for a single mapping or a list of mappings.

    Args:
        mapping: A dict with a mapping or a list of dicts

    Returns:
        Callable that checks if a series consists of the mappable values

    Examples:
        >>> coercion_map_test({"Yes": True, "No": False})
        >>> coercion_map_test(
        >>>     [
        >>>         {"Yes": True, "No": False},
        >>>         {"Y": True, "N": False},
        >>>     ]
        >>> )
    """

    if type(mapping) == list:

        def f(series: pd.Series) -> bool:
            # TODO: None value
            return any(
                series.isin(list(single_map.keys()) + [None]).all()
                for single_map in mapping
            )

    elif type(mapping) == dict:

        def f(series: pd.Series) -> bool:
            return series.isin(list(mapping.keys()) + [None]).all()

    else:
        raise ValueError("Mapping should be dict or list of dicts")
    return f


def coercion_map(mapping: Union[List[Dict], Dict]) -> Callable:
    """Maps a series given a mapping

    Args:
        mapping: a dict to map, or a list of dicts.

    Returns:
        A callable that maps the series.
    """
    if type(mapping) == list:
        mapping = {k: v for d in mapping for k, v in d.items()}

    elif type(mapping) != dict:
        raise ValueError("Mapping should be dict or list of dicts")

    def f(series: pd.Series) -> pd.Series:
        return series.map(mapping)

    return f
