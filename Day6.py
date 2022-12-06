datastream = None

with open("Day6.txt") as f:
    datastream = f.readline()

def find_start_of_packet_marker(data: str, length=4):
    for marker_end in range(length, len(data)):
        marker = set(data[marker_end-length:marker_end])
        if len(marker) == length:
            return marker_end

print(find_start_of_packet_marker(datastream))
print(find_start_of_packet_marker(datastream, 14))