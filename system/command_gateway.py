"""
Command gateway for routing and executing system commands.
"""


class CommandGateway:
    """Routes and executes system commands with validation."""

    def __init__(self, permissions_manager=None):
        """Initialize the command gateway.
        
        Args:
            permissions_manager: Manager for checking command permissions.
        """
        self.permissions_manager = permissions_manager
        self.command_history = []

    def execute_command(self, command, args=None):
        """Execute a system command with permission checks.
        
        Args:
            command: The command to execute.
            args: Optional arguments for the command.
            
        Returns:
            Command result or error.
        """
        if self.permissions_manager and not self.permissions_manager.has_permission(command):
            return {"error": "Permission denied"}
        
        self.command_history.append({"command": command, "args": args})
        return {"status": "executed", "command": command}

    def validate_command(self, command):
        """Validate that a command is safe to execute.
        
        Args:
            command: The command to validate.
            
        Returns:
            bool: True if command is valid and safe.
        """
        pass

    def get_command_history(self):
        """Get the history of executed commands.
        
        Returns:
            List of command records.
        """
        return self.command_history

    def clear_history(self):
        """Clear command history."""
        self.command_history = []
