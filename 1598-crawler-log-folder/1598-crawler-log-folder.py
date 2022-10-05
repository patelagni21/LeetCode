class Solution:
    def minOperations(self, logs: List[str]) -> int:
        if not logs:
            return 0
        
        s = []
        
        for log in logs:
            if log == '../':
                if s:
                    s.pop()
            elif log == './':
                continue
            else:
                s.append(log)
        
        return len(s)