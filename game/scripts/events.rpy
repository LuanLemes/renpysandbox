init python:
    class Calendar(object):
        def __init__(self, current_day, week_days, day_time, current_week_day, current_day_time):
            self.week_days = week_days
            self.day_time = day_time
            self.current_week_day = current_week_day
            self.current_day_time = current_day_time
            self.current_day = current_day
        @property
        def output(self):
            return   self.week_days[self.current_week_day] + " " + self.day_time[self.current_day_time] + " day " + str(self.current_day)

        def add_current_day(self, days):
            self.current_day += days
            self.current_day_time = 0
            if self.current_week_day == 6:
                self.current_week_day = 0
            else:
                self.current_week_day += 1

        def add_current_day_time(self, times):
            if self.current_day_time == 3:
                self.add_current_day(1)
                return
            self.current_day_time +=1
