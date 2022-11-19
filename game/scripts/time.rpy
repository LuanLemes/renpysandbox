label start_time_variables:
    $ week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    $ day_time = ["Morning", "Afternoon", "Evening", "Night"]
    $ current_week_day = 3
    $ current_day_time = 3
    $ current_day = 0
    $ calendar = Calendar(0, week_days, day_time, 0, 0)
    $ c = 0
    return

label time_output_label:
    $ gaming = True
    $ date_output = week_days[current_week_day] + " " + day_time[current_day_time] + " day " + str(current_day)
    "[date_output]"
    "and"
    $ output = calendar.output
    "[output]"
    while gaming == True:
        # $ calendar.add_current_day(1)
        $ calendar.add_current_day_time(1)

        $ output = calendar.output
        "[output]"

    return
