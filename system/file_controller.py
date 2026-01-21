"""
File controller for managing file system operations.
"""

import os
from typing import List, Dict, Optional


class FileController:
    """Controls file system operations with safety checks."""

    def __init__(self, allowed_paths=None):
        """Initialize the file controller.
        
        Args:
            allowed_paths: List of allowed base paths for operations.
        """
        self.allowed_paths = allowed_paths or ["/workspaces/avatar"]

    def read_file(self, file_path):
        """Read a file with permission checks.
        
        Args:
            file_path: Path to the file to read.
            
        Returns:
            File contents or error.
        """
        if not self._is_allowed_path(file_path):
            return {"error": "Access denied"}
        
        try:
            with open(file_path, 'r') as f:
                return {"content": f.read(), "path": file_path}
        except Exception as e:
            return {"error": str(e)}

    def write_file(self, file_path, content):
        """Write to a file with permission checks.
        
        Args:
            file_path: Path to the file to write.
            content: Content to write.
            
        Returns:
            Status of the write operation.
        """
        if not self._is_allowed_path(file_path):
            return {"error": "Access denied"}
        
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            return {"status": "written", "path": file_path}
        except Exception as e:
            return {"error": str(e)}

    def list_files(self, directory_path):
        """List files in a directory with permission checks.
        
        Args:
            directory_path: Path to the directory.
            
        Returns:
            List of files or error.
        """
        if not self._is_allowed_path(directory_path):
            return {"error": "Access denied"}
        
        try:
            files = os.listdir(directory_path)
            return {"files": files, "path": directory_path}
        except Exception as e:
            return {"error": str(e)}

    def delete_file(self, file_path):
        """Delete a file with permission checks.
        
        Args:
            file_path: Path to the file to delete.
            
        Returns:
            Status of the delete operation.
        """
        if not self._is_allowed_path(file_path):
            return {"error": "Access denied"}
        
        try:
            os.remove(file_path)
            return {"status": "deleted", "path": file_path}
        except Exception as e:
            return {"error": str(e)}

    def create_directory(self, directory_path):
        """Create a directory with permission checks.
        
        Args:
            directory_path: Path to the directory to create.
            
        Returns:
            Status of the operation.
        """
        if not self._is_allowed_path(directory_path):
            return {"error": "Access denied"}
        
        try:
            os.makedirs(directory_path, exist_ok=True)
            return {"status": "created", "path": directory_path}
        except Exception as e:
            return {"error": str(e)}

    def _is_allowed_path(self, path):
        """Check if a path is in allowed directories.
        
        Args:
            path: The path to check.
            
        Returns:
            bool: True if path is allowed, False otherwise.
        """
        abs_path = os.path.abspath(path)
        for allowed in self.allowed_paths:
            if abs_path.startswith(os.path.abspath(allowed)):
                return True
        return False
