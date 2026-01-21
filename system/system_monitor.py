"""
System monitor for tracking system health and resource usage.
"""

import psutil
from typing import Dict, Any


class SystemMonitor:
    """Monitors system health and resource utilization."""

    def __init__(self):
        """Initialize the system monitor."""
        self.alerts = []
        self.thresholds = {
            "cpu_percent": 80,
            "memory_percent": 85,
            "disk_percent": 90
        }

    def get_system_status(self) -> Dict[str, Any]:
        """Get current system status and resource usage.
        
        Returns:
            Dictionary with system status information.
        """
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory": self._get_memory_info(),
            "disk": self._get_disk_info(),
            "process_count": len(psutil.pids())
        }

    def _get_memory_info(self) -> Dict[str, Any]:
        """Get memory usage information.
        
        Returns:
            Dictionary with memory statistics.
        """
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "percent": mem.percent,
            "used": mem.used
        }

    def _get_disk_info(self) -> Dict[str, Any]:
        """Get disk usage information.
        
        Returns:
            Dictionary with disk statistics.
        """
        disk = psutil.disk_usage('/')
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }

    def check_alerts(self) -> list:
        """Check system status for alerts.
        
        Returns:
            List of active alerts.
        """
        alerts = []
        status = self.get_system_status()
        
        if status["cpu_percent"] > self.thresholds["cpu_percent"]:
            alerts.append(f"CPU usage high: {status['cpu_percent']}%")
        
        if status["memory"]["percent"] > self.thresholds["memory_percent"]:
            alerts.append(f"Memory usage high: {status['memory']['percent']}%")
        
        if status["disk"]["percent"] > self.thresholds["disk_percent"]:
            alerts.append(f"Disk usage high: {status['disk']['percent']}%")
        
        self.alerts = alerts
        return alerts

    def set_threshold(self, metric_name, value):
        """Set alert threshold for a metric.
        
        Args:
            metric_name: Name of the metric.
            value: Threshold value.
        """
        if metric_name in self.thresholds:
            self.thresholds[metric_name] = value

    def get_alerts(self) -> list:
        """Get current alerts.
        
        Returns:
            List of current alerts.
        """
        return self.alerts
