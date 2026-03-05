# main.py
# APPENDIX: ADDITIONAL EXERCISES

print("\n" + "=" * 40)
print("APPENDIX EXERCISES")
print("=" * 40)

import access_control
import media_engine

# Student Identity Configuration (copied from main)
LAST_NAME = "Laude"
STUDENT_ID = "TUPM-25-4764"
FAVORITE_ARTIST = "SLIPKNOT"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
CONTROL_NUM = max(1, SEED_DIGIT)

# EXERCISE 1: Secure Access System
print("\n [EXERCISE 1] Secure Access System")


@access_control.audit_log
def secure_access(control, artist):
    level = access_control.compute_access_level(control, artist)
    print(f"    Access Level: {level}")
    print(f"    Threshold: {control * 5}")
    return access_control.validate_access(level, control)


result1 = secure_access(CONTROL_NUM, FAVORITE_ARTIST)
print(f"    Decision: {result1}")

# EXERCISE 1: ASSESSMENT DATA
print("\n" + "=" * 40)
print("EXERCISE 1 ASSESSMENT DATA")
print("=" * 40)
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"FAVORITE_ARTIST Length: {len(FAVORITE_ARTIST)}")
access_level = CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
print(f"Computed Access Level: {access_level}")
threshold = CONTROL_NUM * 5
print(f"Threshold Applied: {threshold}")
print(f"Final Authorization Decision: {result1}")
print("=" * 40)

# EXERCISE 2: Signal Shutdown (with decorator)
print("\n [EXERCISE 2] Signal Shutdown")


# Decorator for Exercise 2
def shutdown_logger(func):
    def wrapper(*args, **kwargs):
        print("        Authorization Started")
        result = func(*args, **kwargs)
        print("        Authorization Completed")
        return result

    return wrapper


@shutdown_logger
def signal_shutdown(power):
    if power == 0:
        print(f"    Signal: {power} - Base case reached")
        return 1
    print(f"    Current signal strength: {power}")
    return 1 + signal_shutdown(power - 1)


start_power = CONTROL_NUM + len(FAVORITE_ARTIST)
print(f"    Initial Power: {start_power}")
calls = signal_shutdown(start_power)
print(f"    Total recursive calls: {calls}")

# EXERCISE 2: ASSESSMENT DATA
print("\n" + "=" * 40)
print("EXERCISE 2 ASSESSMENT DATA")
print("=" * 40)
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"Initial Signal Strength: {start_power}")
print(f"Base Case Condition: Power == 0")
print(f"Total Recursive Calls: {calls}")
print("=" * 40)

# EXERCISE 3: Media Analytics
print("\n [EXERCISE 3] Media Analytics")


@media_engine.monitor
def media_analytics(limit):
    stream = media_engine.play_count_stream(limit)
    total = 0
    count = 0

    print("    Play counts generated:")
    for value in stream:
        print(f"    {value}")
        total += value
        count += 1

    return total, count


stream_limit = CONTROL_NUM + len(FAVORITE_ARTIST)
print(f"    Stream Limits: {stream_limit}")

total_plays, records = media_analytics(stream_limit)

print(f"\n    Total Plays: {total_plays}")
print(f"    Records Processed: {records}")

# EXERCISE 3: ASSESSMENT DATA
print("\n" + "=" * 40)
print("EXERCISE 3 ASSESSMENT DATA")
print("=" * 40)
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"FAVORITE_ARTIST Used: {FAVORITE_ARTIST}")
print(f"Computed Stream Limit: {stream_limit}")
# Generate the play counts to display them
play_counts = []
for i in range(2, stream_limit + 1, 2):
    play_counts.append(i * i)
print(f"Generate Play Counts: {', '.join(map(str, play_counts))}")
print(f"Total Plays: {total_plays}")
print(f"Number of Records Processed: {records}")
print("=" * 40)
