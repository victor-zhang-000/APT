class website(object):
    def __init__(self,name):
        self.name=name
        self.allpeople=set()
    def addpeople(self,people):
        self.allpeople.add(people)
    def __contains__(self, item):
        return (item in self.allpeople)
    def __str__(self):
        return self.name
    def __iter__(self):
        for p in self.allpeople:
            yield p


def highest_affinity(site_list, user_list, time_list):
    log_count=0
    site_unique_list=[]
    site_class_list =[]
    for site in site_list:
        if site not in site_unique_list:
            site_unique_list.append(site)
            site_class_list.append(website(site))

        for ws in site_class_list:
            if site==ws.name:
                ws.addpeople(user_list[log_count])
        log_count += 1

    # start bubble
    site_count=len(site_class_list)
    max_affinity=0
    affinity=0
    return_aff_site=[]

    for i in range(site_count):
        for j in range(i+1,site_count):
            #intersect
            affinity=0
            for p in site_class_list[i]:
                if p in site_class_list[j]:
                    affinity+=1
            if (affinity>max_affinity):
                return_aff_site=[]
                max_affinity=affinity
                return_aff_site.append(site_class_list[i].name)
                return_aff_site.append(site_class_list[j].name)


    return tuple((sorted(return_aff_site)))

    # a set of elements with three values: [website,name,index] the pair of first two values should be unique
    # process

