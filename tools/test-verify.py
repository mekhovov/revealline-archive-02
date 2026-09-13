import tempfile,unittest
from pathlib import Path
from prepare import scan,verify_directories
class ArtifactDirectoryTests(unittest.TestCase):
 def test_exact_tree(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);(r/'a').mkdir();(r/'a/x').write_bytes(b'x');verify_directories(r,scan(r))
 def test_empty_hidden_directory_is_not_an_accepted_file_inventory(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);(r/'x').write_bytes(b'x');expected=scan(r);(r/'.git').mkdir()
   self.assertEqual(scan(r),expected)
   with self.assertRaisesRegex(RuntimeError,'directory'):verify_directories(r,expected)
 def test_empty_ordinary_directory_is_not_an_accepted_file_inventory(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);(r/'x').write_bytes(b'x');expected=scan(r);(r/'unlisted').mkdir()
   with self.assertRaisesRegex(RuntimeError,'directory'):verify_directories(r,expected)
 def test_directory_link_is_refused(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);(r/'a').mkdir();(r/'a/x').write_bytes(b'x');expected=scan(r);(r/'link').symlink_to(r/'a',target_is_directory=True)
   with self.assertRaisesRegex(RuntimeError,'symlink'):scan(r)
   with self.assertRaisesRegex(RuntimeError,'directory'):verify_directories(r,expected)
if __name__=='__main__':unittest.main()
