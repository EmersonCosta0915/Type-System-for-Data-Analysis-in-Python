from pathlib import Path

from visions.core.model.types import tenzing_integer, tenzing_existing_path
from visions.core.summaries.summary import CompleteSummary


summaries_dir = Path("summaries/")
summaries_dir.mkdir(exist_ok=True)

summary = CompleteSummary()

# For all types
summary.plot(summaries_dir / "summary.svg")

# For a specific type
summary.plot(summaries_dir / "summary_integer.svg", tenzing_integer)
summary.plot(summaries_dir / "summary_existing_path.svg", tenzing_existing_path)
