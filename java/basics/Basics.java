// javac Basics.java
// java Basics



class Basics{
    public static void main( String []args){
        // Example program in Java showing the basics.
        // a static method is something that can run without
        // instantiating the class, like in Python.
        System.out.println("Hello world!");

        // Integer declaration:
        int a,c;
        a = 4;
        int b = 10;
        // Create an instance of Example:
        Example Example = new Example();
        c = Example.multiply(a,b);
        Example.if_else_if(1);
        Example.if_else_if(10);
        System.out.format("Value of c:  %d", c);
        Example.forloop(10);
        Example.array_create_and_print();
        Human jan;
        jan = new Human();
        jan.name = "Jan";
        jan.age = 7;
        jan.introduce();
        
        
    }


}