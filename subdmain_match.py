class Solution(object):
    
    
    
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        res = []
        for cp in cpdomains:
            cp_list=cp.split(" ")
            cp_count=int(cp_list[0])
            dom=cp_list[1].split('.')
            
            #print(cp_count)
            print(dom)
            for i,sub_dom in enumerate(dom):
                string='.'.join(dom[i:])
                if string not in d:
                    d[string]=cp_count
                else:
                    d[string]+=cp_count
        
        #print(d)
        for x,y in d.items():
            res.append(str(y)+" "+x)
        
        return res