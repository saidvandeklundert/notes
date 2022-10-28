class Example{
    /*
     * Example class as placeholder to
     * expiriment with language features.
     * 
     */
    public int multiply(int a, int b){
        return a * b;
    }

    public void if_else_if(int a){
        if (a==1){
            System.out.println("Value is 1");
        } else if (a >1 |a <10){
            System.out.println("Value is between 1 and 10.");
        } else{
            System.out.println("Value is above 10.");
        }
    }

    public void forloop(int a){
        for (int i = 0;i <a; i++){
            System.out.format("inside for loop:  %d\n", i);
        }
    }

    public void array_create_and_print(){
            int[] ia = new int[101];
            for (int i = 0; i < ia.length; i++) ia[i] = i;
            int sum = 0;
            for (int e : ia) sum += e;
            System.out.println(sum);
            // iterate the array:
            for (int i =0;i<ia.length;i++){
                System.out.println(ia[i]);
            }

        }
}