import pytest

from unittest.mock import ANY, mock_open, patch

from test_utils.tools import dump_data


@pytest.mark.parametrize('path', [
    '/temp.dump',
])
def test_dump_data(path):
    data = {}
    with patch('builtins.open', mock_open()) as mock_file,\
            patch('test_utils.tools.dump_data.pickle.dump') as mock_pickle:
        dump_data.dump(path, {})
        mock_file.assert_called_once()
        mock_pickle.assert_called_once_with(data, ANY)
