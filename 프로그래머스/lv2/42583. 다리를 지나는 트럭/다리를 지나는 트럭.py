from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    dq = deque(0 for _ in range(bridge_length))
    truck_weights = deque(i for i in truck_weights)
    bridge_weight = 0
    
    while dq:
        answer += 1
        bridge_weight -= dq.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                dq.append(truck)
                bridge_weight += truck
            else:
                dq.append(0)
    return answer