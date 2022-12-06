datastream = None

with open("Day6.txt") as f:
    datastream = f.readline()

def find_start_of_packet_marker(data: str):
    marker_end = None

    for end in range(4, len(data)):
        marker = set(data[end-4:end])
        if len(marker) == 4:
            return end

    return marker_end

print(find_start_of_packet_marker(datastream))