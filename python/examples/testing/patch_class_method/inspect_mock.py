from report_generator import ReportGenerator
from unittest import mock


@mock.patch.object(ReportGenerator, "_get_information_from_database")
def test_calculator(mock_my_method):

    mock_my_method.return_value = [10, 10]
    report_generator = ReportGenerator()
    report = report_generator.generate_report()
    import pdb

    pdb.set_trace()
    assert report == 20


test_calculator()
