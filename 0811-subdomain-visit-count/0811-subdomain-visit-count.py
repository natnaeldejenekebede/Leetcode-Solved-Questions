class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = {}
        
        for domain in cpdomains:
            count, full_domain = domain.split()
            count = int(count)
            subdomains = full_domain.split('.')
            
            for i in range(len(subdomains)):
                curr_domain = '.'.join(subdomains[i:])
                freq[curr_domain] = freq.get(curr_domain, 0) + count
        
        output = [str(freq[key]) + ' ' + key for key in freq]
        
        return output
