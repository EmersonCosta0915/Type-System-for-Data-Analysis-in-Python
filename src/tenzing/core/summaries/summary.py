import pandas as pd
import networkx as nx

from tenzing.core.model import tenzing_complete_set
from tenzing.core.model.models import tenzing_model
from tenzing.core.model.types import *
from tenzing.core.summaries import *
from tenzing.core.summaries.frame.dataframe_series_summary import (
    dataframe_series_summary,
)
from tenzing.core.summaries.frame.dataframe_type_summary import dataframe_type_summary
from tenzing.utils.graph import output_graph


class Summary(object):
    def __init__(self, summary_ops, typeset):
        """

        Args:
            summary_ops:
            typeset:
        """
        self.typeset = typeset
        if summary_ops is None:
            summary_ops = {}

        if not all(
            issubclass(base_type, tenzing_model) for base_type in summary_ops.keys()
        ):
            raise TypeError("Summaries must be mapped on a type!")

        self.summary_ops = summary_ops

    def summarize_frame(
        self, df: pd.DataFrame, series_summary: dict, series_types: dict
    ):
        """Summarize a DataFrame based on the DataFrame object and the summaries of individual series

        Args:
            df: the DataFrame object
            series_summary: mapping from column name to the individual summaries
            series_types: mapping from column name to the series' type

        Returns:
            A summary of the DataFrame
        """
        return {
            **dataframe_summary(df),
            **dataframe_type_summary(series_types),
            **dataframe_series_summary(series_summary),
        }

    def summarize_series(self, series: pd.Series, summary_type: tenzing_model) -> dict:
        """

        Args:
            series:
            summary_type:

        Returns:

        """
        summary = {}

        G = self.typeset.base_graph.copy()

        done = []
        for base_type, summary_ops in self.summary_ops.items():
            if base_type not in done and nx.has_path(G, base_type, summary_type):
                for op in summary_ops:
                    summary.update(op(series))
                done.append(base_type)

        return summary

    def summarize(self, df: pd.DataFrame, types: dict) -> dict:
        """

        Args:
            df:
            types:

        Returns:

        """
        series_summary = {
            col: self.summarize_series(df[col], types[col]) for col in df.columns
        }
        frame_summary = self.summarize_frame(df, series_summary, types)
        return {"types": types, "series": series_summary, "frame": frame_summary}

    def plot(self, file_name, type_specific=None):
        """

        Args:
            file_name:
            type_specific:

        Returns:

        """
        G = self.typeset.base_graph.copy()
        G.graph["node"] = {"shape": "box", "color": "red"}

        included_nodes = G.nodes
        if type_specific is not None:
            leave = nx.ancestors(G, type_specific)

            included_nodes = leave
            G.remove_nodes_from(G.nodes - leave)

        G.add_node("summary", shape="note")
        for base_type, summary_ops in self.summary_ops.items():
            if len(summary_ops) > 0 and base_type in included_nodes:
                G.add_edge(
                    str(base_type),
                    "summary",
                    label="\n".join([str(op.__name__) for op in summary_ops]),
                )

        output_graph(G, file_name)


class CompleteSummary(Summary):
    def __init__(self):
        type_summary_ops = {
            tenzing_bool: [],
            tenzing_categorical: [category_summary, unique_summary],
            tenzing_complex: [
                infinite_summary,
                numerical_basic_summary,
                unique_summary_complex,
            ],
            tenzing_datetime: [range_summary, unique_summary],
            tenzing_date: [],
            tenzing_existing_path: [existing_path_summary, path_summary, text_summary],
            tenzing_float: [
                infinite_summary,
                numerical_summary,
                zero_summary,
                unique_summary,
            ],
            tenzing_geometry: [],
            tenzing_image_path: [],
            tenzing_integer: [
                infinite_summary,
                numerical_summary,
                zero_summary,
                unique_summary,
            ],
            tenzing_object: [unique_summary],
            tenzing_path: [path_summary, text_summary],
            tenzing_string: [text_summary, unique_summary],
            tenzing_time: [],
            tenzing_timedelta: [],
            tenzing_url: [url_summary, unique_summary],
            tenzing_generic: [base_summary, missing_summary],
        }
        super().__init__(type_summary_ops, tenzing_complete_set())
