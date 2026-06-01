class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqmap = defaultdict(int)

        for t in tasks:
            freqmap[t] += 1
        
        maxfreq = 0
        maxcount = 0
        for freq in freqmap.values():
            if freq > maxfreq:
                maxfreq = freq
                maxcount = 1
            elif freq == maxfreq:
                maxcount += 1
        
        time = (maxfreq-1) * (n+1) + maxcount

        return max(time, len(tasks))