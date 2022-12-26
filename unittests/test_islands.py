from unittest import TestCase, main
from unittest.mock import mock_open, patch

from file_handlers import if_file_exists, if_file_readable, if_file_not_empty, FileNotExist, FileNotReadable, FileEmpty
from to_array import if_array_rectangular, if_data_consistent, read_file_to_array


class TestFileHandlers(TestCase):
    def test_file_exists(self):
        path = "../islands.txt"
        self.assertTrue(if_file_exists(path=path))

    def test_file_not_exists(self):
        path = "file_not_exists.txt"
        self.assertRaises(FileNotExist, if_file_exists, path)

    def test_file_readable(self):
        path = "../islands.txt"
        self.assertTrue(if_file_readable(path=path))

    @patch('builtins.open', mock_open(read_data=''))
    def test_file_not_readable(self):
        self.assertRaises(FileNotReadable, if_file_readable, "some_path")

    def test_file_not_empty(self):
        path = "../islands.txt"
        self.assertTrue(if_file_not_empty(path=path))

    def test_file_empty(self):
        path = "empty.txt"
        self.assertRaises(FileEmpty, if_file_not_empty, path)


class TestArrayData(TestCase):
    def test_array_rectangular(self):
        array = [["0", "1", "0"], ["0", "1", "1"], ["1", "1", "0"], ["0", "1", "0"]]
        self.assertTrue(if_array_rectangular(array=array))

    def test_array_not_rectangular(self):
        array = [["0", "1"], ["0", "1", "1"], ["1", "1", "0"], ["0", "1", "0"]]
        self.assertFalse(if_array_rectangular(array=array))

    def test_data_consistent(self):
        line = ["0", "0", "1", "0", "1", "0", "1", "1", "1"]
        self.assertTrue(if_data_consistent(line=line))

    def test_data_not_consistent(self):
        line = ["0", "0", "1", "x", "1", "0", "1", "1", "1"]
        self.assertFalse(if_data_consistent(line=line))


class TestMakeArray(TestCase):
    data = ("00010100101\n"
            "11111000111\n"
            "00010110001\n"
            "00000000000\n"
            "11001001001\n"
            "01001111001\n"
            "00000101011")

    def test_read_file_to_array(self):
        mo = mock_open(read_data=self.data)
        with patch("builtins.open", mo) as mocked_open:
            self.assertEqual(read_file_to_array(path=self.data),
                             [['0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1'],
                              ['1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1'],
                              ['0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '1'],
                              ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                              ['1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'],
                              ['0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1'],
                              ['0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1']
                              ])


if __name__ == "__main__":
    main()
