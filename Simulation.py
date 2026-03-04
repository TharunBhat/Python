import matplotlib.pyplot as plt
import time
print("Tharun G Bhat - 4MW23CS175")
print("Q5: Stop-and-Wait ARQ Simulation (Sequence Diagram)")
print("----------------------------------------------")
SENDER_X = 1
RECEIVER_X = 4
y_level = 0
fig, ax = plt.subplots(figsize=(10, 12))
def plot_event(label, event_type, y_start, y_end):
    start_pos, end_pos = (0, 0), (0, 0)
    color, style = 'blue', 'solid'
    if event_type == 'frame':
        start_pos = (SENDER_X, y_start)
        end_pos = (RECEIVER_X, y_end)
        color = 'blue'
    elif event_type == 'ack':
        start_pos = (RECEIVER_X, y_start)
        end_pos = (SENDER_X, y_end)
        color = 'green'
    elif event_type == 'frame_lost':
        start_pos = (SENDER_X, y_start)
        end_pos = (SENDER_X + (RECEIVER_X - SENDER_X) * 0.75, y_start + (y_end - y_start) * 0.75)
        color = 'red'
        style = 'dashed'
        plt.text(end_pos[0], end_pos[1], 'X', color='red', fontsize=16, ha='center', va='center', weight='bold')
    elif event_type == 'ack_lost':
        start_pos = (RECEIVER_X, y_start)
        end_pos = (RECEIVER_X + (SENDER_X - RECEIVER_X) * 0.75, y_start + (y_end - y_start) * 0.75)
        color = 'red'
        style = 'dashed'
        plt.text(end_pos[0], end_pos[1], 'X', color='red', fontsize=16, ha='center', va='center', weight='bold')
    ax.annotate(
        "",
        xy=end_pos,
        xytext=start_pos,
        arrowprops=dict(arrowstyle="->", color=color, linestyle=style, linewidth=1.5),
    )

    mid_x = (start_pos[0] + end_pos[0]) / 2
    mid_y = (start_pos[1] + end_pos[1]) / 2
    plt.text(mid_x, mid_y - 0.1, label, ha='center', va='bottom', fontsize=9,
             bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', pad=0.1))

def plot_timeout(y_level_local):
    plt.text(SENDER_X + 0.1, y_level_local, '       TIMEOUT', color='red', ha='left', va='center', fontsize=9)
    plt.plot([SENDER_X, SENDER_X+0.2, SENDER_X], [y_level_local-0.2, y_level_local, y_level_local+0.2],
             color='red', linestyle='dashed')

def sender(total_frames):
    global y_level
    seq_num = 1
    while seq_num <= total_frames:
        print(f"[SENDER]: Sending Frame {seq_num}...")
        y_start = y_level
        y_end = y_level + 1

        status = receiver(seq_num)

        if status == "ACK_OK":
            plot_event(f"Sending Frame {seq_num}", 'frame', y_start, y_end)
            plot_event(f"Receiving ACK {seq_num}", 'ack', y_end, y_start + 2)
            print(f"[SENDER]: Received ACK {seq_num}. Moving to next frame.\n")
            y_level += 2
            seq_num += 1

        elif status == "FRAME_LOST":
            plot_event(f"Sending Frame {seq_num} (LOST)", 'frame_lost', y_start, y_end)
            plot_timeout(y_end + 0.5)
            print(f"[SENDER]: TIMEOUT (Frame {seq_num} LOST). Retransmitting...\n")
            y_level += 1.5

        elif status == "ACK_LOST":
            plot_event(f"Sending Frame {seq_num}", 'frame', y_start, y_end)
            plot_event(f"Receiving ACK {seq_num} (LOST)", 'ack_lost', y_end, y_start + 2)
            plot_timeout(y_start + 2.5)
            print(f"[SENDER]: TIMEOUT (ACK {seq_num} LOST). Retransmitting...\n")
            y_level += 2.5

        elif status == "DUPLICATE_ACK":
            plot_event(f"Sending Frame {seq_num} (Re-tx)", 'frame', y_start, y_end)
            plot_event(f"Receiving ACK {seq_num} (Re-sent)", 'ack', y_end, y_start + 2)
            print(f"[SENDER]: Received ACK {seq_num} (from re-transmission). Moving to next frame.\n")
            y_level += 2
            seq_num += 1

        time.sleep(0.1)

def receiver(frame_num):
    if frame_num == 3 and not receiver.frame_3_resent:
        print(f"[RECEIVER]: ... Frame 3 LOST in transit ...")
        receiver.frame_3_resent = True
        return "FRAME_LOST"

    if frame_num == 4 and not receiver.ack_4_resent:
        print(f"[RECEIVER]: Received Frame {frame_num}. Sending ACK {frame_num}...")
        print(f"[SENDER]: ... ACK 4 LOST in transit ...")
        receiver.ack_4_resent = True
        return "ACK_LOST"

    if frame_num == 4 and receiver.ack_4_resent:
        print(f"[RECEIVER]: Received DUPLICATE Frame {frame_num}. Discarding. Resending ACK {frame_num}...")
        return "DUPLICATE_ACK"

    print(f"[RECEIVER]: Received Frame {frame_num}. Sending ACK {frame_num}...")
    return "ACK_OK"

receiver.frame_3_resent = False
receiver.ack_4_resent = False

sender(total_frames=5)

print("----------------------------------------------")
print("All frames sent and acknowledged.")
print("Showing simulation diagram...")
plt.vlines([SENDER_X, RECEIVER_X], 0, y_level + 1, color="black", linewidth=2)
plt.text(SENDER_X, -0.5, "Sender", ha='center', fontsize=14, weight='bold')
plt.text(RECEIVER_X, -0.5, "Receiver", ha='center', fontsize=14, weight='bold')
ax.set_ylim(y_level + 1, -1)
ax.set_xlim(0, 5)
ax.axis('off')
plt.title("Stop-and-Wait ARQ Sequence Diagram", fontsize=16)
plt.show()
