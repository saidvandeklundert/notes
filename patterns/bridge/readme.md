## Bridge Design Pattern

Intent: Lets you split a large class or a set of closely related classes into
two separate hierarchies—abstraction and implementation—which can be developed
independently of each other.

              A
           /     \                        A         N
         Aa      Ab        ===>        /     \     / \
        / \     /  \                 Aa(N) Ab(N)  1   2
      Aa1 Aa2  Ab1 Ab2



            Exchanges abstraction <-  bridge -> Tradingbot abstraction
    Binance                                         AggroBot
    Coinbase                                        SafeBot


A pitfall of the Bridge Pattern is the risk of overcomplicating things.