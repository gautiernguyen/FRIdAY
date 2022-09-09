import numpy as np

class Event:

    def __init__(self, begin, end, param=None):
        self.begin = begin
        self.end = end
        self.proba = None
        self.duration = self.end-self.begin
def overlapWithList(ref_event, event_list):
    '''
    return the list of the overlaps between an event and the elements of
    an event list
    Have the possibility to have it as the percentage of fthe considered event
    in the list
    '''
    return [overlap(ref_event, elt) for elt in event_list]

def overlap(event1, event2):
    '''return the time overlap between two events as a timedelta'''
    delta1 = min(event1.end, event2.end)
    delta2 = max(event1.begin, event2.begin)
    return max(delta1-delta2, 0)

def get_event_from_timeserie(y, label):

    diffs = np.where(np.diff(y==1))[0]
    if y[0]==1:
        diffs = np.insert(diffs, 0, 0)
    if y[-1]==1:
        diffs = np.insert(diffs, len(diffs), len(y)-1)
    begins = diffs[::2]
    ends = diffs[1::2]
    serie_evtList = []
    for i in range(len(begins)):
        serie_evtList.append(Event(begins[i], ends[i]))
    return serie_evtList

def jaccard(predicted_list, validation_list):
    '''
    compute jaccard indice of two event lists
    '''
    inter = [[overlap(predicted, expected) for predicted in predicted_list] for expected in validation_list]
    return np.sum(inter)/(np.sum([x.duration for x in validation_list])+np.sum([x.duration for x in predicted_list])-np.sum(inter))
