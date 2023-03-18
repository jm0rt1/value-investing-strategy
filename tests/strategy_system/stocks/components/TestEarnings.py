# TODO

from pathlib import Path


TEST_PATH = Path(
    "tests/test_files/inputs/strategy_system/stocks/stock/components/AAPL.Earnings.json")
DATA = {
    "symbol": "AAPL",
    "annualEarnings": [
        {
            "fiscalDateEnding": "2022-12-31",
            "reportedEPS": "1.88"
        }
    ],
    "quarterlyEarnings": [
        {
            "fiscalDateEnding": "2022-12-31",
            "reportedDate": "2023-02-02",
            "reportedEPS": "1.88",
            "estimatedEPS": "1.94",
            "surprise": "-0.06",
            "surprisePercentage": "-3.0928"
        }
    ]
}
