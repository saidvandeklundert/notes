class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next



    
def removeKthNodeFromEnd(head, k):    	
	head_start = k
	first_runner = head
	second_runner = head
	second_runner_previous = head
	while first_runner.next is not None:
		if head_start != 0:
			head_start -= 1
			first_runner = first_runner.next
		else :			
			second_runner_previous = second_runner
			second_runner = second_runner.next			
			first_runner = first_runner.next		
    if second_runner is None:
		head.value = head.next.value
		head.next = head.next.next
	else:
        second_runner.next = second_runner.next.next
    