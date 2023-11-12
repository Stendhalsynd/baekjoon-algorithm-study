from collections import deque

def solution(cap, n, deliveries, pickups):
    
    def last_valid_idx(queue):
        while queue and queue[-1] == 0:
            queue.pop()
        return len(queue)
    
    def get_distance(queue_d, queue_p):
        max_distance = max(last_valid_idx(queue_d), last_valid_idx(queue_p))
        return max_distance * 2
    
    def consume_capacity(queue, capacity):
        total = 0
        while queue and total < capacity:
            amount_to_consume = min(queue[-1], capacity - total)
            queue[-1] -= amount_to_consume
            total += amount_to_consume
            if queue[-1] == 0:
                queue.pop()
        return queue
    
    answer = 0 
    deliveries = deque(deliveries)
    pickups = deque(pickups)
    
    while deliveries or pickups:
        answer += get_distance(deliveries, pickups)
        
        deliveries = consume_capacity(deliveries, cap)
        pickups = consume_capacity(pickups, cap)
    
    return answer
