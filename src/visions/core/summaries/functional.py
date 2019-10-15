import pandas as pd

from visions.core.model import VisionsBaseType
from visions.core.summaries.summary import Summary


def summarize_frame(df: pd.DataFrame, summarizer: Summary):
    return summarizer.summarize_frame(df)


def summarize_series(
    series: pd.Series, series_type: VisionsBaseType, summarizer: Summary
):
    return summarizer.summarize_series(series, series_type)


def summarize(df: pd.DataFrame, series_types: dict, summarizer: Summary):
    return summarizer.summarize(df, series_types)
