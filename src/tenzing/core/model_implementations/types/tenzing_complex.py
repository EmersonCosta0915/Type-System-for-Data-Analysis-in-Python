import pandas.api.types as pdt

from tenzing.core import tenzing_model
from tenzing.core.mixins import uniqueSummaryMixin, optionMixin, baseSummaryMixin
from tenzing.utils import singleton


@singleton.singleton_object
class tenzing_complex(baseSummaryMixin, optionMixin, uniqueSummaryMixin, tenzing_model):
    """**Complex** implementation of :class:`tenzing.core.models.tenzing_model`.

    >>> x = pd.Series([np.complex(0, 0), np.complex(1, 2), np.complex(3, -1), np.nan])
    >>> x in tenzing_complex
    True
    """
    def contains_op(self, series):
        return pdt.is_complex_dtype(series)

    def cast_op(self, series):
        return series.astype('complex')

    def summarization_op(self, series):
        summary = super().summarization_op(series)

        aggregates = ['mean']
        summary.update(series.agg(aggregates).to_dict())
        return summary
