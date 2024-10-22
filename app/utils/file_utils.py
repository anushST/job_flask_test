import os
import uuid
from pathlib import Path


def is_file_ext_allowed(file_name: str, allowed_extensions: set) -> bool:
    """Check if the file has allowed extension."""
    if file_name:
        return file_name.split('.')[-1] in allowed_extensions
    return False


class FilePath:
    """The class generates new uuid filename."""

    def __init__(self, old_filename, upload_folder, base_dir):
        self.old_filename = old_filename
        self.extension = self._get_file_extension()
        self.new_uuid_filename = self._generate_unique_filename()
        self.upload_folder = upload_folder
        self.base_dir = base_dir
        self.relative_path = self._get_relative_path()
        self.absolute_path = self._get_absolute_path()
        self.rel_path_filename = self._get_relative_path_with_filename()
        self.abs_path_filename = self._get_absolute_path_with_filename()
        self.url_path_type = self._get_url_type_rel_path_with_name()

    def _generate_unique_filename(self):
        """Generate a unique filename based on UUID."""
        unique_filename = str(uuid.uuid4()).replace('-', '')
        return f"{unique_filename}{self.extension}"

    def _get_file_extension(self):
        """Get the extension of the uploaded file."""
        return Path(self.old_filename).suffix

    def _get_relative_path(self):
        """Get the relative path for saving the file."""
        return self.upload_folder

    def _get_absolute_path(self):
        """Get the absolute path for saving the file."""
        return os.path.join(self.base_dir, self.relative_path)

    def _get_relative_path_with_filename(self):
        """Get the relative path for saving the file including filename."""
        return os.path.join(self.upload_folder, self.new_uuid_filename)

    def _get_absolute_path_with_filename(self):
        """Get the absolute path for saving the file including filename."""
        return os.path.join(self.base_dir, self.rel_path_filename)

    def _get_url_type_rel_path_with_name(self):
        """Get the relative path in url format with '/'."""
        return self.rel_path_filename.replace('\\', '/')
