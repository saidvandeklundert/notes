Call stack is a stack of frames.

Every thread has a call stack.

Every function that is executed is executed in its own frame. In that frame, we will also find all the functions variables.

When the function is done, the frame is popped from the stack and the program resumes by continuing what is then the top frame.

When a function calls another function, a new frame for that is added to the top of the stack. 

When a program creates too many frames on the stack, the computer runs out of memory. This situation is called 'stack overflow'.