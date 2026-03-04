import time
print("Tharun G Bhat - 4MW23CS175")
def sliding_window(frames, window_size):
    print(f"Total Frames: {len(frames)}")
    print(f"Window Size: {window_size}\n")
    print("Starting Transmission...\n")
    i = 0
    while i < len(frames):
        window = frames[i:i+window_size]
        print(f"Current Window: {window}")
        for frame in window:
            print(f"Sending Frame {frame}")
            time.sleep(0.5)
        print("All ACKs received for current window.\n")
        i += window_size
        time.sleep(1)
    print("Transmission Complete.")
frames = [1, 2, 3, 4, 5, 6, 7, 8]
sliding_window(frames, 3)

