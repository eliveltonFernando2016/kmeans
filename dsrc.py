class Dsrc:
    def __init__(self, txnid, rxnid, rss, snr):
        self.txnid = txnid
        self.rxnid = rxnid
        self.rss = rss
        self.snr = snr

    def setTxnid(self, txnid):
        self.txnid = txnid
    
    def setRxnid(self, rxnid):
        self.rxnid = rxnid
    
    def setRss(self, rss):
        self.rss = rss

    def setSnr(self, snr):
        self.snr = snr

    def getTxnid(self):
        return self.txnid

    def getRxnid(self):
        return self.rxnid

    def getRss(self):
        return self.rss

    def getSnr(self):
        return self.snr