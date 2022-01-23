Channels are how orchestration is handled in go.

Better not to think about channels as a datastructure. 

When thinking about channels, think about signaling. Channels allow for signaling between the different go routines. This in turn allows for orchestration between the go routines.