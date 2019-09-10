class uniqueSummaryMixin:
    """Mixin adding missing value support to tenzing types

    When creating a custom Tenzing type simply inherit from optionMixin to add
    automatic support for missing values.

    """

    def get_series(self, series):
        series = super().get_series(series)
        return series

    def summarization_op(self, series):
        summary = super().summarization_op(series)

        # try:
        n_unique = len(set(series.values))
        # n_unique = series.nunique()
        summary.update({"n_unique": n_unique, "perc_unique": float(n_unique) / len(series)})
        # except Exception:
        #     pass
        return summary


"""
    def warnings(summary):
        messages = []
        if summary["n_unique"] == 1:
            messages.append("n_unique:const")
        if summary["p_unique"] == 1.0:
            messages.append("n_unique:unique")
        return messages
"""
