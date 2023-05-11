from riotwatcher import LolWatcher, ApiError


region = 'na1'

class LeagueAPI:
    def __init__(self, api_token):
        self.token = api_token
        self.lol_watcher = LolWatcher(api_key=self.token)

    def get_summoner(self, summoner_name):
        return self.lol_watcher.summoner.by_name(region, summoner_name)


    def get_puuid(self, summoner_name):
        text_file = open(r"/home/andweste/Tokens/secret_creds_repo/league_ids.txt").readlines()
        puuid = ""
        for line in text_file:
            if line.split(';')[0] == summoner_name:
                puuid = line.split(';')[1].strip()
                break
        return puuid


    def get_recent_matches(self, puuid, count):
        matches = self.lol_watcher.match.matchlist_by_puuid(region=region, puuid=puuid, count=count)
        return matches

    # def get_kda(self, match: LolWatcher.match, puuid):



    # get last x matches for each summoner puuid
    # iterate through and build kda, store as a summoner_history object
    # chart the kda's on one line chart
    # later on can worry about creating a db
    def build_kda(self, summoner_name):
        puuid = self.get_puuid(summoner_name)
        matches = self.get_recent_matches(puuid=puuid, count=10)
        print(matches[0])
