datastream = None

with open("Day6.txt") as f:
    datastream = f.readline()

def find_start_of_packet_marker(data: str, length=4):
    marker_end = None

    for end in range(length, len(data)):
        marker = set(data[end-length:end])
        if len(marker) == length:
            return end

    return marker_end

print(find_start_of_packet_marker(datastream))
print(find_start_of_packet_marker(datastream, 14))