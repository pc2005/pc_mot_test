import os
import zipfile
import tempfile

def get_gzipped_model_size(file):
  """ gzip and get model size

  Args:
      file (str): File URL

  Returns:
      size (int): Size of gzipped file
  """
  # Returns size of gzipped model, in bytes.
  _, zipped_file = tempfile.mkstemp('.zip')
  with zipfile.ZipFile(zipped_file, 'w', compression=zipfile.ZIP_DEFLATED) as f:
    f.write(file)

  return os.path.getsize(zipped_file)

