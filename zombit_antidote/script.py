from collections import defaultdict


def count_next_meetings(meeting, start_times):
    '''
    Given meeting [start, end] and sorted list of start times,
    returns count of available subsequent meetings.
    '''

    start, end = meeting

    return len([start_time for start_time in start_times if start_time >= end])


def next_best_meeting(meetings, start_times):
    '''
    Given sorted list of meetings, and sorted list of start times,
    returns the meeting from the list that offers the highest number
    of subsequent meetings.
    '''

    best_num_meetings_after = 0
    best_meeting_option = meetings[0]

    for meeting in meetings:
        num_subsequent_meetings = count_next_meetings(meeting, start_times)

        if num_subsequent_meetings > best_num_meetings_after:
            best_num_meetings_after = num_subsequent_meetings
            best_meeting_option = meeting

    return best_meeting_option


def answer(meetings):
    '''
    Given a list of meeting requests, returns the maximum
    number of non-overlapping meetings that can be scheduled.
    '''

    d = defaultdict(list)

    for meeting in meetings:
        cur_start, cur_end = meeting
        d[cur_start].append(cur_end)

    for start, end_times in d.iteritems():
        d[start] = sorted(end_times)

    start_times = d.keys()

    best_schedule = []
    choice_meeting = next_best_meeting(meetings, start_times)
    best_schedule.append(choice_meeting)

    next_meetings = [meeting for meeting in meetings if meeting[0] >= best_schedule[-1][1]]

    while len(next_meetings) > 0:
        choice_meeting = next_best_meeting(next_meetings, start_times)
        best_schedule.append(choice_meeting)

        next_meetings = [meeting for meeting in next_meetings if meeting[0] >= best_schedule[-1][1]]


    return(len(best_schedule))



if __name__ == '__main__':

    meetings = sorted(input())
    output = answer(meetings)
    print(output)
