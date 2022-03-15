class Transfer:
    def __init__(self, fromClub, toClub, player, fee, season, period, isLoan):
        self.fromClub = fromClub
        self.toClub = toClub
        self.player = player
        self.fee = fee
        self.season = season
        self.period = period
        self.isLoan = isLoan

    def __eq__(self, other):
        return self.season == other.season and      \
               self.fromClub == other.fromClub and  \
               self.toClub == other.toClub and      \
               self.fee == other.fee and            \
               self.period == other.period and      \
               self.isLoan == other.isLoan 

    def __lt__(self, other):
        if self.season != other.season:
            return self.season < other.season
        if self.player != other.player:
            return self.player < other.player
        if self.fromClub != other.fromClub:
            return self.fromClub < other.fromClub
        if self.toClub != other.toClub:
            return self.toClub < other.toClub
        if self.period != other.period:
            return self.period < other.period
        return False

    def __str__(self):
        return self.player.__str__() + ": " + \
               self.fromClub.__str__() + " -> " + self.toClub.__str__() + \
               (", loaned for " if self.isLoan else ", sold for ") + \
               str(self.fee) + "M, during " + self.season.__str__()