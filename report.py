def print_report(total_time, face_count, audio_count, movement_count):

    print("\n================ FINAL INTERVIEW REPORT ================\n")

    print(f"Total Interview Duration : {total_time} seconds")
    print(f"Multiple Face Detected  : {face_count} times")
    print(f"Multiple Voice Detected : {audio_count} times")
    print(f"Face Movement Detected  : {movement_count} times")

    if face_count > 0 or audio_count > 0 or movement_count > 0:
        print("\n⚠️ Suspicious Activity Detected")
    else:
        print("\n✅ Clean Interview Session")

    print("\n=======================================================\n")
