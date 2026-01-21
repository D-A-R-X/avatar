"""
Memory filter for filtering and prioritizing memory retrieval.
"""


class MemoryFilter:
    """Filters and prioritizes memories based on relevance and importance."""

    def __init__(self):
        """Initialize the memory filter."""
        self.filters = []
        self.priority_rules = []

    def add_filter(self, filter_func):
        """Add a filter function.
        
        Args:
            filter_func: Callable that filters memories.
        """
        self.filters.append(filter_func)

    def add_priority_rule(self, rule):
        """Add a priority rule for memory ranking.
        
        Args:
            rule: Priority rule to apply.
        """
        self.priority_rules.append(rule)

    def filter_memories(self, memories):
        """Apply filters to memories.
        
        Args:
            memories: List of memories to filter.
            
        Returns:
            Filtered list of memories.
        """
        filtered = memories
        for filter_func in self.filters:
            filtered = [m for m in filtered if filter_func(m)]
        return filtered

    def rank_memories(self, memories):
        """Rank memories by priority.
        
        Args:
            memories: List of memories to rank.
            
        Returns:
            Ranked list of memories.
        """
        return sorted(memories, key=lambda m: self._calculate_priority(m), reverse=True)

    def _calculate_priority(self, memory):
        """Calculate priority score for a memory.
        
        Args:
            memory: The memory to score.
            
        Returns:
            Priority score.
        """
        score = 0
        for rule in self.priority_rules:
            score += rule(memory)
        return score

    def get_relevant_memories(self, memories, query):
        """Get memories relevant to a query.
        
        Args:
            memories: List of memories to search.
            query: Query to match against.
            
        Returns:
            List of relevant memories ranked by priority.
        """
        filtered = self.filter_memories(memories)
        return self.rank_memories(filtered)
