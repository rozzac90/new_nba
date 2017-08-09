
from new_nba import enums
from new_nba.utils import clean_locals
from new_nba.endpoints.baseendpoint import BaseEndpoint


class Common(BaseEndpoint):

    def commonTeamYears(self, LeagueID=enums.LeagueID.Default):
        """
        Get information on when teams were playing in the league.
    
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :returns: breakdown of min and max year playing in nba by team.
    
        """
        params = clean_locals(locals())
        endpoint = 'commonTeamYears'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return r
    
    def commonallplayers(self, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, IsOnlyCurrentSeason=1):
        """
        Get individual player details.
    
        :param LeagueID: league to retrieve data for.
        :type LeagueID: str
        :param Season: Season for which we require data.
        :type Season: str('%Y-%y')
        :param IsOnlyCurrentSeason: define whether to only get players on a roster in current season.
        :type IsOnlyCurrentSeason: bool(1|0)
        :returns: player information.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'commonallplayers'
        r = self.request(params, endpoint)
        print(r)
        df = self.process_response(r, 0, 'resultSets')
        return r
    
    def commonplayerinfo(self, PlayerID):
        """
        Get detailed information for a player.
    
        :param PlayerID: id of player to get information for.
        :type PlayerID: int
        :returns: detailed player information.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'commonplayerinfo'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def commonplayoffseries(self, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default):
        """
        Get playoff series match ups for a given season.
    
        :param LeagueID: league to retrieve data for.
        :type LeagueID: str
        :param Season: Season for which we require data.
        :type Season: str('%Y-%y')
        :returns: match up by home/away team id and series id.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'commonplayoffseries'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def commonteamroster(self, TeamID, Season=enums.Season.Default):
        """
        Get team roster breakdown.
    
        :param TeamID:
        :type TeamID: int
        :param Season: season for which we require data.
        :type Season: str('%Y-%y')
        :returns: roster breakdown of player details.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'commonteamroster'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def teaminfocommon(self, TeamID, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default):
        """
        Get high level team data.
    
        :param TeamID: id of team for which to get data.
        :type TeamID: int
        :param LeagueID: id of league in which team plays.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param Season: season for which we require data.
        :type Season: str('%Y-%y')
        :param SeasonType: playoff or regular season specification.
        :type SeasonType: nba.nba.bin.enums.SeasonType
        :returns: team information and season record.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'teaminfocommon'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
