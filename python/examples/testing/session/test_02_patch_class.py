from E02_patch_class import ReportGenerator
from unittest import mock


def test_report_generator():
    report_gen = ReportGenerator()
    report = report_gen.generate_report()
    assert report == 2853


@mock.patch.object(ReportGenerator, "_get_database_data")
def test_report_generator_patched(mocked_method):
    mocked_method.return_value = [4324, 2341, 2324, 2424]
    report_generator = ReportGenerator()
    report = report_generator.generate_report()
    assert report == 2853


@mock.patch.object(ReportGenerator, "_get_database_data")
def test_report_generator_patched_mock_and_see(mocked_method):
    mocked_method.return_value = [4324, 2341, 2324, 2424]
    report_generator = ReportGenerator()
    report = report_generator.generate_report()
    import pdb

    pdb.set_trace()
    assert report == 2853
