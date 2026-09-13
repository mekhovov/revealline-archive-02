import tempfile,unittest
from pathlib import Path
from prepare import scan,verify_directories,copy_frozen_site
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
class FrozenCopyTests(unittest.TestCase):
 def test_copy_preserves_hidden_bytes_and_original(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);original=root/'frozen';original.mkdir();(original/'.xonix-build.json').write_bytes(b'original');(original/'game').mkdir();(original/'game/index.html').write_bytes(b'game');before=scan(original)
   copy_frozen_site(original,root/'copy');self.assertEqual(scan(root/'copy'),before);self.assertEqual(scan(original),before)
 def test_symlink_refused_before_copy(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);original=root/'frozen';original.mkdir();(root/'outside').write_bytes(b'x');(original/'link').symlink_to(root/'outside')
   with self.assertRaisesRegex(RuntimeError,'regular'):copy_frozen_site(original,root/'copy')
   self.assertFalse((root/'copy').exists())
 def test_extra_empty_directory_refused_before_copy(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);original=root/'frozen';original.mkdir();(original/'x').write_bytes(b'x');(original/'.extra').mkdir()
   with self.assertRaisesRegex(RuntimeError,'directory'):copy_frozen_site(original,root/'copy')
   self.assertFalse((root/'copy').exists())
 def test_existing_destination_is_retained(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);original=root/'frozen';original.mkdir();(original/'x').write_bytes(b'x');target=root/'copy';target.mkdir();(target/'prior').write_bytes(b'prior')
   with self.assertRaises(FileExistsError):copy_frozen_site(original,target)
   self.assertEqual(scan(target),[{'path':'prior','bytes':5,'sha256':__import__('hashlib').sha256(b'prior').hexdigest()}])
if __name__=='__main__':unittest.main()
