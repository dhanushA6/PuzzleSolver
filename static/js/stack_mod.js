class Stack {
    constructor() {
      this.items = [];
    }

    // push element to the stack
    push(element) {
      this.items.push(element);
    }
  
    // pop element from the stack
    pop() {
      if (this.isEmpty()) return "Underflow";
      return this.items.pop();
    }
  
    // peek the top element of the stack
    peek() {
      return this.items[this.items.length - 1];
    }
  
    // check if the stack is empty
    isEmpty() {
      return this.items.length === 0;
    }
  
    // return the size of the stack
    size() {
      return this.items.length;
    }
  
    // print the stack
    printStack() {
      let str = "";
      for (let i = 0; i < this.items.length; i++)
        str += this.items[i] + " ";
      return str;
    }
  }
  


//   // Example usage:
//   const stack = new Stack();
//   console.log(stack.isEmpty()); // true
  
//   stack.push(10);
//   stack.push(20);
//   stack.push(30);
  
//   console.log(stack.printStack()); // 10 20 30
  
//   console.log("Top element is:", stack.peek()); // 30
  
//   console.log("Popped element:", stack.pop()); // 30
  
//   console.log(stack.printStack()); // 10 20
  