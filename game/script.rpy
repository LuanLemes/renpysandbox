define e = Character("Eileen", color="FD97E2")
define x = Character(_(''), color="#c8ffc8")
define d = Character("Dave")
image picture_1 = im.Scale("bg cave.jpg", 1920, 1080)
image picture_2 = im.Scale("bg panorama.webp", 1920, 1080)
image picture_3 = im.Scale("bg whitehouse.jpg", 1920, 1080)

label start:
    # call variables
    # call timering
    scene picture_1
    call start_time_variables
    call time_output_label

    # while GameRunning:
    #     "[Hours]:[Minutes]:[Seconds]"
    #     $ Seconds += 1
    #     if Seconds == 60:
    #         $ Seconds = 0
    #         $ Minutes += 7
    #     if Minutes >= 60:
    #         $ Minutes = 0
    #         $ Hours += 1
    #     if Hours == 25:
    #         $ Hours = 0
    #         $ Minutes = 0
    #         $ Seconds = 0


return

# label variables:
#     $ Hours = 0
#     $ Minutes = 0
#     $ Seconds = 0
#     $ GameRunning = True
#     return
