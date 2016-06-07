import datetime
import os

def process():
    for root, dirs, files in os.walk('season_1/training_data/order_data'):
        for filename in files:
            if not filename.startswith('.') and filename.startswith('order_data'):
                f = open(os.path.join(root, filename))
                req = {}
                ans = {}

                for line in f:
                    orderid, driverid, userid, start, end, price, timer = line.strip().split('\t')
                    pertimer = timer_sec(timer)
                    if req.has_key((start, pertimer)):
                        req[(start,pertimer)] += 1
                    else:
                        req[(start,pertimer)] = 1

                    if driverid != 'NULL':
                        if ans.has_key((start, pertimer)):
                            ans[(start,pertimer)] += 1
                        else:
                            ans[(start,pertimer)] = 1

                fo = open(os.path.join(root, "proceed_" + filename), "w")
                for i, j in req.iteritems():
                    if not ans.has_key(i):
                        ans[i] = 0
                    fo.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(i[0], i[1], j, ans[i],j-ans[i]))
            


def timer_sec(timer):
	d = datetime.datetime.strptime(timer, "%Y-%m-%d %H:%M:%S")
	piece = (d.hour * 60 + d.minute) / 10 + 1
	return piece



def same_point(district):
    for root, dirs, files in os.walk('season_1/training_data/order_data'):
        for filename in files:
            if filename.startswith('proceed_'):
                f = open(os.path.join("season_1/training_data/order_data", filename))
                ad=[]
                for line in f:
                    address, timerper, request, answer, gap = line.strip().split("\t")
                    if address == district:
                        ad.append((timerper, request))
                ff = open(os.path.join("season_1/training_data/order_data", address),"w")
                for i in ad:
                    ff.write("{0}\t{1}\n".format(i[0],i[1]))
