package main

import (
	"io"
	"io/ioutil"
	"log"
)

type PersonsBiography struct {
	LifeStory string
	Done      bool
}

func NewReader(LifeStory string) *PersonsBiography {
	return &PersonsBiography{LifeStory, false}
}

func (pb *PersonsBiography) Read(p []byte) (n int, err error) {
	if pb.Done {
		return 0, io.EOF
	}
	for i, b := range []byte(pb.LifeStory) {
		p[i] = b
	}
	pb.Done = true
	return len(pb.LifeStory), nil
}

func main() {
	lifeStory := "then and then, such and such"
	nr := NewReader(lifeStory)
	stuff, _ := ioutil.ReadAll(nr)
	log.Printf("%s", stuff)
}
