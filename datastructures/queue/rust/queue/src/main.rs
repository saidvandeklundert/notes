/*
Implementation of a queue using a linkedlist
*/
use std::collections::LinkedList;

#[derive(Debug)]
pub struct Queue<T> {
    items: LinkedList<T>,

    
}

impl<T> Queue<T> {
    pub fn new() -> Queue<T> {
        Queue {
            items: LinkedList::new(),
        }
    }

    pub fn enqueue(&mut self, item: T)
     {
        self.items.push_back(item)
        

    }

    pub fn is_empty(self) -> bool {
        return self.items.is_empty();
    }
}

fn main() {
    println!("Hello, world!");
    let mut q = Queue::new();
    q.enqueue(3);
    q.enqueue(2);
    q.enqueue(1);
    println!("{:?}", q);
}

#[cfg(test)]
mod tests {
    use super::Queue;

    #[test]
    fn test_enqueue() {
        let mut queue: Queue<i32> = Queue::new();
        queue.enqueue(64);
        assert_eq!(queue.is_empty(), false);
    }
}
