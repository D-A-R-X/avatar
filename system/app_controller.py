"""
Application controller for managing application lifecycle and execution.
"""


class AppController:
    """Controls application lifecycle and execution."""

    def __init__(self):
        """Initialize the application controller."""
        self.running_apps = {}
        self.app_registry = {}

    def register_app(self, app_name, app_instance):
        """Register an application.
        
        Args:
            app_name: Name of the application.
            app_instance: Instance of the application.
        """
        self.app_registry[app_name] = app_instance

    def launch_app(self, app_name):
        """Launch a registered application.
        
        Args:
            app_name: Name of the application to launch.
            
        Returns:
            Status of the launch operation.
        """
        if app_name not in self.app_registry:
            return {"error": "Application not found"}
        
        app = self.app_registry[app_name]
        self.running_apps[app_name] = app
        return {"status": "launched", "app": app_name}

    def stop_app(self, app_name):
        """Stop a running application.
        
        Args:
            app_name: Name of the application to stop.
            
        Returns:
            Status of the stop operation.
        """
        if app_name in self.running_apps:
            del self.running_apps[app_name]
            return {"status": "stopped", "app": app_name}
        return {"error": "Application not running"}

    def get_running_apps(self):
        """Get list of running applications.
        
        Returns:
            List of running application names.
        """
        return list(self.running_apps.keys())

    def restart_app(self, app_name):
        """Restart an application.
        
        Args:
            app_name: Name of the application to restart.
            
        Returns:
            Status of the restart operation.
        """
        self.stop_app(app_name)
        return self.launch_app(app_name)
