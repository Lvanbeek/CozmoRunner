import asyncio
import time
import random
import cozmo


def follow_qrs(robot: cozmo.robot.Robot):
    '''The core of the follow_faces program'''

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.util.degrees(0)).wait_for_completed()

    code_to_follow = None

    print("Press CTRL-C to quit")
    while True:
        if code_to_follow:
            #turn = random.choice(-90, 90)
            robot.say_text("I found a cube!").wait_for_completed()
            # start turning towards the face
            robot.go_to_object(code_to_follow, cozmo.robot.util.distance_mm(50)).wait_for_completed()
            robot.say_text("I made it to the code").wait_for_completed()
            if code_to_follow.cube_id is 1:
                robot.say_text("This is Cube 1").wait_for_completed()
                robot.turn_in_place(cozmo.robot.util.Angle(degrees=90)).wait_for_completed()
                robot.say_text("I'm turning").wait_for_completed()
            if code_to_follow.cube_id is 2:
                robot.say_text("This is Cube 2").wait_for_completed()
                robot.turn_in_place(cozmo.robot.util.Angle(degrees=-90)).wait_for_completed()
                robot.say_text("I'm turning").wait_for_completed()
            if code_to_follow.cube_id is 3:
                robot.say_text("This is Cube 3").wait_for_completed()
                robot.turn_in_place(cozmo.robot.util.Angle(degrees=180)).wait_for_completed()
                robot.say_text("I'm turning").wait_for_completed()
            robot.set_head_angle(cozmo.robot.util.degrees(0)).wait_for_completed()
            code_to_follow = None

        if not (code_to_follow and code_to_follow.is_visible):
            # find a visible face, timeout if nothing found after a short while
            try:
                code_to_follow = robot.world.wait_for_observed_light_cube(timeout=None)
            except asyncio.TimeoutError:
                print("I fail")

        time.sleep(.1)


cozmo.run_program(follow_qrs, use_viewer=True, force_viewer_on_top=True)
