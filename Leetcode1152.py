def mostVisitedPattern(username, timestamp, website):
        from collections import defaultdict, Counter
        from itertools import combinations
        users = defaultdict(list)

        for user, time, web in sorted(zip(username, timestamp, website), key= lambda x: (x[0], x[1])):
            users[user].append(web)

        pattern = Counter()

        for user, site in users.items():
            pattern.update(set(combinations(site,3)))
        
        return max(sorted(pattern), key=pattern.get)




if __name__ == '__main__':
    username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
    timestamp = [1,2,3,4,5,6,7,8,9,10]
    website = ["home","about","career","home","cart","maps","home","home","about","career"]
    print(mostVisitedPattern(username, timestamp, website))