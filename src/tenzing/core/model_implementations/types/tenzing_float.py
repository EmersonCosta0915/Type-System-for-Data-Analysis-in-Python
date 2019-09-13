import pandas.api.types as pdt
import numpy as np

from tenzing.core.model_implementations.types.tenzing_generic import tenzing_generic
from tenzing.core.model_implementations.types.tenzing_integer import tenzing_integer
from tenzing.core.reuse import unique_summary, zero_summary


class tenzing_float(tenzing_generic):
    """**Float** implementation of :class:`tenzing.core.models.tenzing_model`.

    >>> x = pd.Series([1.0, 2.5, 5.0, np.nan])
    >>> x in tenzing_float
    True
    """

    @classmethod
    def contains_op(cls, series):
        if not pdt.is_float_dtype(series):
            return False
        # TODO: are we sure we want this to depend on integer?
        elif series in tenzing_integer:
            return False
        else:
            return True

    @classmethod
    def cast_op(cls, series, operation=None):
        return series.astype(float)

    @classmethod
    @unique_summary
    @zero_summary
    def summarization_op(cls, series):
        summary = super().summarization_op(series)

        # Filter series
        series = super().get_series(series)

        aggregates = [
            "mean",
            "std",
            "var",
            "max",
            "min",
            "median",
            "kurt",
            "skew",
            "sum",
            "mad",
        ]
        summary.update(series.agg(aggregates).to_dict())

        quantiles = [0.05, 0.25, 0.5, 0.75, 0.95]
        for percentile, value in series.quantile(quantiles).to_dict().items():
            summary["quantile_{:d}".format(int(percentile * 100))] = value

        summary["range"] = summary["max"] - summary["min"]
        summary["iqr"] = summary["quantile_75"] - summary["quantile_25"]
        summary["cv"] = summary["std"] / summary["mean"] if summary["mean"] else np.NaN

        # TODO: only calculations for histogram, not the plotting
        # summary['image'] = plotting.histogram(series)
        return summary
