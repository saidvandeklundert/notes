fn main() {
    println!("Hello, world!");
    let mut stack = Stack::new(10);
    stack.push(1);
    stack.push(2);
    println!("{:?}",stack);

    println!("{:?}",stack.pop());
    println!("{:?}",stack);
    stack.pop();
    stack.pop();
    stack.pop();
    println!("{:?}",stack.pop());    

}

#[derive(Debug)]
struct Stack{
    items: Vec<i32>
}
impl Stack{
    fn new(size:usize)->Stack{
        return Stack{items:Vec::with_capacity(size).try_into().unwrap()}
    }

    fn push(&mut self, item:i32){
        self.items.push(item);
    }

    fn pop(&mut self)->  Option<i32>{
        self.items.pop()
    }

    fn clear(&mut self){
        self.items.clear();
    }

    fn peek(self)->Option<i32>{
        let return_value = self.items.get(0);
        match return_value {            
            None => return None,
            _ => return Some(return_value.unwrap().clone()),
        }

    }

    fn count(self)->usize{
        return self.items.len()
    }          
}

    
    
    //count()->int
    //is_empty()->bool
    //size()->int
    

#[cfg(test)]
mod tests{
    use super::*;
    #[test]
    fn test_basics(){
        let mut stack = Stack::new(10);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assert_eq!(stack.pop(),Some(3));
        assert_eq!(stack.pop(),Some(2));
        assert_eq!(stack.pop(),Some(1));
        assert_eq!(stack.pop(),None);

    }

    #[test]
    fn test_clear(){
        let mut stack = Stack::new(10);
        stack.push(1);
        stack.clear();
        assert_eq!(stack.pop(),None);
    }

    #[test]
    fn test_peek(){
        let mut stack = Stack::new(10);
        
        stack.push(123);
        
        assert_eq!(stack.peek(),Some(123));
    }    
    #[test]
    fn test_count(){
        let mut stack = Stack::new(10);
        
        stack.push(123);
        stack.push(123);
        stack.push(123);
        
        assert_eq!(stack.count(),3);
    } 
}