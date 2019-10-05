import pandas as pd

from tenzing.core.model import tenzing_complete_set, type_cast, type_inference
from tenzing.core.summaries.summary import CompleteSummary


# Load dataset
df = pd.read_csv(
    "https://github.com/codebrainz/color-names/raw/master/output/colors.csv",
    names=["Code", "Name", "Hex", "R", "G", "B"],
)

# Type
typeset = tenzing_complete_set()

# Type inference
inferred_types = type_inference(df, typeset)
print(inferred_types)

# Type cast
cast_df, cast_types = type_cast(df, typeset)
print(cast_types)

# Summarization
summary = CompleteSummary()
summaries = summary.summarize(cast_df, cast_types)
for key, variable_summary in summaries["series"].items():
    print(key, variable_summary)
